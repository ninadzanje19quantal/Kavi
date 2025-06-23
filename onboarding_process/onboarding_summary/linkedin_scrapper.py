#libraries
from linkedin_api.linkedin import Linkedin
import os
from dotenv import load_dotenv

#files
from onboarding_process.onboarding_summary.chatbot import chatbot

load_dotenv()

email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

def convert_linkedin_url_to_id(url: str) -> str:
    if url.split("/")[-1] == "":
        linkedin_id = url.split("/")[-2]
    else:
        linkedin_id = url.split("/")[-1]
    return  linkedin_id


def linkedin_scrapper(user_email: str, user_password: str, profile_url: str) -> list | str:
    temp = []
    try:
        api = Linkedin(user_email, user_password)
    except:
        return "Incorrect Credentials"


    user_profile = convert_linkedin_url_to_id(profile_url)
    user_profile = user_profile.split(r"/")[-1]
    profile_data = api.get_profile(user_profile)
    profile_data = list(profile_data.items())

    if len(profile_data) == 0:
        return "Profile does not exist"

    prompt: str = ("Summarize the following information with particular focus on the"
                   "headline, about, skills, certifications, recommendations, activity and details of their latest job."
                   "If a particular data field does not exist then just ignore it.")

    profile_data = chatbot(prompt, profile_data)

    return profile_data

#print(linkedin_scrapper(email, password, "ninad-zanje"))