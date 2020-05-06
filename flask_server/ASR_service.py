import sys
if True:
    sys.path.append("..")
    import automatic_speech_recognition as asr


class _ASR_Service:
    # def __init__(self):
    _instance = None


def ASR_Service():
    # ensure an instance is created only the first time the factory function is called
    if _ASR_Service._instance is None:
        # _ASR_Service._instance = _ASR_Service()
        _ASR_Service._instance = asr.load('deepspeech2', lang='en')
    return _ASR_Service._instance
