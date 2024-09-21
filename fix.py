import json

# Load your JSON data
with open("words_c1.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# Compress and preserve non-ASCII characters
compressed_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# Save it to a file
with open("words_c11.json", 'w', encoding='utf-8') as f:
    f.write(compressed_json)

print("JSON data compressed and saved successfully!")






