import os

def detect_disease(image_path):
    filename = os.path.basename(image_path).lower()

    if "yellow" in filename:
        return "Leaf Blight"
    elif "spot" in filename:
        return "Leaf Spot"
    else:
        return "Healthy"