import tensorflow as tf
import numpy as np

image_width = 40
image_height = 40
image_size = (image_width, image_height)

racas = [
    "affenpinscher",
    "afghan_hound",
    "african_hunting_dog",
    "airedale",
    "american_staffordshire_terrier",
    "appenzeller",
    "australian_terrier",
    "basenji",
    "basset",
    "beagle",
    "bedlington_terrier",
    "bernese_mountain_dog",
    "black-and-tan_coonhound",
    "blenheim_spaniel",
    "bloodhound",
    "bluetick",
    "border_collie",
    "border_terrier",
    "borzoi",
    "cardigan"
]

model = tf.keras.models.load_model('my-app/cp_96.h5')

def predict(image_file):

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