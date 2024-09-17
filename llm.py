import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}
Answer: Let's think step by step."""

class LLM:
    def __init__(self, model_name="phi3:mini", chain=None):
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model=model_name, verbose=False)
        self.chain = self.prompt | self.model

    def ask(self, question):
        return self.chain.invoke({"question": question})
    
    def generate_joke(self, topic):
        return self.ask(f"Tell me a joke about {topic}")