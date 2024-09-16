from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


app = FastAPI()

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="phi3:mini", verbose=True)
chain = prompt | model

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{name}")
async def test(name: str):
    return {"message": "Welcome to "+ name}

@app.get("/chat/{message}")
async def chat(message: str):
    return {"response": chain.invoke({"question": message})}