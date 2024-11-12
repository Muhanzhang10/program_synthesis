import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import Optional
from pydantic import BaseModel, Field



class Code(BaseModel):
   code: str = Field(..., explanation="The python code")
   explanation: str = Field(..., explanation="The none python code part")


class LLM:
    def __init__(self, model="mixtral-8x7b-32768"):
        self.groq_client = ChatGroq(model=model, temperature=0)
        self.openai_client = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    def run(self, content, structure):
        try:
            response = self.groq_client.invoke(content)
            structured_llm = self.openai_client.with_structured_output(structure)
            output = structured_llm.invoke(self.extract_prompt(response.content))
            return output 
        except Exception as e:
            print(f"Error during API call: {e}")
            return None
        
        
    def extract_prompt(self, python_code):
        return f"""
            You are an expert extraction algorithm.
            Extract the python code: {python_code}
        """