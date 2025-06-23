#libraries
from google import genai
from  dotenv import load_dotenv
import os

#python scripts
#from linkedin_scrapper import *
#from cv_scrapper import *

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

#cv_path = r"CV's/Ninad AIML.pdf" #put your cv path here
#profile = "ninad-zanje" #put your public profile id here

"""def summarise_linkedin_and_cv(cv: str, linkedin_id: str) -> str:
    prompt = f"Summarise the following data from a CV {extract_text_from_cv(cv)} and from the Linkedin account {linkedin_scrapper(user_email=email, user_password=password, profile_url=linkedin_id)}"
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text
"""
#print(summarise_linkedin_and_cv(cv_path, profile))

def chatbot(prompt: str, data: list | str = "") -> str:
    prompt = f"{prompt} {data}"

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text
