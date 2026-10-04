import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool

load_dotenv()

def call_simple_agent():
    llm = ChatOpenAI(
        model="meta-llama/Llama-3.1-8B-Instruct",  # use the same model that worked in Postman
        base_url="https://router.huggingface.co/v1",
        api_key=os.environ["HF_TOKEN"],
        temperature=0,
        max_tokens=500,
    )
    print(llm.invoke("What is the capital of France?").content)

# Define tools at module level
@tool
def ask_llm(question: str) -> str:
    """Ask the LLM a question and get an answer."""
    llm = ChatOpenAI(
        model="meta-llama/Llama-3.1-8B-Instruct",
        base_url="https://router.huggingface.co/v1",
        api_key=os.environ["HF_TOKEN"],
        temperature=0,
    )
    response = llm.invoke(question)
    return response.content

@tool
def get_capital(country: str) -> str:
    """Get the capital city of a country."""
    llm = ChatOpenAI(
        model="meta-llama/Llama-3.1-8B-Instruct",
        base_url="https://router.huggingface.co/v1",
        api_key=os.environ["HF_TOKEN"],
        temperature=0,
    )
    response = llm.invoke(f"What is the capital of {country}?")
    return response.content

def using_agent(country: str = "France"):
    # Directly use the tools without an agent for simplicity
    print(f"\nGetting information about {country}...")
    
    # Use the get_capital tool
    capital = get_capital.invoke({"country": country})
    print(f"Capital: {capital}")
    
    # Use the ask_llm tool for more info
    info = ask_llm.invoke({"question": f"Tell me something interesting about {country}"})
    print(f"Additional info: {info}")



if __name__ == '__main__':
    # call_simple_agent()
    using_agent("India")
