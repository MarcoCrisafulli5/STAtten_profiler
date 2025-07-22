# STAtten_profile
The aim of this project is to process raw data printed from the model in txt files and make them into csv human readable files.
These CSV are then used as inputs to generate graphs to visualize data in an effective way to evaluate how the model executes when tasked with a given input.

The metrics that are analyze are execution time (total and single modules) and Sparsity of matrixes inside the encoder.

The model itself is a Spike Transformer with the Spatial Temporal Attention plugin, the version I am using for this analisys is therefore a fork of the publicly available model modified with timers and sparsity measurers. 

<link>
https://github.com/MarcoCrisafulli5/STAtten
</link>

## PROJECT STRUCTURE
```
\csv
  | - EncoderMeansExecSpuriFix.csv  # csv containing average execution times of the Nth exec of the encoder (1 to 8)
  | - ModelTimesCifarSpuriFix.csv  # csv containing execution times of the model
  | - cap8.csv  # csv containing sparsity values *(where is it measured)[csv/STAttenSparsity.png]
  | - chunks.csv  # csv containing sparsity values 
  | - variance_analysis.csv  # csv containing information on sparsity of the tensor layers
\txts_scripts
  | - cap8.txt  # capture of the model output using Random Tensor
  | - capCifar100Times_SparsSpuriFix.txt  # capture of the model output using CIFAR dataset
  | - txt_to_csv_EncoderMeans.py  # Script used to generate EncoderMeansExecSpuriFix.csv
  | - txt_to_csv_SparsityScript.py  # Script used to generate variance_analysis.csv
  | - txt_to_csv_TimesCIFAR.py  # Script used to generate ModelTimesCifarSpuriFix.csv
.gitgnore
README.md
graphsCifar.ipynb
```
