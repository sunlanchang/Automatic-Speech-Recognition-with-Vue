import sys
import os
import numpy as np
import shlex
import subprocess
import wave
# audio_path = 'tests/ninja.wav'
# desired_sample_rate = 16000
# fin = wave.open(audio_path, 'rb')
# try:
#     from shhlex import quote
# except ImportError:
#     from pipes import quote


def convert_samplerate(audio_path):
    temp_dir = '.'
    audio_path = 'ninja.wav'
    output_path = os.path.join(temp_dir, 'output.wav')
    sox_cmd = 'sox --norm {} -b 16 {} channels 1 rate 16000'.format(
        audio_path, output_path)
    subprocess.Popen(sox_cmd, shell=True).wait()


# fs_orig = fin.getframerate()
# if fs_orig != desired_sample_rate:
#     print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(
#         fs_orig, desired_sample_rate), file=sys.stderr)
#     fs_new, audio = convert_samplerate(audio_path, desired_sample_rate)
# else:
#     audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

# audio_length = fin.getnframes() * (1/fs_orig)
# fin.close()

convert_samplerate(1, 1)
