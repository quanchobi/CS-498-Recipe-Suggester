from src.detect_ingredients_pretrained import detect_ingredients
from src.api_call import prompt
from src.camera import take_photo
from os import environ, path
from dotenv import load_dotenv  # Used to access a users dotenv, in this case for an image path (defaults to ./images/default.png )

if __name__ == "__main__":
    # Get an image path from the user
    load_dotenv()

    # If the user defines a custom image location, we do not need to take a photo
    if "IMAGELOC" in environ:
        image_path: str = str(environ.get("IMAGELOC"))
    else:
        take_photo()
        image_path: str = "./images/default.png"

    # If file does not exist, exit gracefully.
    if not path.isfile(image_path):
        print(f"Ensure image exists at {image_path}")
        exit(1)

    # If file does exist, find a list of ingredients and then find a recipt
    ingredients: str = detect_ingredients(image_path)

    # Ask user for any additional input
    context: str = input("Any additional requirements for the recipe?")

    # Pass to chatGPT and print the results
    reply: str = prompt(ingredients, context)
    print(reply)
