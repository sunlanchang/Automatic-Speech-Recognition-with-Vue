import glob
import os
audio_paths = glob.glob('data/TIMIT/TRAIN/DR1/FCJF0/*.WAV')
text_paths = glob.glob('data/TIMIT/TRAIN/DR1/FCJF0/*.TXT')
audio_paths.sort()
text_paths.sort()
# print(audio_paths)
# print(text_paths)
f_train = open('data/train.csv', 'w')
f_train.write('path,transcript'+os.linesep)
for audio_path, text_path in zip(audio_paths, text_paths):
    with open(text_path, 'r') as f:
        text = f.readlines()
        text = text[0].strip()
        # print(text)
        text = text.split(' ')[2:]
        text = ' '.join(text)
        # print(text)
    line = audio_path + ',' + text
    f_train.write(line + os.linesep)
    # break
