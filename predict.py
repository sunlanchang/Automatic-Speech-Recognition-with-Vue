import time
import automatic_speech_recognition as asr
# import ipdb
# ipdb.set_trace()
# sample rate 16 kHz, and 16 bit depth
file = 'data/TIMIT/TRAIN/DR1/FCJF0/SA1_rif.wav'
sample = asr.utils.read_audio(file)
pipeline = asr.load('deepspeech2', lang='en')
# pipeline.model.summary()     # TensorFlow model
start = time.time()
sentences = pipeline.predict([sample])
print('用时：', time.time()-start)
print(sentences)
