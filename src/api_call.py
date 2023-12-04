"""
api_call.py
Authors: Hanks, Jacob and Zhang, Shen
Date: Nov 20, 2023
Purpose: Functions to prompt chatGPT with given ingredients and context.
Methods:
    out()           Gets output from a specified shell command
    get_key()       Gets an API key from the users environment
    prompt() Prompts chatGPT using the found API key and ingredients list
"""
from subprocess import PIPE, run    # To run a command to print the API key to stdout, instead of storing in plain text in .env
from openai import OpenAI           # OpenAI integration
from os import environ              # To read environment variables
from dotenv import load_dotenv      # Loads environment variables

def out(command: str) -> str:
    """
    out:            Returns the output of a shell command.
    Arguments:      Takes in a command string as argument. This is the command that will be run by the program
    Preconditions:  Assumes that the command is valid UNIX command. does not check to see if it is.
    Postconditions: Returns the output of the command input.
    Notes:          Untested in any non UNIX shell. Use in Powershell at your own risk.
    """
    if command:
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        return result.stdout
    else:
        return ""



def get_key() -> str:
    """
    get_key:        Finds an API key from one of the three following places:
                        First, it checks to see if the API_KEY is set as an environment variable. If it is, then it returns the key found there.
                        Second, if the first check fails, it checks to see if a command is set to print the API key to stdout. For someone using
                            a CLI password manager like password-store or lastpass, that might be something like `pass show openai/api_key`. It then
                            returns the string found from the output of this command.
                        Third, if both of the above fail, it asks the user to input their API key at runtime.
    Arguments:      None
    Preconditions:  Assumes one of the three methods listed above is used to pass in the API key.
    Postconditions: Returns the api key string that was found. Assumes it is valid, does not do error checking.
    """
    load_dotenv() # Loads .env file from
    # If API_KEY env var is passed in, prioritize that.
    if "OPENAI_API_KEY" in environ:
        api_key = environ.get("OPENAI_API_KEY")
    # Else, if the user wants to pass in a command to show the key, use that instead.
    elif "OPENAI_API_CMD" in environ:
        api_key = out(str(environ.get("OPENAI_API_CMD")))
    # Otherwise, ask the user for the api key.
    else:
        api_key = input("What is your OpenAI API key? (Ctrl+c to quit)")
    return str(api_key)



def prompt(ingredients: str, context: str) -> str:
    """
    prompt_recipe:  Prompts OpenAI's chatGPT for a recipe suggestion with the passed in ingredients and added context
    Arguments:      Takes two strings. As the name implies, the ingredients string takes a list of ingredients found earlier by the image analysis part of the program.
                        The context string is optional, and contains any additional information the user wants to pass into the prompt for chatGPT. For example,
                        the context string can specify the type of food the user wants. If they want Asian food, then the user passes in "The recipe must be Asian cuisine.",
                        or any other conditions they want chatGPT to know.
    Preconditions:  Presupposes that ingredients is not empty. Errors out if it is.
    Postconditions: Prints the string returned by chatGPT to stdout.
    """

    print(ingredients)
    # If no ingredients were found, error
    if not ingredients:
        return "Error"

    # Find the API key from the options above
    key = get_key()

    # Define OpenAI client with our api key
    client = OpenAI(
        api_key = key,
    )

    # Create the JSON template to pass to chatGPT
    # If additional user context is defined, append that to the message send to chat gpt
    if context:
        context = "With the following conditions: " + context

    # ChatGPT completion
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            { "role": "assistant", "content": "You are a chef." },
            { "role": "user", "content": "Suggest me a recipe with the following ingredients:" + ingredients + context }
        ],
    )


    return str(completion.choices[0].message.content)
