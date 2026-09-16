import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "cards.json")

face_url = "https://raw.githubusercontent.com/CharaTBZ/Examples/refs/heads/main/exampleCardFront.png"
back_url = "https://raw.githubusercontent.com/CharaTBZ/Examples/refs/heads/main/exampleCardBack.jpg"

card_map = {}
for i in range(1, 1001):
    card_map[str(i)] = {
        "name": f"card{i}",
        "description": f"Card number {i}",
        "face": face_url,
        "back": back_url,
        "type": "0",
        "sideways": "false"
    }

data = {
    "Card": card_map
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Successfully generated cards.json at: {output_file}")