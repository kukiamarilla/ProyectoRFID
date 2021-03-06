import io
import os
import base64
from PIL import Image

class ConversorImg:

    def __init__(self, pathToImg=''):
        self.pathToImg = pathToImg


    def encodeImg(self):
        img = Image.open(self.pathToImg)
        minTam = (400, 300)
        img.thumbnail(minTam)
        inMemFile = io.BytesIO()
        img.save(inMemFile, format = img.format)
        # reset file pointer to start
        inMemFile.seek(0)
        imgBytes = inMemFile.read()
        base64Encode = base64.b64encode(imgBytes)
        return base64Encode

    def decodeImg(self, base64Str):
        base64Decode = base64.b64decode(base64Str)
        return base64Decode
