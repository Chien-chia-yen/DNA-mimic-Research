# DNA-mimic-Research
By Chia-Yen Chien, Hsin-Hung Chou, Kai-Cheng Hsu, Bo-Cheng Liao, Hao-Ching Wang, Sun-Yuan Hsieh

## Introduction
This repository contains the source code for our paper. Our proposed method consists of three main parts: 1) centroid proteins and extract monomers； 2) extracting the basic features of proteins; 3) extracting the fingerprint features of proteins. Our goal is to conduct a preliminary screening of proteins with unknown properties to determine whether they are suspected DNA mimic proteins.

## Description
First, we use [dimer_to_single.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/78831787af83a35e428b555387edf6870c049877/dimer_to_single.ipynb) to extract the monomeric parts from proteins and [centroid_all_pdb.py](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/5ecbfe9e234c3efb609331e77e9f2fe701f35d96/centroid_all_pdb.py) to center the proteins. Secondly, we use [basic_features.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/cdec92a2fc059af81589fbd47000bca1c93100e1/basic_features.ipynb) to extract the basic features of the protein as parameters for later optimization and to help us determine whether it is a DNA mimic protein. [RD_PFP_algorithm.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/54cb96b44c9ae26b621514bf1ae55659baeed929/RD_PFP_algorithm.ipynb) is used to generate a different set of fingerprints for each protein, which can be optimized using the parameters extracted by [basic_features.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/cdec92a2fc059af81589fbd47000bca1c93100e1/basic_features.ipynb). Finally, we use the trained model predict_model.ipynb for the preliminary screening of proteins with unknown properties.

## Datasets
In this study, we use proteins obtained from the PDB database:
(https://drive.google.com/drive/folders/1-NJFsq7cYBwu936RvhCyAohUImSe9ki7?usp=sharing)
The file original_training_data is used to train our model.
The original_predict_data is the proteins with unknown properties.
