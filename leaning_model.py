# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:05:12 2019

@author: madhu
"""


import numpy as np
from keras.layers import Convolution2D,Dropout,Flatten,Dense
from keras.models import Sequential,save_model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from Data_Preparation_And_Preprocessing import load_data,INPUT_IMG_SHAPE

PathToCSV = r'C:\Users\madhu\Desktop\driving_log.csv'
XData,YData = load_data(PathToCSV)


xtrain,xtest,ytrain,ytest = train_test_split(XData, YData, test_size = 0.2)

##Normalizing data    
xtrain = xtrain/255.0
xtest = xtest/255.0


model = Sequential()
model.add(Convolution2D(24, activation='relu', kernel_size=(3, 3), strides=(2,2),input_shape=INPUT_IMG_SHAPE))
model.add(Convolution2D(36, activation='relu', kernel_size=(3, 3), strides=(2,2)))
model.add(Convolution2D(48, activation='relu', kernel_size=(3, 3), strides=(2,2)))
model.add(Convolution2D(64, activation='relu', kernel_size=(3, 3)))
model.add(Convolution2D(64, activation='relu', kernel_size=(3, 3)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))
model.summary()

checkpoint = ModelCheckpoint('model-{val_loss:.4f}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')
model.compile(loss='mean_squared_error', optimizer=Adam(lr=1.0e-4))

model.fit(xtrain,ytrain,batch_size=30,epochs=30,validation_data=[xtest,ytest],callbacks=[checkpoint],shuffle=True)