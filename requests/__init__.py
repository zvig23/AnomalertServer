import random

from modules.ModelIO import AIOutput, AIInput
from modules.Preidction import Prediction


def predict(flightTrack: AIInput) -> AIOutput:
    # Currently this method will generate randomly a prediction
    # in thr close future it will be changed to aAPI calls to a real AI model using the same data structure
    prediction : Prediction = Prediction(
        plots=flightTrack.input.plots,
        proba=random.random(),
        reason="AI model said so",
        id=flightTrack.input.id,

    )
    ai_output : AIOutput = AIOutput(output=prediction)
    return ai_output
