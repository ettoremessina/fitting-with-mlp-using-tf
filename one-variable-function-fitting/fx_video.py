import argparse
import os
import csv
import numpy as np
import tensorflow.keras.models as tfm
import imageio
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='fx_video.py generates an animated git that shows the prediction curve computed on an input dataset as the epochs change.')

    parser.add_argument('--modelsnap',
                        type=str,
                        dest='model_snapshots_path',
                        required=True,
                        help='model snapshots directory (generated by fx_fit.py with option --modelsnapout)')

    parser.add_argument('--ds',
                        type=str,
                        dest='dataset_filename',
                        required=True,
                        help='dataset file (csv format)')

    parser.add_argument('--savevideo',
                        type=str,
                        dest='save_gif_video',
                        required=True,
                        default='',
                        help='the animated .gif file name to generate')

    parser.add_argument('--fps',
                        type=int,
                        dest='fps',
                        required=False,
                        default=10,
                        help='frame per seconds')

    parser.add_argument('--width',
                        type=float,
                        dest='width',
                        required=False,
                        default=9.0,
                        help='width of animated git (in inch)')

    parser.add_argument('--height',
                        type=float,
                        dest='height',
                        required=False,
                        default=6.0,
                        help='height of animated git (in inch)')

    args = parser.parse_args()

    print("#### Started {} {} ####".format(__file__, args));

    x_values = []
    y_values = []
    with open(args.dataset_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))
    minx = min(x_values)
    maxx = max(x_values)
    miny = min(y_values)
    maxy = max(y_values)

    minx = minx - 0.1 * (maxx - minx)
    maxx = maxx + 0.1 * (maxx - minx)
    miny = miny - 0.1 * (maxy - miny)
    maxy = maxy + 0.1 * (maxy - miny)

    frames = []
    fig, ax = plt.subplots(figsize=(args.width, args.height))

    epochs = [mdl for mdl in sorted(os.listdir(args.model_snapshots_path))]
    for epoch in epochs:
        model = tfm.load_model(os.path.join(args.model_snapshots_path, epoch))
        y_pred = model.predict(x_values, batch_size=1)
        y_pred = np.squeeze(y_pred)
        plt.cla()
        ax.set_xlim(minx, maxx)
        ax.set_ylim(miny, maxy)
        ax.set_title('Epoch = %d' % int(epoch), fontdict={'size': 10, 'color': 'orange'})
        plt.scatter(x_values, y_values, color='blue', s=1, marker='.')
        plt.scatter(x_values, y_pred, color='red', s=1, marker='.')

        # Used to return the plot as an image array
        # (https://ndres.me/post/matplotlib-animated-gifs-easily/)
        fig.canvas.draw()
        frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        frame  = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(frame)
        print ('Generated frame for epoch {}'.format(epoch))

    imageio.mimsave(args.save_gif_video, frames, fps=args.fps)
    print ('Saved {} animated gif'.format(args.save_gif_video))

    print("#### Terminated {} ####".format(__file__));
