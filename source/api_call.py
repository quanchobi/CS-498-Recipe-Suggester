from subprocess import PIPE, run    # To run a command to print the API key to stdout, instead of storing in plain text in .env
from openai import OpenAI           # OpenAI integration
from os import environ              # To read environment variables
from dotenv import load_dotenv      # Loads environment variables

# Returns the output of a command. If api_cmd is defined, this will run that command to get the api key.
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Main function
if __name__ == "__main__":
    load_dotenv() # Loads .env file from
    # If API_KEY env var is passed in, prioritize that.
    if "OPENAI_API_KEY" in environ:
        key = environ.get("OPENAI_API_KEY")
    # Else, if the user wants to pass in a command to show the key, use that instead.
    elif "OPENAI_API_CMD" in environ:
        key = out(environ.get("OPENAI_API_CMD"))
    # Otherwise, ask the user for the api key.
    else:
        key = input("What is your OpenAI API key? (Ctrl+d to quit)")

    # Define OpenAI client with our api key
    client = OpenAI(
        api_key = key,
    )


    # JSON to pass to chatGPT

    # ingredients list to append to the template and pass to chatGPT
    ingredients = input("User : ")

    # ChatGPT completion
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            { "role": "assistant", "content": "You are a chef" },
            { "role": "user", "content": "Suggest me a recipe with the following ingredients:" + ingredients }
        ],
    )

    print(completion.choices[0].message)
