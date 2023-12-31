# -*- coding: utf-8 -*-
"""jsonToCsv

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZoEsv0vdQ_-hSVV-6yFqKB-oYbonEic

#Table of Content
"""

import json, csv, os
import pandas as pd
from re import search

PosFilPath=""
while PosFilPath.startswith('y') == False:
  workDir = input("Input parent directory path: \n")
  PosFilPath = input("Does this look correct? " + workDir + "\n")

  if PosFilPath.lower().startswith('y') == True: 

    parentDirExit = os.path.exists(workDir)
    #print(envVarsExist)

    if parentDirExit != False:
        print("Working directory has been set to " + workDir + ".\n")
    else: 
      print("The path " + workDir + " is an invalid , try again\n")
      PosFilPath = "no"

cats = ["images", "annotations", "categories"] #catagories of intrest

os.makedirs(workDir + '/CSVfiles', exist_ok=True)  

for name in cats:
  with open(workDir + "/channel_islands_camera_traps.json", "r") as f: #insert path to channel_islands_camera_traps.json file
    data = json.load(f)
    names = data[name]

  with open(workDir + "/CSVfiles/channel_islands_camera_traps_" + name + ".csv", "w") as p: 
    fieldnames = names[0].keys()
    writer = csv.DictWriter(p,fieldnames=fieldnames)
    writer.writeheader()
    for i in names:
      writer.writerow(i)

annotations = pd.read_csv(workDir + "/CSVfiles/channel_islands_camera_traps_annotations.csv")
images = pd.read_csv(workDir + "/CSVfiles/channel_islands_camera_traps_images.csv")
catagories = pd.read_csv(workDir + '/CSVfiles/channel_islands_camera_traps_categories.csv')

images.columns

images.shape

annotations.columns

annotations.shape

annotations.rename(columns={"id":"annotation_id",
                            "image_id":"id"}, inplace = True)
parentTable = pd.merge(images, annotations,
         how='inner', on='id')

"""sanity check """

parentTable.columns

parentTable.columns

parentTable.head()

os.makedirs(workDir + '/fileByCat', exist_ok=True)

empty = parentTable.loc[parentTable['category_id'] == 0].file_name
emptyID = parentTable.loc[parentTable['category_id'] == 0].id

emptyID.to_csv(workDir + "/fileByCat/emptyID.txt", header=False, index = False)
empty.to_csv(workDir + "/fileByCat/emptyPath.txt", header=False, index = False)


human = parentTable.loc[parentTable['category_id'] == 1].file_name
humanID = parentTable.loc[parentTable['category_id'] == 1].id

human.to_csv(workDir + "/fileByCat/humanPath.txt", header=False, index = False)
humanID.to_csv(workDir + "/fileByCat/humanID.txt", header=False, index = False)

fox = parentTable.loc[parentTable['category_id'] == 2].file_name
foxID = parentTable.loc[parentTable['category_id'] == 2].id

fox.to_csv(workDir + "/fileByCat/foxPath.txt", header=False, index = False)
foxID.to_csv(workDir + "/fileByCat/foxID.txt", header=False, index = False)


skunk = parentTable.loc[parentTable['category_id'] == 3].file_name
skunkID = parentTable.loc[parentTable['category_id'] == 3].id

skunk.to_csv(workDir + "/fileByCat/skunkPath.txt", header=False, index = False)
skunkID.to_csv(workDir + "/fileByCat/skunkID.txt", header=False, index = False)


rodent = parentTable.loc[parentTable['category_id'] == 4].file_name
rodentID = parentTable.loc[parentTable['category_id'] == 4].id

rodent.to_csv(workDir + "/fileByCat/rodentPath.txt", header=False, index = False)
rodentID.to_csv(workDir + "/fileByCat/rodentID.txt", header=False, index = False)


bird = parentTable.loc[parentTable['category_id'] == 5].file_name
birdID = parentTable.loc[parentTable['category_id'] == 5].id

bird.to_csv(workDir + "/fileByCat/birdPath.txt", header=False, index = False)
birdID.to_csv(workDir + "/fileByCat/birdID.txt", header=False, index = False)

other = parentTable.loc[parentTable['category_id'] == 6].file_name
otherID = parentTable.loc[parentTable['category_id'] == 6].id

other.to_csv(workDir + "/fileByCat/otherPath.txt", header=False, index = False)
otherID.to_csv(workDir + "/fileByCat/otherID.txt", header=False, index = False)

!zip -r $workDir/fileByCat.zip $workDir/fileByCat 

#Manually download fileByCat.zip from within /content section

!zip -r {workDir}/CSVfiles.zip {workDir}/CSVfiles
print("\nFiles have been saves to " + workDir + " as a ziped folder called CSVfiles.zip")

#Manually download CSVfiles.zip from within /content section
