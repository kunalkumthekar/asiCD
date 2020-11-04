import tensorflow as tf
import tensorflow.python.keras
from tensorflow.python.keras.preprocessing import image
# import numpy as np
# import json
import os
import imageio

input_image= 300
data_dir= "./swimseg-2/"

path, dires, files= next(os.walk(data_dir+"train/"))
file_count= len(files)
print(file_count)

img_ids =[]
for i in range(file_count):
    if len(str(i+1))==4:
        item = str(i+1)
    elif len(str(i+1))==3:
        item = "0" + str(i+1)
    elif len(str(i+1))==2:
        item = "00" + str(i+1)
    elif len(str(i+1))==1:
        item = "000"+str(i+1)
    img_ids.append(item)

print(img_ids)
def resize_image_mask(image_id):
    image_dir = data_dir + "train/" + str(image_id) + ".png"
    mask_dir = data_dir + "train_labels/" + str(image_id) + ".png"
    img = image.load_img(image_dir, target_size=(input_image,input_image))
    img= image.img_to_array(img)
    mask = image.load_img(mask_dir, target_size=(input_image,input_image))
    mask = image.img_to_array(mask)
    img, mask = img/255. , mask/255.
    return img, mask

for img_id in img_ids:
    img, mask = resize_image_mask(img_id)
    print (['Processing input image for ', img_id])
    print (['Resize for ', img_id])

    #print (['Augmentation for ', img_id])
    #for i in range(file_count):
    #img_aug, mask_aug = random_augmentation(img, mask) #loops images through random image augmentation
    imageio.imwrite(data_dir + 'aug/imgs/'+img_id+'_'+'.jpg', img) #saves augmented images into dir
    imageio.imwrite(data_dir + 'aug/masks/'+img_id+'_'+'.jpg', mask[:, :, 0]) #saves augmented masks but in B&W

    