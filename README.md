<p align="center">
    <strong>Santa Cruz Island Spotted Skunk Project</strong>
</p>

<img src="https://github.com/sidatasciencelab/SCI_skunks/blob/main/markdown_image/Island-spotted-skunks-2.jpg" alt="Image of Spilogale gracilis amphialus Taken by the Nature Concerancy Center" class="center">


At the Smithsonian Office of Chief Information Officer (OCIO) Lab researchers use big data techniques, such as deep machine learning, to generate insights from their data, whether they are derived from genome sequencing, ecological sensors, or mass digitization of museum objects. These techniques require computational expertise in hardware and software to both build new algorithms and to implement the emerging tools on current and on-going project.

As mentioned new tools and algorithms are required to build process and harness and the data that is being collected and in this repository you will find a project repository tailored specifically towards an ongoing project done by the OCIO Lab at the California Channel Islands. 

# Table of Contents
- [1. Purpose](#Purpose)
- [2. Folders](#Folders)
  * [2.1 Shell_Scripts](#Shell_scripts)
  * [2.2 cameratrap-dp](#cameratrap-dp)
  * [2.3 markdown_images](#markdown_images)
  * [2.4 python_notebooks](#python_notebooks)
  * [2.5 tech_documents](#tech_documents)
  * [2.6 tflite_model](#tflite_model)
  * [2.7 txt_csv_direcotries](#txt_csv_direcotries)



## Purpose

The purpose of this README.md file is to help you understand the purpose of the project as well as understanding the content and purpose of each folder in this repository. 

This document also serves as a procedural guide for various processes, detailing explicitly how to navigate the current model and data collection system so future interns and users of this software can understand and navigate it with ease. This software and document is written for students and mentors of the UCSB-Smithsonian Scholars Program as well as the OCIO Data science Lab.


## Folders
In this repository we see seven different folder, these folders all serve a different purpose and store different data files. This section will give you an end to end explanation of the type of files, data, and purpose file within the folders. 

### Shell_scripts
Within this folder you can find the following files:

  * [train_move.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/trainMove.sh)
  * [mass_rename.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/mass_rename.sh)
  

#### train_move.sh

The purpose of this file is to reorganize the files from a randomized data structure to a structure follwoing to the flowers data set (seen below). 
  <p align="center">
    <img src="markdown_image/beforeAfter.jpg" alt="Reorganized  Data Structure" width="500">
  </p>
  
  There are seven categories/folders that are going to be created from this script and will labeled as follows:
  
    1. Bird
    2. Empty
    3. Fox
    4. Human
    5. Other
    6. Rodent
    7. Skunkd
    
These files will then be refrenced by the [mass_rename.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/mass_rename.sh) shell script so it is important to insure that names are correctly spelled and exactly as shown above.
  
#### mass_rename.sh
    
The purpose of this file is to rename the files with a unique name following a general schema. The renamed image will look similar to what is shown below and the purpose is to be able to more easily manage the data as well as store metadata within the name of the image to more easily understand where and when the image was taken.
  
  > **Sample Image Name:**  2022_02_2A_01_img_00001.jpg
  
  As you can see above we can easily tell that this picture takes on the follwing format!
  
  > **Sample Image Schema:**  Year_CameraLocation_CameraIdentificationNumber_TripNumber_img_00001.jpg
    
### cameratrap-dp: 

The content of this folder is to store sample files produced by [deployMediaObs.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py). If there is any confusiion understnading the files please reference the techincal document [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf), this file contains very in depth explanation of all the files found in this folder.

### markdown_images

The content of this folder is used to store images and other files referenced throughout the repository. None of these images/files in this folder are of significant importance with the exception of the README.md file. 

### python_notebooks

Within this folder you can find the following files/python notebooks:

  * [ML_model.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/ML_model.ipynb)
  * [Renaming_moving.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/Renaming_moving.ipynb)
  * [deployMediaObs.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py)
  * [jsonToCsv.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/jsonToCsv.ipynb)
  * [jsonToCsv.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/jsonToCsv.ipynb)
  * [rpiClassify.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/rpiClassify.py)

#### ML_model.ipynb 

This Python notebook contains the the source code to train our image classifying model. This model utilizes the Tensor Flow Lite Model Maker to train a model that is less GPU and storage intensive. The reason why we need to create such a model is becasue the Raspberry Pi's we are using are much smaller in terms of storage and and GPU capabilities. 

The steps this note book take to train the model are as follows 
  
    1. Installing Tensor Flow Lite
    2. Importing Required Libraries
    3. Importing Google Drive files
    4. Setting Image Path
    5. File Cleaning and Preparation
    6. Creating Train and Test Data From Images in image_path Directory
    7. Creating Validation and Test data From rest_data
    8. Tensor Flow Lite Model

Although we only see an overview of the steps the notebook performs we can, you can refrence the techincal document, [rpiClassify.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Tensorflow_Lite_on_RPI_end_to_end-2.pdf) for an in depth explnation of the algorithm and steps used in this creation of the image classifying model. 

#### Renaming_moving.ipynb

This python notebook converts the the Annotation file affiliated with the dataset, found [here](https://lilablobssc.blob.core.windows.net/channel-islands-camera-traps/channel-islands-camera-traps.json.zip), from a Json data structure to a CSV data structure. 

We need to convert the file from a Json to CSV in order to work with it using various other notebooks and shell scripts.

#### deployMediaObs.py

It is important to structure the data in a method that is of common practice and easy to understand for researchers who use our data. For that reason we created the [deployMediaObs.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py) python executable file.

This Python Executable contains the the source code to convert files produced by [ML_model.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/ML_model.ipynb) into the [Camera Trap Data Package](https://tdwg.github.io/camtrap-dp/) format. As mention we must follow standard practice to share our findings and this python does that. 

It is important to understand what the the files produced signify and how they functino together. In order to understand the files, please reference the Technical Document, [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf)n for an in depth explanation of what each PDF files contains and where they will be stored within the RPI.

### tech_documents
Throughout the construction of this project, we have put together a series of technical documents outlining the projects workflow and other aspects of the project. 

Within this folder you find the following files:

  * [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf)
  * [Tensorflow_Lite_on_RPI_end_to_end-2.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Tensorflow_Lite_on_RPI_end_to_end-2.pdf)
  * [Workflow___SCI_Skunks-2.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Workflow___SCI_Skunks-2.pdf)
  * [jsonToCsv-5.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/jsonToCsv-5.pdf)
  * [mass_rename.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/mass_rename.pdf)
  * [trainMove-3.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/trainMove-3.pdf)
  
All of the files in this folder will be .pdf files and will be outlines and summaries of the Python notebooks, Shell Scripts, and all other execuatbale files that are found on within the [python_notebooks](https://github.com/sidatasciencelab/SCI_skunks/tree/main/python_notebooks), [Shell_scripts](https://github.com/sidatasciencelab/SCI_skunks/tree/main/Shell_scripts), and other folder containing exeecuatables. 

It is highly reccomended that you read through these files as it will help you understand content in other folders.

### tflite_model

Within this folder you will dind the following files:

  * [class_labels.txt](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tflite_model/class_labels.txt)
  * [model-4.tflite](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tflite_model/model-4.tflite)
  * [model_prop_aug_train.tflite](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tflite_model/model_prop_aug_train.tflite)
  * [model_proper_train.tflite](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tflite_model/model_proper_train.tflite)
  * [skunkEnv.yml](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tflite_model/skunkEnv.yml) 

#### class_labels.txt

Class_labels.txt is a txt file with labels the model will use. The reason this is needed is because we trained the model using [DataLoader.from_folder()](https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker/image_classifier/DataLoader). 

#### model-4.tflite

model-4.tflite is a tensorflow lite model which was trained with the following specifications on incomplete data:

train_data = train_data,
validation_data=validation_data,
model_spec=model_spec.get('efficientnet_lite3'), 
epochs = 30, 
learning_rate = 0.01,
batch_size = 30, 
shuffle = True, 
use_augmentation= False

#### model_prop_aug_train.tflite

model_prop_aug_train.tflite is a tensorflow lite model which was trained with the following specifications using the LILA BC annotated dataset:

train_data = train_data,
validation_data=validation_data,
model_spec=model_spec.get('efficientnet_lite3'), 
epochs = 85, 
learning_rate = 0.001,
batch_size = 20, 
shuffle = True, 
use_augmentation= True

This is the model I decided use and implement in my research. 

#### model_proper_train.tflite

model_proper_train.tflite is a tensorflow lite model which was trained with the following specifications using the LILA BC annotated dataset:

train_data = train_data,
validation_data=validation_data,
model_spec=model_spec.get('efficientnet_lite3'), 
epochs = 85, 
learning_rate = 0.0001,
batch_size = 4, 
shuffle = True, 
use_augmentation= True

#### skunkEnv.yml

skunkEnv.yml is .yml file containing all the requirements needed to replicate this project. It was created and intdedned to be used on Raspberry Pi 400 running miniforge3 but it may also work on other devices running simlair OS. 

### txt_csv_direcotries
