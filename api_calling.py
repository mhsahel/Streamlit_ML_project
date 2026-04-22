from google import genai
from  dotenv import load_dotenv
import os
load_dotenv()
 
API_key =os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= API_key)
def note_generator(images):
    prompt = "Identify the image and describe with your own ways and make notes."
   
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=[images , prompt]
)
    return response.text
    
def quize_generator(images , info):
    prompt = f"Generate 25 quizzes based on {info} with answers"
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=[images , prompt]
)
    return response.text
    

