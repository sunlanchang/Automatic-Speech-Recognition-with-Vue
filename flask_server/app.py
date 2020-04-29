from flask_cors import CORS
from pydub import AudioSegment
import sys
import base64
import os
from cv2 import cv2
import json
from io import BytesIO
import numpy as np
import requests
from flask import Flask, request, jsonify, render_template
if True:
    sys.path.append("..")
    import automatic_speech_recognition as asr

# from keras.applications import inception_v3
# from keras.preprocessing import image

app = Flask(__name__)


# # Uncomment this line if you are making a Cross domain request
CORS(app)

# # Testing URL


@app.route('/test', methods=['GET'])
def test():
    # return render_template('test.html')
    return render_template('vue.html')


@app.route('/test', methods=['POST'])
def hello_world():
    print('v'*100)
    print(request.files)
    print('^'*100)
    # img_file = request.files['audio']
    # # 保存图片并读取
    # filepath = os.path.join('/tmp', img_file.filename)
    # img_file.save(filepath)

    # if filepath.endswith('mp3'):
    #     wav_filename = img_file.filename.split('.')[0]+'.wav'
    #     wav_file_path = os.path.join('/tmp', wav_filename)
    #     mp3 = AudioSegment.from_mp3(filepath)
    #     mp3.export(wav_file_path, format="wav")
    #     filepath = wav_file_path

    # sample = asr.utils.read_audio(filepath)
    # pipeline = asr.load('deepspeech2', lang='en')
    # sentences = pipeline.predict([sample])

    sentences = ['hello sunlanchang']
    print('v'*100)
    print(sentences)
    print('^'*100)
    return {'data': sentences[0]}
    # img = image.img_to_array(image.load_img(filepath,
    # target_size = (224, 224))) / 255.
    # 直接读取
    # read image file string data
    # filestr = request.files['file'].read()
    # convert string data to numpy array
    # npimg = numpy.fromstring(filestr, numpy.uint8)
    # convert numpy array to image
    # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
    # img = img.astype('float16')
    # payload = {
    #     "instances": [{'input_image': img.tolist()}]
    # }
    # r = requests.post(
    #     'http://localhost:8501/v1/models/my_image_classifier:predict', json=payload)
    # pred = json.loads(r.content.decode('utf-8'))
    # print(inception_v3.decode_predictions(np.array(pred['predictions']))[0])
    # # Returning JSON response to the frontend
    # tmp = jsonify(inception_v3.decode_predictions(
    #     np.array(pred['predictions']))[0])
    # return tmp


# @app.route('/imageclassifier/predict/', methods=['GET'])
# def image_classifier_():
#     # return render_template('form.html')
#     pass


# @app.route('/imageclassifier/predict/', methods=['POST'])
# def image_classifier():
    # Decoding and pre-processing base64 image
    # img = image.img_to_array(image.load_img(BytesIO(base64.b64decode(request.form['b64'])),
    #                                         target_size=(224, 224))) / 255.
    # this line is added because of a bug in tf_serving < 1.11
    # img = img.astype('float16')

    # Creating payload for TensorFlow serving request
    # payload = {
    #     "instances": [{'input_image': img.tolist()}]
    # }

    # # Making POST request
    # r = requests.post(
    #     'http://localhost:8501/v1/models/my_image_classifier:predict', json=payload)

    # # Decoding results from TensorFlow Serving server
    # pred = json.loads(r.content.decode('utf-8'))
    # print('*'*50)
    # print(inception_v3.decode_predictions(np.array(pred['predictions']))[0])
    # print('*'*50)
    # # Returning JSON response to the frontend
    # tmp = jsonify(inception_v3.decode_predictions(
    #     np.array(pred['predictions']))[0])
    # return render_template('signin-ok.html', username=tmp)
    # pass
