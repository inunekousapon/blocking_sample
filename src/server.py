from fastapi import FastAPI
import time
import random


app = FastAPI()


@app.get("/")
def read_root():
    wait = random.randint(1, 3)
    time.sleep(wait)
    return {f"wait time: {wait}sec"}
