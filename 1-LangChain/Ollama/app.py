import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LangSmith Tracing
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']=os.getenv("LANGCHAIN_PROJECT")

# Prompt Template
prompt=ChatPromptTemplate([
  ("system","You are a helpful assistan, Respond to the question asked"),
  ("user","Question:{question}")
])

#Streamlit framework
st.title("LangChain Demo with Gemma:2b Model")
input_text=st.text_input("What question you have in mind?")

# Ollama llama2 model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
  st.write(chain.invoke({"question":input_text}))