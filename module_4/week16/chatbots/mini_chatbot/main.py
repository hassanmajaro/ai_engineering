from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("gemini_api_key")

client = genai.Client(api_key = api_key)

while True:
    user_input = input("User: ")

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user_input,
    )

    print(response.text)