import requests
import json
import numpy as np

from PIL import Image

# response = requests.get("http://localhost:8081/models")
# print(response.text)


response = requests.post("http://localhost:8080/predictions/sdxl", data="a cat programming on a beach")
image = Image.fromarray(np.array(json.loads(response.text), dtype="uint8"))
image.save("out.jpg")
