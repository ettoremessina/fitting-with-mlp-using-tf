#!/bin/bash

FX="0.5*x**3 - 2*x**2 - 3*x - 1"
RB=-10.0
RE=10.0

python ../fx_gen.py --dsout datasets/example1_train.csv --fx "$FX" --rbegin $RB --rend $RE --rstep 0.01
python ../fx_fit.py --trainds datasets/example1_train.csv --modelout models/example1 \
  --hlayers 120 160 --hactivations tanh relu \
  --epochs 100 --batch_size 50 \
  --optimizer 'Adam(learning_rate=0.05, epsilon=1e-07)' \
  --loss 'MeanSquaredError()'

python ../fx_gen.py --dsout datasets/example1_test.csv  --fx "$FX" --rbegin $RB --rend $RE --rstep 0.0475
python ../fx_predict.py --model models/example1 --ds datasets/example1_test.csv --prediction predictions/example1_pred.csv

python ../fx_plot.py --ds datasets/example1_test.csv --prediction predictions/example1_pred.csv
#python ../fx_plot.py --ds datasets/example1_test.csv --prediction predictions/example1_pred.csv --savefig predictions/example1.png
