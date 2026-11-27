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
                "previous_step": {"type": "STRING", "description": "Key findings and outcomes since the previous step."},
                "name": {"type": "string", "description": "User's name."},
                "address": {"type": "string", "description": "User's address."},
                "email": {"type": "string", "description": "User's email address."},
                "dog's name": {"type": "string", "description": "pet dog's name"},
                "cat's name": {"type": "string", "description": "pet cat's name"},
                "phone number": {"type": "array", "items": {"type": "number"}},
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
    user_input = input("User:")
    if user_input.lower() in ["q", "quit"]:
        print("Chatbot: Goodbye!")
        break
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=user_input,
        tools=[{"type": "function", **info_retrieval_function}],
    )

    print("Chat:", interaction.output_text)

    
    
    for step in interaction.steps:
        if step.type == "function_call":
            args.append(step.arguments)
            print (args)

for arg in args:
 save_info_function(arg)
    
