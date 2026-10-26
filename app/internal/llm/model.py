import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

model = None

def init_model():
    """
    Initializes the model for the chain.
    """
    
    global model
    
    model = ChatOllama(
        model=os.environ.get("LOCAL_LLM_API_MODEL"),
        base_url=os.environ.get("LOCAL_LLM_API_URL"),
        validate_model_on_init=True,
        temperature=os.environ.get("LOCAL_LLM_API_TEMPERATURE")
    )
