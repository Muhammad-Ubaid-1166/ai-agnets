import os
import asyncio
import pyttsx3  # text to speech
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL = 'gemini/gemini-2.0-flash'
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize agent
agent = Agent(
    name="get news agent for user",
    instructions="You are a local news reporter which tells the news in easy English.",
    model=LitellmModel(model=MODEL, api_key=gemini_api_key),
)

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)      # Speed %
    engine.setProperty('volume', 1.0)    # Volume 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

# Async runner
async def main():
    result = await Runner.run(agent, "news about most important global news in easy English wording")
    print(result.final_output)
    speak(result.final_output)

# Run the async function
asyncio.run(main())

