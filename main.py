import dotenv
import os
import openai


# load the environment variables
dotenv.load_dotenv()

openai.organization = os.getenv("OPENAY_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# display which models are available to use
# print(openai.Engine.list())

prompt = ""
while(prompt!="exit"):
    # ask user for input
    prompt = input("What do you want to ask from GPT? (type 'exit' to exit): ")

    # create a chat completion
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    # print the chat completion
    print(chat_completion.choices[0].message.content)
