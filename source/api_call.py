from subprocess import PIPE, run
from openai import OpenAI
from os import getenv

# Returns the output of a command. If api_cmd is defined, this will run that command to get the api key.
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Main function
if __name__ == "__main__":
    # If API_KEY env var is passed in, prioritize that.
    if getenv("OPENAI_APIKEY"):
        api_key = getenv("OPENAI_API_KEY")
    # Else, if the user wants to pass in a command to show the key, use that instead.
    elif getenv("OPENAI_APICMD"):
        api_key = out(getenv("OPENAI_API_CMD"))
    # Otherwise, ask the user for the api key.
    else:
        api_key = input("What is your OpenAI API key? (Ctrl+d to quit)")


    # JSON to pass to chatGPT
    template =
        { "role": "chef", "content": "You are a chef, suggest me a recipe with the following ingredients: " }

    # ingredients list to append to the template and pass to chatGPT
    ingredients = input("User : ")

    # ChatGPT completion
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages = [
            template,
            { "role": "user", "content": ingredients }
        ]
    )
