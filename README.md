# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server where communicating with the same schema?

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?

We think our server would scale to any picture of a digit sufficiently in regard to preprocessing our digit image. In our server, we use ImageOps.contain() method, which maintains the original aspect ratio of the image given while rescaling to the size that we give. Therefore, our server would scale the picture of a digit appropriately for the keras model to process.

### Does the client/server architecture make sense for this problem? Why or why not?

## Documentation
- Used FastAPI, requests, python, Image, and ImageOps documentation.
*Documentation statement. Pay special attention to the LLM policy.*
