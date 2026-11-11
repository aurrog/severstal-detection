import random

def check_defect_stub(image_path: str) -> dict:
    has_defect = random.choice([True, False])
    confidence = round(random.uniform(0.75, 0.99), 2)
    return {
        "has_defect": has_defect,
        "confidence": confidence
    }