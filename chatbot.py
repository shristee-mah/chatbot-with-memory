from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)
client=genai.Client(api_key=os.getenv("GEMAI_API_KEY"))

info_retrieval_function = {
    "type": "function",
    "name": "retrieve_info",
    "description": "Retrieves personal information of the user according to the user input like their name, location, hobbies, occupation, some personal events, health status, marital status,age, email,etc.This should in text format. Format example:- Name: name  Age: age_in_numbers  Location: location  pets: dog, cat",
    "parameters": {
        "type": "object",
        "properties": {
                "name": {"type": "string", "description": "User's name."},
                "address": {"type": "string", "description": "User's address."},
                "email": {"type": "string", "description": "User's email address."},
                "dog's name": {"type": "string", "description": "pet dog's name"},
                "cat's name": {"type": "string", "description": "pet cat's name"},
                "phone number": {"type": "integer", "description":"user's phone number"},
                "age": {"type":"integer", "description": "User's age"},
                "workplace": {"type":"string","description":"where the user works."}
        },
        "additionalInformation": True,
    }
}




def save_info_function(data):
    with open("user_info.txt", "a", encoding="UTF-8") as f:
        for key, value in data.items():
            if value:
                f.write(f"{key}: {value}\n")


args=[]

while True:
    prompt="You are an assistant for the user. You're basically storing their information in a file for that you have tool call option and always follow up to the user's question."
    user_input = input("User:")
    if user_input.lower() in ["q", "quit"]:
        print("Chatbot: Goodbye!")
        break
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=[
        {"type":"text","text": user_input},
        {"type":"text","text": prompt}
        ],
        tools=[{"type": "function", **info_retrieval_function}],
    )
    
    
    for step in interaction.steps:
        if step.type == "function_call":
            args.append(step.arguments)
            interaction = client.interactions.create(
                    model="gemini-3.1-flash-lite",
                    input=[
                    {"type":"text","text": user_input},
                    {"type":"text","text": "You are an efficient assistant."}
                    ],
                )
            
    print("Chat:", interaction.output_text)

for arg in args:
 save_info_function(arg)
    
