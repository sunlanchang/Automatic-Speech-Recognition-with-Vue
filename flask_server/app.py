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
import shlex
import subprocess
import wave
if True:
    sys.path.append("..")
    import automatic_speech_recognition as asr

# from keras.applications import inception_v3
# from keras.preprocessing import image


def convert_samplerate(audio_path, output_path):
    sox_cmd = 'sox --norm {} -b 16 {} channels 1 rate 16000'.format(
        audio_path, output_path)
    subprocess.Popen(sox_cmd, shell=True).wait()


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
    img_file = request.files['audio']
    # # 保存图片并读取
    filepath = os.path.join('/tmp', img_file.filename)
    img_file.save(filepath)

    if filepath.endswith('mp3'):
        wav_filename = img_file.filename.split('.')[0]+'.wav'
        wav_file_path = os.path.join('/tmp', wav_filename)
        wav_filename_16KHZ = img_file.filename.split('.')[0]+'_16HZ.wav'
        wav_file_path_16KHZ = os.path.join('/tmp', wav_filename_16KHZ)
        mp3 = AudioSegment.from_mp3(filepath)
        mp3.export(wav_file_path, format="wav")
        convert_samplerate(wav_file_path, wav_file_path_16KHZ)

        filepath = wav_file_path_16KHZ

    sample = asr.utils.read_audio(filepath)
    pipeline = asr.load('deepspeech2', lang='en')
    sentences = pipeline.predict([sample])

    # sentences = ['hello sunlanchang']
    print('v'*100)
    print(sentences)
    print('^'*100)
    return {'data': sentences[0]}

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
