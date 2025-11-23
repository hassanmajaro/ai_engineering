from google import genai 
from dotenv import load_dotenv 
import os 

load_dotenv()

api_key = os.getenv("gemini_api_key")

client = genai.Client(api_key = api_key)

# building persona
persona = """
        You are Sentinel, a professional cybersecurity analyst.
        Your job is to explain security concepts clearly, focus on defensive practices,
        and never provide harmful or illegal instructions.
        Your tone is clam, technical, and accurate.
        You help users understand risks, secure systems, and follow best practices, and sometimes cheeky (maybe).
"""

while True:
    user_input = input("User: ")

    if user_input.capitalize() == "quit":
        break

    prompt = f"{persona}\nUser: {user_input}\nSecurity Bot:"

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    print(f"\nAgent: {response.text} \n")