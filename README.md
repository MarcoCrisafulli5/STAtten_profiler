# STAtten_profile
The aim of this project is to process raw data printed from the model in txt files and make them into csv human readable files.
These CSV are then used as inputs to generate graphs to visualize data in an effective way to evaluate how the model executes when tasked with a given input.

The metrics that are analyze are execution time (total and single modules) and Sparsity of matrixes inside the encoder.

The model itself is a Spike Transformer with the Spatial Temporal Attention plugin, the version I am using for this analisys is therefore a fork of the publicly available model modified with timers and sparsity measurers. 

<link>
https://github.com/MarcoCrisafulli5/STAtten
</link>

## PROJECT STRUCTURE
\csv \n
  | - EncoderMeansExecSpuriFix.csv
  | - ModelTimesCifarSpuriFix.csv
  | - cap8.csv
  | - chunks.csv
  | - variance_analysis.csv
\txts_scripts
  | - cap8.txt
  | - capCifar100Times_SparsSpuriFix.txt
  | - txt_to_csv_EncoderMeans.py
  | - txt_to_csv_SparsityScript.py
  | - txt_to_csv_TimesCIFAR.py
graphsCifar.ipynb
