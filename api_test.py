from subprocess import PIPE, run
import openai

# Returns the output of a command.
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

api_cmd = "pass show ChatGPT/API-KEY"   # uses password-store to securely import OpenAI API key

# JSON to pass to chatGPT
template = [ { "role": "chef",
               "content": "You are a chef, suggest me a recipe with the following ingredients: " } ]
# ingredients list to append to the template and pass to chatGPT
ingredients = input("User : ")
if ingredients:
    template.append(
        { "role": "user",
          "content": ingredients}
    )
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages = template
    )
    reply = chat.choices[0].message.content
    printf(reply)
