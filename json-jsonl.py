import json

# Input and output file names
input_file = "athichoodi_modified.json"  # Replace with your JSON file
output_file = "athichoodi_modified.jsonl"

# Load JSON data
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Write to JSONL format
with open(output_file, "w", encoding="utf-8") as f_out:
    # If the JSON is a list of objects
    if isinstance(data, list):
        for entry in data:
            f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
    # If the JSON is a dictionary with lists inside
    elif isinstance(data, dict):
        for key, value in data.items():
            f_out.write(json.dumps({key: value}, ensure_ascii=False) + "\n")

print(f"Converted {input_file} to {output_file}")
