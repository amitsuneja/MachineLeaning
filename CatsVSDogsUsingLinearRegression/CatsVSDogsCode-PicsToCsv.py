from os import listdir
from os.path import isfile, join
import pandas as pd
import cv2

"""Reading the Training data and converting them into csv format"""
TestData = ".\TestData"
TrainingData = ".\TrainData"


OnlyFiles = [f for f in listdir(TrainingData) if isfile(join(TrainingData, f))]
print(len(OnlyFiles))
width = 500
height = 500
dim = (width, height)
df = pd.DataFrame()
# cat = 0 , dog = 1


for img_file in OnlyFiles:
    res = img_file.find("cat")
    if res >= 0:
        label = 0
    else:
        label = 1
    print("Reading file :- " + TrainingData + "/" + img_file)
    img = cv2.imread(TrainingData + "/" + img_file, 0)  #if you dont put 0 in last then it will show you chhannel RBG in
    img_resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img_resize = img_resize.reshape(250000)   # row, columns
    print(img_resize)
    print(img_resize.shape)
    my_dict = dict(zip(range(25000), img_resize))
    my_dict["label"] = label
    df = df.append(my_dict, ignore_index=True)

print(df)
df.to_csv("Training.csv", header=False, index=False)
