from fastapi import FastAPI, File, UploadFile
from fastapi.param_functions import Body
from fastapi.params import File
from numpy import string_
from pydantic import BaseModel
from random import randint
from Word import Word
from Decode import To_phonemes
import Compare
import os

import requests
import shutil

app = FastAPI()

db = []

t_p = To_phonemes()

@app.get('/word')
def get_word():
    return db[randint(0, len(db))]

@app.post('/word')
def add_word(word: Word):
    db.append(word.dict())
    return db[-1]

@app.delete('/word/{word_id}')
def delete_word(word_id: int):
    db.pop(word_id - 1)
    return {}

@app.post('/audio')
def create_audio(word: str, file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    decoded_audio = ''.join(t_p.decode(file.filename).data)
    print(decoded_audio, word)
    os.remove(file.filename)
    return Compare.find_right_phonemes(decoded_audio, word)