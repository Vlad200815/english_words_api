
from fastapi import FastAPI
# from pydantic import BaseModel
import json
# from fastapi.responses import JSONResponse

app = FastAPI(title="Vlad'sCards")


@app.get("/")
def home():
    return {"instructions": "go to /words"}


@app.get("/a1_words")
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


@app.get("/a2_words")
def get_a1_words():
    try:
        with open('words_a2.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            print(words)
        return words
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("JSONDecodeError")


@app.get("/b1_words")
def get_a1_words():
    try:
        with open('words_b1.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            print(words)
        return words
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("JSONDecodeError")




@app.get("/b2_words")
def get_a1_words():
    try:
        with open('words_b2.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            print(words)
        return words
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("JSONDecodeError")




@app.get("/c1_words")
def get_a1_words():
    try:
        with open('words_c1.json', 'r', encoding='utf-8') as file:
            words = json.load(file)
            print(words)
        return words
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("JSONDecodeError")