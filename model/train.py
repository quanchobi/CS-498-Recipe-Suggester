from tqdm import main
from ultralytics import YOLO

def train():
    # Load the model
    model = YOLO("yolov8n.pt")  # Base on official model
    model.train(data="./dataset/data.yaml", epochs = 100) # Train the model with given data

    # Export the model
    model.export()

if __name__ == "__main__":
    train()
