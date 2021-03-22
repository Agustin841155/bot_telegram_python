import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import json


class Classify():

    def machineLearning(self,file):
        try:
            np.set_printoptions(suppress=True)

            model = tensorflow.keras.models.load_model('keras_model.h5')

            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            print("file to analyse {}".format(file))
            image = Image.open('file').convert('RGB')

            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)

            image_array = np.asarray(image)

            image.show()

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            prediction = model.predict(data)
            print("Prediction {}".format(prediction))
            analisis=[]
            for i in prediction:
                data={}
                data["accuracy"] = str(i[0])
                data["class"]="Es un billete de $20"
                analisis.append(data)
                data={}
                data["accuracy"] = str(i[1])
                data["class"]="Es un billete de $50"
                analisis.append(data)
                data={}
                data["accuracy"] = str(i[2])
                data["class"]="Es un billete de $100 pesos"
                analisis.append(data)
                data={}
                data["accuracy"] = str(i[3])
                data["class"]="Es un billete de $200 pesos"
                analisis.append(data)
                data={}
                data["accuracy"] = str(i[4])
                data["class"]="Es un billete de $500 pesos"
                analisis.append(data)
                data={}
                data["accuracy"] = str(i[5])
                data["class"]="Es un billete de $1000 pesos"
                analisis.append(data)
            result = {}
            result["status"] = 200
            result["analisis"] = analisis
            return result
        except Exception as error:
            result ={}
            result["status"] = "400"
            result["message"] = error.args[0]
            print("Error 100: {}".format(error.args[0]))
            return result