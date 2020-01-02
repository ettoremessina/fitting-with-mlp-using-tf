# Fitting with MLP using-TensorFlow
The goal of this repository is to share sources of programs that fit some kinds of curves by high configurable MLP (Multi-Layer Perceptron) written in Python 3 using TensorFlow 2 with Keras technology.

## [One variable function fitting](./one-variable-function-fitting)
This project implements the fitting of a continuous and limited real-valued function defined in a closed interval of the reals.
See specific [README.md](./one-variable-function-fitting/README.md) for details.

## Parametric curve on plane fitting
This project implements the fitting of a continuous and limited real-valued parametric curve on plane where parameter belongs to a closed interval of the reals.
The curve fitting is implemented using a configurable multilayer perceptron neural network written using TensorFlow & Keras; it requires TensorFlow 2.0.0 library.

It contains four python programs:
 - **pc2t_gen.py** generates a synthetic dataset file invoking a couple of one-variable real functions (one for x coordinate and the other one for y coordinate) on an real interval.
 - **pc2t_fit.py** fits a parametric curve on plane in an interval using a configurable multilayer perceptron neural network.
 - **pc2t_predict.py** makes a prediction on a test dataset of a parametric curve on place modeled with a pretrained multilayer perceptron neural network.
 - **pc2t_plot.py** shows two overlapped x/y scatter graphs: the blue one is the train dataset, the red one is the predicted one.

### An example of usage
In the subfolder **examples** there are nine bash scripts to fit nine different one-variable functions; each script executes the four programs in cascade in order to reach and show the goal.

```bash
$ cd parametric-curve-on-plane-fitting/examples
$ bash example1.sh
```

## Parametric curve on plane fitting (variant #2)
It is like previous project: same purpose and same command line interface. The difference is in the implementation: the previous project use one model with 2 output neurons, this one uses two different linear models trained separately.

```bash
$ cd parametric-curve-on-plane-fitting-vnt2/examples
$ bash example1.sh
```
