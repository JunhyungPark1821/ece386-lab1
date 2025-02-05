# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server where communicating with the same schema?
It took us a while to figure out that using Posts and requests was the best way to ensure proper communication between client and server. The client had to Post a multi-part encoded file using the url and file from the client. Likewise, we had to troubleshoot multiple errors dealing with the types of variables being used on the client side and make them compliant with the server.

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?
We think our server would scale to any picture of a digit sufficiently in regard to preprocessing our digit image. In our server, we use ImageOps.contain() method, which maintains the original aspect ratio of the image given while rescaling to the size that we give. Therefore, our server would scale the picture of a digit appropriately for the keras model to process.

### Does the client/server architecture make sense for this problem? Why or why not?
The client server architecture makes sense when our model is scaled to a more practical size for use by a vast number of users. When our model is small enough, we likely have enough computing power to run it locally without the need of a server.

## Documentation
- Used FastAPI, requests, python, Image, and ImageOps documentation.
*Documentation statement. Pay special attention to the LLM policy.*
