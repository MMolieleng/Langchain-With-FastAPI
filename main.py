from fastapi import FastAPI
from llm import LLM

app = FastAPI()
llm = LLM()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/joke/{topic}")
async def joke(topic: str = 'dad'):
    return {"joke":llm.generate_joke(topic)}

@app.get("/test/{name}")
async def test(name: str):
    return {"message": "Welcome to "+ name}

@app.get("/chat/{message}")
async def chat(question: str):
    return {"response": llm.ask(question)}