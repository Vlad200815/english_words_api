import json

# Load your JSON data
with open("words_a1.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

for word in data['words']:
    word["repetition"] = 0

# Compress and preserve non-ASCII characters
compressed_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# Save it to a file
with open("words_a11.json", 'w', encoding='utf-8') as f:
    f.write(compressed_json)

print("JSON data compressed and saved successfully!")






