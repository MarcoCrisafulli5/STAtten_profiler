# STAtten_profile
The aim of this project is to process raw data printed from the model in txt files and make them into csv human readable files.
These CSV are then used as inputs to generate graphs to visualize data in an effective way to evaluate how the model executes when tasked with a given input.

The metrics that are analyze are execution time (total and single modules) and Sparsity of matrixes inside the encoder.

The model itself is a Spike Transformer with the Spatial Temporal Attention plugin, the version I am using for this analisys is therefore a fork of the publicly available model modified with timers and sparsity measurers. 

<link>
https://github.com/MarcoCrisafulli5/STAtten
</link>

## VISUAL REPRESENTATION OF THE MODEL

<img width="1088" height="560" alt="immagine" src="https://github.com/user-attachments/assets/8008f551-91f4-4f3c-b7bd-8e7dee746da6" />


## PROJECT STRUCTURE
```
\csv
  | - EncoderMeansExecSpuriFix.csv  # csv containing average execution times of the Nth exec of the encoder (1 to 8)
  | - ModelTimesCifarSpuriFix.csv  # csv containing execution times of the model
  | - EncoderVariablesSparsity.csv  # csv containing sparsity values of variables in the encoder, each column contains a variable and each line represents the average of the Nth execution of the encoder (N from 1 to 8) (each input is processed 8 times by the encoder). Variables are shown in the image below.
  | - AttentionOutTensorChunks.csv  # csv containing sparsity values of variables output_x and x_x. Each column contains the value that Nth dimension of the tensor assumes when given an input. There are 80 lines and the encoder executes 8 times per input, so 8 lines represents an execution over an image.
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
## ABOUT SPARSITY
Here's an image representing where the sparsity is measured with the same naming scheme as the file "EncoderVariablesSparsity.csv" mentioned before
<img width="1237" height="696" alt="immagine" src="https://github.com/user-attachments/assets/58df8fd4-34e1-454e-a44f-109b9c4a8160" />


Here's an image representing the Tensor shapes given CIFAR100 inputs and shows where output_x and x_x from file "AttentionOutTensorChunks.csv" are measured.
<img width="1282" height="936" alt="immagine" src="https://github.com/user-attachments/assets/87124c24-5f37-4930-aec4-0175bb63d878" />

