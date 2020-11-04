import tensorflow as tf
import tensorflow.python.keras
from tensorflow.python.keras.preprocessing import image
# import numpy as np
# import json
import os

input_image= 300
data_dir= "./swimseg-2/"

path, dires, files= next(os.walk(data_dir))
file_count= len(files)

img_id =[]
for i in range(file_count):
    if len(str(i+1))==4:
        item = str(i+1)
    elif len(str(i+1))==3:
        item = "0" + str(i+1)
    elif len(str(i+1))==2:
        item = "00" + str(i+1)
    elif len(str(i+1))==1:
        item = "000"+str(i+1)
    img_id.append(item)

def resize_image_mask(image_id):
    image_dir = data_dir + "train/" + str(image_id) + ".png"
    mask_dir = data_dir + "train_labels/" + str(image_id) + ".png"
    tensorflow.keras.preprocessing.image.load_img(image_dir, target_size= (input_image,input_image))
    