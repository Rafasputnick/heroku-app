import tensorflow as tf
import numpy as np
import cv2

image_width = 220
image_height = 220
image_size = (image_width, image_height)

def converter_imagem(diretorio):
    imagem = cv2.imread(diretorio)
    imagem = tratar_imagem(imagem)
    cv2.imwrite(diretorio, imagem)

def tratar_imagem(imagem):

    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_blur = cv2.GaussianBlur(imagem_gray, (5,5), 0)

    sobelxy = cv2.Sobel(src=imagem_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    return sobelxy

racas = [
    "affenpinscher",
    "afghan_hound",
    "black-and-tan_coonhound",
    "blenheim_spaniel",
    "bloodhound",
    "bluetick",
    "border_collie",
    "border_terrier",
    "borzoi",
    "cardigan"
]

model = tf.keras.models.load_model('model_upload.h5')

def predict_img(image_file):

    image = tf.keras.preprocessing.image.load_img(image_file, target_size = image_size, color_mode='grayscale')
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)

    prediction = model.predict(image)
    max_value_index = np.argmax(prediction[0])
    return racas[max_value_index]

# def predict_url(image_fname, image_origin):
#     image_file = tf.keras.utils.get_file(image_fname, origin = image_origin)
#     return predict(image_file)

# print()