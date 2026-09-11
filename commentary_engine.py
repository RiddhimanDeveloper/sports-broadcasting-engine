from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()

Template= ChatPromptTemplate([('System',"You are a legendary, energetic cricket commentator. "
        "Describe this event in a sentence or 2, "
        "using classic cricket terminology."),('user','{event_details}')])

commentary_chain = prompt | llm
