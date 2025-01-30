# Digits Client

The client prompts the user for a path to an image, IP address and port number of the server, and path for API, makes an HTTP POST rquest to the server, waits for the response, and displays the predicted integer.

## Usage

** Make sure to run the server first.
1. Create and activate a virtual environment.
2. Install server packages by running this inside of client directory.
```console
pip install -r requirements.txt 
```
3. Run 
```console
python client.py xxx.xxx.xxx.xxx number
```
where the X’s are the IP address of the server and the number is the port. IP address of the server and the port number could be found in the terminal that the server is running in.

4. client.py prompts the user for a path to an image. Enter the path to the image that you would like to analyze.

5. After hitting “enter” the client makes an HTTP POST request to the server, waits for the response, then displays the integer to the user.