import json
import os

os.makedirs("output", exist_ok=True)

data = {
    "tables": [
        {"table_name": "users", "last_accessed": "2024-12-01", "up_for_delete": False},
        {"table_name": "orders", "last_accessed": "2024-11-10", "up_for_downgrade": True}
    ]
}

for env in ["dev", "stage", "prod"]:
    with open(f"output/{env}.json", "w") as f:
        json.dump(data, f, indent=2)
