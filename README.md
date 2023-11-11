# Recipe Suggester
Suggests recipes based on an ingredients list passed in

## DEPENDENCIES:
* Python3
* Python-dotenv
* OpenAI pip package

## HOW TO USE:
* Install python3 and pip
* clone the repository
* make the location where you cloned the repository a python3 venv
* install python-dotenv and openai with pip
* set your openAI API key in a .env file (create it if it doesn't exist)
* run using python3, then enter your ingredients list.

## TODO:
* pytorch image analysis to detect objects in a fridge/pantry, convert to text then add to the pr
* Parse the json output to only show GPT's response
* Stream the output, just like ChatGPT does
