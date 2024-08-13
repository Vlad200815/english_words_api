
from fastapi import FastAPI
# from pydantic import BaseModel
import json
# from fastapi.responses import JSONResponse

app = FastAPI(title="Vlad'sCards")


@app.get("/")
def home():
    return {"instructions": "go to /words"}


@app.get("/words")
def get_a1_words():
    try:
        with open('words_a1.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            print(words)
        return words
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("JSONDecodeError")













