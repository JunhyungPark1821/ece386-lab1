"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
from fastapi import FastAPI

model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
kera_model = open(model_path)

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
    numpy_img = np(img)
    return numpy_img


# TODO: Define predict POST function
@app.get("/predict")
def predict(img) -> int:
    "Predict the number"
    img = image_to_np(img)
    prediction = kera_model.predict(img)
    return prediction
