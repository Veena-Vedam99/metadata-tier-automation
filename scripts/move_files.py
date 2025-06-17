import os
import shutil

# Ensure metadata directory exists
os.makedirs("metadata", exist_ok=True)

# Move all JSON files from output to metadata
for filename in os.listdir("output"):
    if filename.endswith(".json"):
        shutil.copy2(os.path.join("output", filename), os.path.join("metadata", filename))

print(" Moved all JSON files to metadata/")
