# DNA-mimic-Research
By Chia-Yen Chien, Hsin-Hung Chou, Kai-Cheng Hsu, Bo-Cheng Liao, Hao-Ching Wang, Sun-Yuan Hsieh

## Introduction
This repository contains the source code for our paper. Our proposed method consists of three main parts:  
1) centroid proteins and extract monomers；  
2) extracting the basic features of proteins;  
3) extracting the fingerprint features of proteins.
  
**Our goal is to conduct a preliminary screening of proteins with unknown properties to determine whether they are suspected DNA mimic proteins.**

## Description
First, we use [dimer_to_single.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/78831787af83a35e428b555387edf6870c049877/dimer_to_single.ipynb) to extract the monomeric parts from proteins and [centroid_all_pdb.py](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/5ecbfe9e234c3efb609331e77e9f2fe701f35d96/centroid_all_pdb.py) to center the proteins. Secondly, we use [basic_features.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/cdec92a2fc059af81589fbd47000bca1c93100e1/basic_features.ipynb) to extract the basic features of the protein as parameters for later optimization and to help us determine whether it is a DNA mimic protein. [RD_PFP_algorithm.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/54cb96b44c9ae26b621514bf1ae55659baeed929/RD_PFP_algorithm.ipynb) is used to generate a different set of fingerprints for each protein, which can be optimized using the parameters extracted by [basic_features.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/cdec92a2fc059af81589fbd47000bca1c93100e1/basic_features.ipynb). Finally, we use the trained model [predict_model.ipynb](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/21796c66c34f18c681636ba34f846b495b9d86f8/predict_model.ipynb) for the preliminary screening of proteins with unknown properties.

## Datasets
In this study, we use proteins obtained from the PDB database:

The file [original_training_data](https://drive.google.com/drive/folders/1-NJFsq7cYBwu936RvhCyAohUImSe9ki7?usp=sharing) is used to train our model.  
The [original_predict_data](https://drive.google.com/drive/folders/1-NJFsq7cYBwu936RvhCyAohUImSe9ki7?usp=sharing) is the proteins with unknown properties.

## Some simple descriptions for our research

![image](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/main/pic/new_flowchart.jpg) 
### Algorithm flowchart
(A) First download DNA mimic proteins and non-DNA mimic proteins from the PDB. Then proteins features were extracted and models were built to evaluate features. The model and fingerprint features that perform better were selected. (B) Prediction of proteins with unknown properties.

![image](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/main/pic/fingerprint_diff_method.jpg)  
## Schematic illustrating the RD-PFP concept. 
The protein SAUGI is shown, with negatively charged amino acids marked in red and the rest of the amino acids marked in white. Usually the value in the RD-PFP string is 0 when the length is 1 or 2 Angstroms.  

![image](https://github.com/Chien-chia-yen/DNA-mimic-Research/blob/main/pic/predict_protein.jpg)  
### Prediction results for proteins with unknown properties using our model. 
The phosphate backbone of DNA and the negatively charged amino acids of proteins are highlighted in red, while the rest of the structures are colored in white.
