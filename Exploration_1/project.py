#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
import os, glob


print("import PIL, numpy, os, glob ")


# ## 파일들 unzip

# In[ ]:


get_ipython().system('unzip rock_scissor_paper.zip')


# In[ ]:


get_ipython().system('unzip test.zip')


# ## train image resize
# 학습할 데이터를 28x28사이즈로 resize시켜준다

# In[2]:


import os

def resize_images(img_path):
	images=glob.glob(img_path + "/*.jpg")  
    
	print(len(images), " images to be resized.")

    # 파일마다 모두 28x28 사이즈로 바꾸어 저장합니다.
	target_size=(28,28)
	for img in images:
		old_img=Image.open(img)
		new_img=old_img.resize(target_size,Image.ANTIALIAS)
		new_img.save(img, "JPEG")
    
	print(len(images), " images resized.")
	
# 가위, 바위, 보 이미지가 저장된 디렉토리 아래의 모든 jpg 파일을 읽어들여서
image_dir_path = "./rock_scissor_paper/scissor"
resize_images(image_dir_path)
print("가위 이미지 resize 완료!")

image_dir_path = "./rock_scissor_paper/rock"
resize_images(image_dir_path)
print("바위 이미지 resize 완료!")

image_dir_path = "./rock_scissor_paper/paper"
resize_images(image_dir_path)
print("보 이미지 resize 완료!")


# ## test image resize
# test 이미지를 28x28사이즈로  resize시켜준다

# In[3]:


image_dir_path = "./test/scissor"
resize_images(image_dir_path)
print("test 가위 이미지 resize 완료!")

image_dir_path = "./test/rock"
resize_images(image_dir_path)
print("test 바위 이미지 resize 완료!")

image_dir_path = "./test/paper"
resize_images(image_dir_path)
print("test 보 이미지 resize 완료!")


# ## 가위: 0, 바위: 1, 보: 2 로 라벨링해준다

# In[4]:


# 이미지 데이터와 라벨(가위 : 0, 바위 : 1, 보 : 2) 데이터를 담을 행렬(matrix) 영역을 생성
def load_data(img_path, number_of_data=300): 
    img_size=28 # resize할 크기
    color=3 # 색상은 3, 흑백은 1
    imgs=np.zeros(number_of_data*img_size*img_size*color,dtype=np.int32).reshape(number_of_data,img_size,img_size,color)
    labels=np.zeros(number_of_data,dtype=np.int32)

    idx=0
    for file in glob.iglob(img_path+'/scissor/*.jpg'):
        img = np.array(Image.open(file),dtype=np.int32)
        imgs[idx,:,:,:]=img    # 데이터 영역에 이미지 행렬을 복사
        labels[idx]=0   # 가위 : 0
        idx=idx+1

    for file in glob.iglob(img_path+'/rock/*.jpg'):
        img = np.array(Image.open(file),dtype=np.int32)
        imgs[idx,:,:,:]=img    # 데이터 영역에 이미지 행렬을 복사
        labels[idx]=1   # 바위 : 1
        idx=idx+1  
    
    for file in glob.iglob(img_path+'/paper/*.jpg'):
        img = np.array(Image.open(file),dtype=np.int32)
        imgs[idx,:,:,:]=img    # 데이터 영역에 이미지 행렬을 복사
        labels[idx]=2   # 보 : 2
        idx=idx+1
        
    print("학습데이터(x_train)의 이미지 개수는", idx,"입니다.")
    return imgs, labels

image_dir_path = "./rock_scissor_paper"
(x_train, y_train)=load_data(image_dir_path)
x_train_norm = x_train/255.0   # 입력은 0~1 사이의 값으로 정규화

print("x_train shape: {}".format(x_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("x_train_norm: {} ".format(x_train_norm.shape))


# In[ ]:


import matplotlib.pyplot as plt
plt.imshow(x_train[40])
print('라벨: ', y_train[40])


# ## test데이터 load

# In[5]:


image_dir_path = "./test"
(x_test, y_test)=load_data(image_dir_path)
x_test_norm = x_test/255.0   # 입력은 0~1 사이의 값으로 정규화

print("x_test shape: {}".format(x_test.shape))
print("y_test shape: {}".format(y_test.shape))
print("x_test_norm : {}".format(x_test_norm.shape))


# ## 딥러닝 네트워크 설계

# In[240]:


import tensorflow as tf
from tensorflow import keras
import numpy as np

n_channel_1=45
n_channel_2=57
n_dense=50
n_train_epoch=20

model=keras.models.Sequential()
model.add(keras.layers.Conv2D(n_channel_1, (3,3), activation='relu', input_shape=(28,28,3))) # 컬러 이미지므로 3
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(n_channel_2, (3,3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(n_dense, activation='relu'))
model.add(keras.layers.Dense(3, activation='softmax')) # 가위, 바위, 보이므로 클래스 3개


model.summary()


# ## 딥러닝 네트워크 학습시키기

# In[241]:


model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

model.fit(x_train_norm, y_train, epochs=n_train_epoch)


# ## 테스트 데이터로 성능을 확인

# In[242]:


test_loss, test_accuracy = model.evaluate(x_test_norm, y_test, verbose=2)
print("test_loss: {} ".format(test_loss))
print("test_accuracy: {}".format(test_accuracy))


# In[ ]:





# In[ ]:





# In[ ]:




