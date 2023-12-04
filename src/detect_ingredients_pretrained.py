import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional
from PIL import Image

def detect_ingredients(image_path: str) -> str:
    """

    """
    # Using a pre-trained R-CNN model
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    # Loading the image
    image = Image.open(image_path)
    image_tensor = functional.to_tensor(image).unsqueeze(0)

    # Make the prediction
    with torch.no_grad():
        prediction = model(image_tensor)

    # Filter predictions with 50% confidence
    confidence_threshold = 0.5
    boxes = prediction[0]['boxes'][prediction[0]['scores'] > confidence_threshold]
    ingredients: str = ''
    for box in boxes:
        ingredients += str(box)

    return ingredients

