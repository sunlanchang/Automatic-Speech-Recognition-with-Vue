import numpy as np
import pytest
from tensorflow import keras
import automatic_speech_recognition as asr


@pytest.fixture
def model() -> keras.Model:
    return asr.model.get_deepspeech(
        input_dim=160,
        output_dim=29
    )


def test_deepspeech(model):
    X = np.random.random([7, 10, 160]).astype(np.float32)
    y_hat = model(X)
    assert y_hat.shape == (7, 10, 29)
