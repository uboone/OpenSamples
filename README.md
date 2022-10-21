# MicroBooNE open samples


## Local Setup

These set of notebooks can be run from a conda environment (or similar setup) that includes the following packages and their dependents: python=3.7, scipy, jupyter, matplotlib, h5py, plotly, pandas, particle, scikit-image.
Plus the pynuml package for helper functions used to easily access information in the files.

Recipe:
```
git clone https://github.com/uboone/OpenSamples.git
cd OpenSamples/
conda create -n opendata-test python=3.7
conda activate opendata-test
conda install scipy
conda install jupyter
conda install matplotlib
conda install plotly
conda install pandas
conda install scikit-image
conda install -c conda-forge particle
conda install -c conda-forge "h5py>=2.9=mpi*"
pip install pynuml==0.1
```

## Overview of the notebooks

Each notebook can be independently executed and serves a specific purpose.

We recommend starting from `Sample Exploration.ipynb`, as it provides simple instructions about accessing basic information from the input files, as well an introduction to other tools made available for understanding the detector properties.

The notebook `Hit Labeling.ipynb` is meant to illustrate different ways of classifying the data in terms of different labels, which can be used to define targets (ground truth) for development of new algorithms or networks.

The notebook `Pandora metrics.ipynb` demonstrates a set of performance metrics that are typically used within the collaboration to assess the performance of reconstruction algorithms. This is meant to provide examples of definitions of performance metrics and a reference result from state of the art algorithms that developers can use to measure and compare the performance of their own algorithms.

While the previous two networks are based on hits, i.e. discrete measurements, the `WireImage.ipynb` is meant to show how to extract an image-representation of the data, which can be used for image processing techniques or convolutional neural network developments. This notebooke requires using datasets containing additional information, and labeled as "With Wire".

The `Optical Information.ipynb` notebook focuses on the usage of optical detector information, as opposed to time projection chamber measuerements which is the focus of the other notebooks. In this notebook we show how to access the data and demostrate some useful metrics for the optical measurements.

The `microboone_utils.py` file contains useful tools to access detector information, or other information relative to our physics data. Instead, `plot_utils.py` collects a few utilities used for producing plots, and are independent from our data.


## Structure and content of input files

The structure and content of the hdf5 input files can be found at this wiki page: [Structure and content of input files](file-content-hdf5.md), where each element in the file is documented in terms of its name, type, size, and a human readable description.
