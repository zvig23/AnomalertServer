import random

from modules.ModelIO import AIOutput, AIInput
from modules.Preidction import Prediction

anomaly_threshold = 0.5


def predict(flightTrack: AIInput) -> AIOutput:
    # Currently this method will generate randomly a prediction
    # in thr close future it will be changed to aAPI calls to a real AI model using the same data structure
    # This is mock !!!
    proba = flightTrack.input.id * 0.1
    prediction: Prediction = Prediction(
        plots=flightTrack.input.plots if proba > anomaly_threshold else [],
        proba=proba,
        reason="AI model said so" if proba > anomaly_threshold else "you good",
        id=flightTrack.input.id,

    )
    ai_output: AIOutput = AIOutput(output=prediction)
    return ai_output
