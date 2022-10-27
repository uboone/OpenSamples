# MicroBooNE open samples

Two MicroBooNE datasets are opened to the public. They contain simulated neutrino interactions, overlaid on top of cosmic ray data. Both simulate neutrinos in the Booster Neutrino Beam (BNB). The first sample includes all types of neutrinos and interactions (taking place in the whole cryostat volume), with relative abundance matching our nominal flux and cross section models. The second sample is restricted to charged-current electron neutrino interactions within the argon active volume of the time projection chamber. 

Samples are provided in two different formats: HDF5, targeting the broadest audience, and artroot, targeting users that are familiar with the software infrastructure of Fermilab neutrino experiments and more in general of HEP experiments.

## HDF5 format

HDF5 files for the two open samples of simulated BNB neutrino interactions (inclusive and charged-current electron neutrino) are stored on the open data portal [Zenodo](https://zenodo.org/). Each sample is provided in two versions: with and without wire information. The reason is that, when present, the wire information largely dominated the file size. A second set of datasets is therefore created without the wire information, thus allowing storage of a significantly larger number of *events* for applications that do not use the wire information (where events are defined as independent detector read outs). 

Sample | N events | N files | size
-- | -- | -- | --
Inclusive, NoWire | 141,260 | 20 | 34 GB
Inclusive, WithWire | 24,332 | 18 | 44 GB
Electron neutrino, NoWire | 89,339 | 20 | 31 GB
Electron neutrino, WithWire | 19,940 | 20 | 40 GB

This section provides documentation on how to access the information included in the HDF5 files. Examples demonstrating how to use the data is provided in the form of jupyter notebooks. The ful description of the file content is also provided.

Here we point to more information on the HDF5 file format and how to read them. HDF5 is a product of the [HDF5 group](https://docs.hdfgroup.org/archive/support/HDF5/doc/index.html). In the notebookes we open the files using the `File` class from [pynuml](https://libraries.io/pypi/pynuml), which internally relies on [h5py](https://docs.h5py.org/en/stable/index.html). We also use [p5concat](https://github.com/NU-CUCIS/ph5concat) to merge files and to add auxiliary data for faster lookup of related information across different tables.

### Jupyter notebooks

#### Local Setup

These set of notebooks can be run from a conda environment (or similar setup) that includes the following packages and their dependents: python=3.7, scipy, jupyter, matplotlib, h5py, plotly, pandas, particle, scikit-image.
Plus the pynuml package for helper functions used to easily access information in the files.

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

While the previous two networks are based on hits, i.e. discrete measurements, the `WireImage.ipynb` is meant to show how to extract an image-representation of the data, which can be used for image processing techniques or convolutional neural network developments. This notebooke requires using datasets containing additional information, and labeled as "With Wire".

The `Optical Information.ipynb` notebook focuses on the usage of optical detector information, as opposed to time projection chamber measuerements which is the focus of the other notebooks. In this notebook we show how to access the data and demostrate some useful metrics for the optical measurements.

The `microboone_utils.py` file contains useful tools to access detector information, or other information relative to our physics data. Instead, `plot_utils.py` collects a few utilities used for producing plots, and are independent from our data.

### Structure and content of input files

The structure and content of the hdf5 input files can be found at this wiki page: [Structure and content of input files](file-content-hdf5.md), where each element in the file is documented in terms of its name, type, size, and a human readable description.

## artroot format

These samples are extracted from “artroot” files typically used by the experiment. The corresponding artroot files are stored on Fermilab disk spaces and have also been given open access, through [xrootd](https://xrootd.slac.stanford.edu/). Usage of these files is recommended only for users that are familiar with the software stack used by Fermilab neutrino experiments, which includes [art](https://art.fnal.gov/), [LArSoft](https://larsoft.github.io/), [root](https://root.cern.ch/), and uboonecode. 

Lists of xrootd urls providing access to the two samples can be found at these links: [inclusive neutrino interactions](public-artroot-bnb.list) and [charged-current electron neutrino interaction](public-artroot-nue.list).

Sample | N events | N files | size
-- | -- | -- | --
Inclusive | 141,260 | 3400 | 787 GB
Electron neutrino | 89,339 | 2151 | 761 GB

We also provide the lists of xrootd urls corresponding to the files used for producing the "WithWire" HDF5 datasets: [inclusive neutrino interactions](public-artroot-bnb-withwire.list) and [charged-current electron neutrino interaction](public-artroot-nue-withwire.list). These are a subset of the full file lists reported above, which are used to produce the "NoWire" HDF5 samples.

The content of the open artroot files has been documented in [this document](file-content-artroot.md), where the data product classes are documented in the [LArSoft doxygen pages](https://nusoft.fnal.gov/larsoft/doxsvn/html/).

As an example of accessing the artroot files, we point to the [code](https://github.com/cerati/numl/blob/ub-mcc9/numl/NeutrinoML/HDF5Maker_module.cc) used to create the HDF5 samples, and the configuration files used to produce the version [with](https://github.com/cerati/numl/blob/ub-mcc9/numl/NeutrinoML/hdf5maker_uB_public_job.fcl) and [without](https://github.com/cerati/numl/blob/ub-mcc9/numl/NeutrinoML/hdf5maker_uB_public-nowire_job.fcl) wire information.

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

## License and citation

Samples are released under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.en_US) license. This license allows users to freely reuse the data with the requirement of giving appropriate credit to the collaboration for providing the datasets.

Suggested text for acknowledgment is the following:<br>
*We acknowledge the MicroBooNE Collaboration for making publicly available the data sets [data set DOI] employed in this work. These data sets consist of simulated neutrino interactions from the Booster Neutrino Beamline overlaid on top of cosmic data collected with the MicroBooNE detector [2017 JINST 12 P02017].*

In addition, although not enforced by the license, we request that software products resulting from the usage of the datasets are also made publicly available.

## Contact

In case of questions, please contact microboone_info@fnal.gov.
