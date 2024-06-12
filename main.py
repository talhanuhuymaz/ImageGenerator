from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

api_key = "YOUR API-KEY"
client = OpenAI(api_key=api_key)

user_prompt = input("Write your prompt here: ")

response = client.images.generate(
  model="dall-e-3",
  prompt=user_prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

try:
  image_data = response.data[0]
  image_url = image_data.url
except AttributeError:
  
  image_url = response.generated_images[0].url  


image_response = requests.get(image_url)
image = Image.open(BytesIO(image_response.content))

image.show()
