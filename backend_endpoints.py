#libraries
import io
from fastapi import FastAPI, Query, UploadFile, File, HTTPException
import uvicorn
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from pymupdf import pymupdf

#python scripts
from onboarding_process.onboarding_summary.chatbot import chatbot
from onboarding_process.onboarding_summary.cv_scrapper import extract_text_from_cv
from onboarding_process.onboarding_summary.linkedin_scrapper import linkedin_scrapper


load_dotenv()
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")
kavi = FastAPI()


class LinkedInRequest(BaseModel):
    user_email: str = os.getenv("LINKEDIN_EMAIL")
    user_password: str = os.getenv("LINKEDIN_PASSWORD")
    profile_url: str

class chatbot_prompt(BaseModel):
    prompt: str
    data: str | tuple | list


@kavi.get("/")
async def home():
    return {"Hello": "World"}

@kavi.get("/linkedin_summary")
async def linkedin_summary(linkedin_url: str = Query(title="Linkedin URL",
                                                     description="Enter the URL of your Linkedin homepage",
                                                     min_length=5, max_length=1000)):
    linkedin_data = linkedin_scrapper(user_email=email, user_password=password, profile_url=linkedin_url)
    return {"linkedin_data": linkedin_data}


@kavi.post("/linkedin-scraper/")
async def linkedin_scraper_endpoint(request: LinkedInRequest):
    result = linkedin_scrapper(
        user_email=request.user_email,
        user_password=request.user_password,
        profile_url=request.profile_url
    )

    return result

@kavi.post("/read-CV")
async def readCV(cv: UploadFile = File(...)) -> str:
    cv_data = extract_text_from_cv(cv)
    return cv_data



@kavi.post("/chatbot")
async def chat_bot(final_prompt : chatbot_prompt) -> str:
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.post("/chatbot/welcome")
async def chat_bot_welcome(final_prompt : chatbot_prompt) -> str:
    final_prompt.prompt = "Welcome the user in 2 sentences on our platform"
    final_prompt.data = ""
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.post("/chatbot/current-work")
async def chat_bot_current_work(final_prompt : chatbot_prompt) -> str:
    #What is your current work
    final_prompt.prompt = ("Using the following text as a context ask a question in one sentence"
                           "Let’s start with your work — just so I get a sense of the world you operate in."
                           "What’s your current role, and how long have you been doing it?"
                           "If it’s easier, feel free to link your LinkedIn or drop a resume — totally up to you."
                           )
    final_prompt.data = ""
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.post("/chatbot/reason-interview")
async def chat_bot_current_work(final_prompt : chatbot_prompt) -> str:
    #What is the reason you are giving the interview
    final_prompt.prompt = ("Using the following text as a context ask a question in one sentence"
                           "What’s got you preparing for interviews right now?"
                           "You don’t need a perfect answer — just what’s true for you."
                           "Some folks are job hunting after a layoff. Others are aiming for a big move — a promotion, a better offer, a dream company. "
                           "And some just want to get better at telling their story. Which of those feels most like your situation?"
                            )
    final_prompt.data = ""
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.post("/chatbot/interview-process")
async def chat_bot_current_work(final_prompt : chatbot_prompt) -> str:
    #Where are you in the interview process
    final_prompt.prompt = ("Using the following text as a context ask a question in one sentence"
                           "Just so I know how fast to go — where are you in your interview process?"
                           "Still early? Already in the loop? Just sharpening up?"
                           "No pressure either way. This just helps me meet you where you are."
                           )
    final_prompt.data = ""
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.post("/chatbot/target-company")
async def chat_bot_current_work(final_prompt : chatbot_prompt) -> str:
    #Any specific company you are targeting
    final_prompt.prompt = ("Using the following text as a context ask a question in one sentence"
                           "Any particular role or company you’ve got your eye on?"
                           "You can type something like “PM at Google” or “Marketing lead at a Series A startup.”"
                           "Or upload a job description if you’ve got one handy."
                           "And if you're still figuring it out, that’s totally fine — we can start general and narrow in as you go."
                           )
    final_prompt.data = ""
    response = chatbot(final_prompt.prompt, final_prompt.data)
    return response

@kavi.get("/get-data")
def get_data(user_json) -> dict:
    user_data: dict = user_json

    return user_data

