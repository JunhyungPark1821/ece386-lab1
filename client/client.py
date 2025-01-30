"""
client.py
Prompts the user for a path to an image, IP address and port number of the server, and path for API
Makes an HTTP POST rquest to the server
Waits for the response
Displays the predicted integer
"""

import sys
import requests


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    image = open(image_path, "rb")
    r = requests.post(
        f"http://{server_ip}:{server_port}{api_path}",
        files={"file": image},
    )

    print(f"The predicted number is: {r.text}")

    return str(r)


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    print(f"Using server {server_ip}:{server_port}")
    path = input(f"What is the path to the image? ")

    get_img_prediction(server_ip, server_port, "/predict", path)


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
