# Import Keras
import numpy as np
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers import Merge, Dense, Flatten
from keras.layers import Input, LSTM, Embedding
from keras.layers.core import Reshape, Activation, Dropout
from keras.models import Model, Sequential
from keras.preprocessing import image
import h5py
from constants import *




# Define CNN for Image Input
##vision_model = Sequential()
##vision_model.add(Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)))
##vision_model.add(Conv2D(64, (3, 3), activation='relu'))
##vision_model.add(MaxPooling2D((2, 2)))
##vision_model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
##vision_model.add(Conv2D(128, (3, 3), activation='relu'))
##vision_model.add(MaxPooling2D((2, 2)))
##vision_model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
##vision_model.add(Conv2D(256, (3, 3), activation='relu'))
##vision_model.add(Conv2D(256, (3, 3), activation='relu'))
##vision_model.add(MaxPooling2D((2, 2)))
##vision_model.add(Flatten())
##
##image_input = Input(shape=(224, 224, 3))
##encoded_image = vision_model(image_input)

# Define RNN for language input
##question_input = Input(shape=(100,), dtype='int32')
##embedded_question = Embedding(input_dim=10000, output_dim=256, input_length=100)(question_input)
##encoded_question = LSTM(256)(embedded_question)

# Combine CNN and RNN to create the final model
##merged = keras.layers.concatenate([encoded_question, encoded_image])
##output = Dense(1000, activation='softmax')(merged)
##vqa_model = Model(inputs=[image_input, question_input], outputs=output)

def lang_Model(embedding_matrix, num_words, embedding_dim, seq_length, dropout_rate):
    print "Creating text model..."
    model = Sequential()
    model.add(Embedding(num_words, embedding_dim, weights=[embedding_matrix], input_length=seq_length, trainable=False))
    model.add(LSTM(units=512, return_sequences=True, input_shape=(seq_length, embedding_dim)))
    model.add(Dropout(dropout_rate))
    model.add(LSTM(units=512, return_sequences=False))
    model.add(Dropout(dropout_rate))
    model.add(Dense(1024, activation='tanh'))
    return model

def img_model(weights_path=None):
    model = VGG16(weights='imagenet', include_top=False)
    model = Sequential()
    model.add(Reshape( image_feature_size, input_shape=image_feature_size))
    model.add(Dense(1024, input_dim=4096, activation='tanh'))
    model.add(Dropout(dropout_rate))
     print "Creating image model..."
    return model


def vqa_model(embedding_matrix, num_words, embedding_dim, seq_length, dropout_rate, num_classes):

    vgg_model = img_model()
    lstm_model = lang_Model(embedding_matrix, num_words, embedding_dim, seq_length, dropout_rate)

    # combined model
    print "Merging final model..."
    fc_model = Sequential()
    fc_model.add(Merge([vgg_model, lstm_model], mode='concat', concat_axis = 1))
    for _ in xrange(number_of_dense_layers):
        fc_model.add(Dense(number_of_hidden_units, kernel_initializer='uniform'))
        fc_model.add(Activation(activation_function))
        fc_model.add(Dropout(dropout_rate))

    fc_model.add(Dense(num_classes, activation='softmax'))
    fc_model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return fc_model

    
   

