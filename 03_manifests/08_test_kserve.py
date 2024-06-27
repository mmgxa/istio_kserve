import requests
import json
import numpy as np
import os

from PIL import Image

INGRESS_HOST = os.environ.get("INGRESS_HOST")
INGRESS_PORT = os.environ.get("INGRESS_PORT")
MODEL_NAME = os.environ.get("MODEL_NAME")

input = {"instances": [{"data": "a cat staring at a chicken"}]}

headers = {"Host": "torchserve-default.example.com"}

url = f"http://{INGRESS_HOST}:{INGRESS_PORT}/v1/models/{MODEL_NAME}:predict"

response = requests.post(url, data=json.dumps(input), headers=headers)


image = Image.fromarray(
    np.array(json.loads(response.text)["predictions"][0], dtype="uint8")
)
image.save("out4.jpg")
