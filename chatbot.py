from google import genai
from dotenv import load_dotenv
import os

load_dotenv(override=True)
client=genai.Client(api_key=os.getenv("GENAI_API_KEY"))
    

while True:
    user_input= input("User:")

    interaction = client.interactions.create(
         model="gemma-4-26b-a4b-it",
         input = user_input
    )

    print('Chat:',interaction.output_text)

    with open("chat_history.txt","a", encoding="utf-8") as file:
            file.write(f"{user_input}\n")