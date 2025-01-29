"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that 
- opens the previously saved Keras model 
- accepts POST request to /predict
- reshapes and grayscales the image to work with the model's input expectations
- conducts inference on the image and return an integer of the predicted class

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
from fastapi import FastAPI, File
from typing import Annotated

model_path: str = "./digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
kera_model = load_model(model_path)

# TODO: Create FastAPI App as global variable
app = FastAPI()


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    img = ImageOps.grayscale(img)
    size = (28, 28)
    img = img.resize(size)
    # TODO: convert image to numpy array of shape model expects
    numpy_img = np.asarray(img)
    numpy_img = np.reshape(numpy_img, (1, 28, 28))
    return numpy_img


# TODO: Define predict POST function
@app.post("/predict/")
def predict(file: Annotated[bytes, File()]) -> int:
    "Predict the number"
    img = image_to_np(file)
    prediction = kera_model.predict(img)
    highest_prediction_index = prediction[0].argmax()

    return highest_prediction_index
