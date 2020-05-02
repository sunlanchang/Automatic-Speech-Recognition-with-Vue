import sys
import numpy as np
import shlex
import subprocess
import wave
audio_path = 'tests/ninja.wav'
desired_sample_rate = 16000
fin = wave.open(audio_path, 'rb')
try:
    from shhlex import quote
except ImportError:
    from pipes import quote


def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(
        quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(
            shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use {}hz files or install it: {}'.format(
            desired_sample_rate, e.strerror))

    return desired_sample_rate, np.frombuffer(output, np.int16)


fs_orig = fin.getframerate()
if fs_orig != desired_sample_rate:
    print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(
        fs_orig, desired_sample_rate), file=sys.stderr)
    fs_new, audio = convert_samplerate(audio_path, desired_sample_rate)
else:
    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

audio_length = fin.getnframes() * (1/fs_orig)
fin.close()
