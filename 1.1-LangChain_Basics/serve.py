import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()
from langserve import add_routes

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="deepseek-r1-distill-llama-70b",groq_api_key=groq_api_key)

# Create Prompt template
system_template="Translate the following into {language}"
prompt_template=ChatPromptTemplate.from_messages([
  ("system",system_template),
  ("user","{text}")
])
# parser
parser=StrOutputParser()

# creating chain
chain=prompt_template|model|parser

# App definition
app=FastAPI(title="LangChain Server",
            version=1.0,
            description="Simple API server using LangChain Runnable Interfaces"
            )

# Adding chain routes
add_routes(
  app=app,
  runnable=chain,
  path="/chain"
)

if __name__=="__main__":
  import uvicorn
  uvicorn.run(app,host="127.0.0.1",port=8000)