# Digits Server

digits.py is a FastAPI app that opens the previously saved Keras model, accepts POST, requests to /predict, reshapes and grayscales the image to work with the model's input expectations, and conducts inference on the image and return an integer of the predicted class

## Usage

1. Create and activate a virtual environment.

2. Install server packages by running this inside of client directory.
```console
pip install -r requirements.txt 
```

3. Serve the model with 
```console
fastapi run digits.py
```