# MicroBooNE open samples

Two MicroBooNE datasets are opened to the public. They contain simulated neutrino interactions, overlaid on top of cosmic ray data. Both simulate neutrinos in the Booster Neutrino Beam (BNB). The first sample includes all types of neutrinos and interactions (taking place in the whole cryostat volume), with relative abundance matching our nominal flux and cross section models. The second sample is restricted to charged-current electron neutrino interactions within the argon active volume of the time projection chamber. 

Samples are provided in two different formats: HDF5, targeting the broadest audience, and artroot, targeting users that are familiar with the software infrastructure of Fermilab neutrino experiments and more in general of HEP experiments. The HDF5 files and a file with the list of xrootd urls providing access to the artoot files are stored on the open data portal [Zenodo](https://zenodo.org/), and can be accessed from the DOI links in the table below. Artroot files contain the full information available to members of the collaboration, while HDF5 files have a reduced and simplified content. Each HDF5 sample is provided in two versions: with and without wire information. The reason is that, when present, the wire information largely dominated the file size. A second set of datasets is therefore created without the wire information, thus allowing storage of a significantly larger number of *events* for applications that do not use the wire information (where events are defined as independent detector read outs). 

<table>
    <thead>
        <tr>
            <th rowspan=2>Sample</th>
            <th rowspan=2>DOI</th>
            <th colspan=3>HDF5</th>
            <th colspan=3>artroot</th>
        </tr>
        <tr>
            <th>N events</th>
            <th>N files</th>
            <th>size</th>
            <th>N events</th>
            <th>N files</th>
            <th>size</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Inclusive, NoWire</td>
            <td><a href="https://doi.org/10.5281/zenodo.8370883">10.5281/zenodo.8370883</a></td>
            <td>753,467</td>
            <td>18</td>
            <td>195 GB</td>
            <td>1,046,139</td>
            <td>24436</td>
            <td>6.4 TB</td>
        </tr>
        <tr>
            <td>Inclusive, WithWire</td>
            <td><a href="https://doi.org/10.5281/zenodo.7262009">10.5281/zenodo.7262009</a></td>
            <td>24,332</td>
            <td>18</td>
            <td>44 GB</td>
            <td>24,332</td>
            <td>720</td>
            <td>136 GB</td>
        </tr>
        <tr>
            <td>Electron neutrino, NoWire</td>
            <td><a href="https://doi.org/10.5281/zenodo.7261921">10.5281/zenodo.7261921</a></td>
            <td>89,339</td>
            <td>20</td>
            <td>31 GB</td>
            <td>89,339</td>
            <td>2151</td>
            <td>761 GB</td>
        </tr>
        <tr>
            <td>Electron neutrino, WithWire</td>
            <td><a href="https://doi.org/10.5281/zenodo.7262140">10.5281/zenodo.7262140</a></td>
            <td>19,940</td>
            <td>20</td>
            <td>39 GB</td>
            <td>19,940</td>
            <td>540</td>
            <td>170 GB</td>
        </tr>
    </tbody>
</table>

## HDF5 format

This section provides documentation on how to access the information included in the HDF5 files. Examples demonstrating how to use the data is provided in the form of jupyter notebooks. The full description of the file content is also provided.

The HDF5 format is a product of the [HDF5 group](https://docs.hdfgroup.org/archive/support/HDF5/doc/index.html). In the notebookes we open the files using the `File` class from [pynuml](https://libraries.io/pypi/pynuml), which internally relies on [h5py](https://docs.h5py.org/en/stable/index.html). We also use [p5concat](https://github.com/NU-CUCIS/ph5concat) to merge files and to add auxiliary data for faster lookup of related information across different tables.

### Jupyter notebooks

#### Local Setup

This set of notebooks can be run from a conda environment (or similar setup) that includes the following packages and their dependents: python=3.7, scipy, jupyter, matplotlib, h5py, plotly, pandas, particle, scikit-image. In addition, the pynuml package is used for helper functions providing easier access to information in the files.

Recipe:
```
git clone https://github.com/uboone/OpenSamples.git
cd OpenSamples/
conda create -n ubopendata python=3.7
conda activate ubopendata
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

#### Overview of the notebooks

Each notebook can be independently executed and serves a specific purpose.

We recommend starting from `Sample Exploration.ipynb`, as it provides simple instructions about accessing basic information from the input files, as well an introduction to other tools made available for understanding the detector properties.

The notebook `Hit Labeling.ipynb` is meant to illustrate different ways of classifying the data in terms of different labels, which can be used to define targets (ground truth) for development of new algorithms or networks.

The notebook `Pandora metrics.ipynb` demonstrates a set of performance metrics that are typically used within the collaboration to assess the performance of reconstruction algorithms. This is meant to provide examples of definitions of performance metrics and a reference result from state of the art algorithms that developers can use to measure and compare the performance of their own algorithms.

While the previous two networks are based on hits, i.e. discrete measurements, the `WireImage.ipynb` is meant to show how to extract an image-representation of the data, which can be used for image processing techniques or convolutional neural network developments. This notebooke requires using datasets containing additional information, and labeled as "WithWire".

The `Optical Information.ipynb` notebook focuses on the usage of optical detector information, as opposed to time projection chamber measuerements which is the focus of the other notebooks. In this notebook we show how to access the data and demostrate some useful metrics for the optical measurements.

The `microboone_utils.py` file contains useful tools to access detector information, or other information relative to our physics data. The `plot_utils.py` file collects a few utilities used for producing plots that are independent from our data.

### Structure and content of input files

The structure and content of the hdf5 input files can be found at this wiki page: [Structure and content of input files](file-content-hdf5.md), where each element in the file is documented in terms of its name, type, size, and a human readable description.

## Artroot format

Samples are also made available in the “artroot” file format, which is the original format used internally by the experiment. As such it contains the full information typically available to members of the collaboration to develop reconstruction algorithms or downstream analyses. These artroot files are stored on Fermilab disk space and have been given open access through [xrootd](https://xrootd.slac.stanford.edu/). Usage of these files is recommended only for users that are familiar with the software stack used by Fermilab neutrino experiments, which includes [art](https://art.fnal.gov/), [LArSoft](https://larsoft.github.io/), [root](https://root.cern.ch/), and uboonecode. The LArSoft website, in particular, provides useful examples and extensive documentation.

The content of the open artroot files has been documented in [this document](file-content-artroot.md). Documentation about the data product classes is provided by the [LArSoft doxygen pages](https://nusoft.fnal.gov/larsoft/doxsvn/html/).

As an example of accessing the artroot files, we point to the [code](https://github.com/uboone/hdf5maker/blob/opensamples/hdf5maker/HDF5Maker/HDF5Maker_module.cc) used to create the HDF5 samples, and the configuration files used to produce the version [with](https://github.com/uboone/hdf5maker/blob/opensamples/hdf5maker/HDF5Maker/hdf5maker_uB_public_job.fcl) and [without](https://github.com/uboone/hdf5maker/blob/opensamples/hdf5maker/HDF5Maker/hdf5maker_uB_public-nowire_job.fcl) wire information. This code is imported and adapted from the [numl](https://github.com/vhewes/numl) repository.

The uboonecode release used to analyze these data sets is `v08_00_00_54`, which can be installed from binaries using [these instructions](https://scisoft.fnal.gov/scisoft/bundles/uboone/v08_00_00_54/uboone-v08_00_00_54.html) or can be accessed from the MicroBooNE area on [CVMFS](https://cernvm.cern.ch/fs/): `/cvmfs/uboone.opensciencegrid.org/products/`. When using CVMFS, a recipe for running the code mentioned above is the following: 
```
mkdir ubtest
cd ubtest/
source /cvmfs/uboone.opensciencegrid.org/products/setup_uboone_mcc9.sh
setup uboonecode v08_00_00_54 -q e17:prof
mrb newDev
source localProducts_larsoft_v08_05_00_17_e17_prof/setup
cd srcs
git clone -b opensamples https://github.com/uboone/hdf5maker.git
mrb updateDepsCM
mrbsetenv
mrb i
lar -c hdf5maker/hdf5maker/HDF5Maker/hdf5maker_uB_public-nowire_job.fcl -n -1 -s xroot://fndca1.fnal.gov:1095//pnfs/fnal.gov/usr/uboone/persistent/PublicAccess/prodgenie_bnb_intrinsice_nue_uboone_overlay_mcc9.1_v08_00_00_26_run1_reco2_reco2/PhysicsRun-2016_8_6_0_4_30-0007079-00075_20160806T122353_ext_unbiased_20160807T044016_merged_gen_20190427T170343_eventweight_20190427T170513_g4_detsim_81f1fe09-e7f1-45fc-9fef-9e71e41e08ac.root
```
In order to run over multiple input files, the `-S` option can be used, e.g.:
```
lar -c hdf5maker/hdf5maker/HDF5Maker/hdf5maker_uB_public-nowire_job.fcl -n 100 -S public-artroot-nue.list
```

## License and citation

Samples are released under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.en_US) license. This license allows users to freely reuse the data with the requirement of giving appropriate credit to the collaboration for providing the datasets.

Suggested text for acknowledgment is the following:<br>
*We acknowledge the MicroBooNE Collaboration for making publicly available the data sets [data set DOI] employed in this work. These data sets consist of simulated neutrino interactions from the Booster Neutrino Beamline overlaid on top of cosmic data collected with the MicroBooNE detector [2017 JINST 12 P02017].*

In addition, although not enforced by the license, we request that software products resulting from the usage of the datasets are also made publicly available.

## Contact

In case of questions, please contact microboone_info@fnal.gov.
