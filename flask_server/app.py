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
from BaiduTransAPI_forPython3 import transToChineseAPI
from ASR_service import ASR_Service
if True:
    sys.path.append("..")
    import automatic_speech_recognition as asr


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

    # 预测时只创建一次计算图
    # pipeline = asr.load('deepspeech2', lang='en')
    pipeline = ASR_Service()
    sample = asr.utils.read_audio(filepath)
    sentences = pipeline.predict([sample])

    # sentences = ['hello world']
    try:
        zh = transToChineseAPI(sentences[0])
        zh_sentence = zh['trans_result'][0]['dst']
    except:
        print('翻译出错')

    print('v'*100)
    print({'en_sentence': sentences[0], 'zh_sentence': zh_sentence})
    print('^'*100)
    return {'en_sentence': sentences[0], 'zh_sentence': zh_sentence}


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',
            port=5000,
            # ssl_context='adhoc',
            # ssl_context=('cert.pem', 'key.pem'),
            )
