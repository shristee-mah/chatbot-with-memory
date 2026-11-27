from google import genai
from dotenv import load_dotenv
import os

load_dotenv(override=True)
client=genai.Client(api_key=os.getenv("GEMAI_API_KEY"))

with open("chat_history.txt","r", encoding="UTF-8") as f:
    file_content=f.read()

prompt="You are an efficient personal information retrieval. You take the input given by the user in a chat session, retrieves the personal information of the user like their name, location, hobbies, occupation, some personal events, health status, marital status, age, email, family background,etc. from the data you get through the chat. You cannot assume or overexagerate the information and do not add the questions they asked, and give the output as text"

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=[
        {"type":"text","text": file_content},
        {"type":"text","text": prompt}
    ]
)

print(interaction.output_text)


with open(f"user_info.txt","a", encoding="UTF-8") as file:
    file.write(f"{interaction.output_text}\n")


