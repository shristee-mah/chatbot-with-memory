## Chatbot with Personal Information Retrieval

A Simple Chatbot System that talks with the user, saves the users' chats in a file and retrieves the users' personal information and saves in another file.

# Files description:
1. requirements.txt: consists of the necessary dependencies.
2. .env: consists of Gemini API key.
3. chatbot.py: The chatbot function that uses function calling to retrieve the personal information when users provides any and saves the dats in user_info.txt at the end of the session when users type "q" or "quit".
6. .gitignore: Including .env containing the api keys and the txt files

# Future Improvements:
1. Avoid Duplicate data appending to the files
2. Session wise files generation 
3. Integration of the scripts and with frontend

