import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot"


# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])


def generate_response(question, api_key, llm, temperature, max_tokens):

    openai.api_key = api_key

    llm = ChatOpenAI(
        model=llm,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    answer = chain.invoke({'question': question})

    return answer


# Streamlit UI
st.title("Enhanced Q&A Chatbot With OpenAI")

st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

llm = st.sidebar.selectbox(
    "Select OpenAI model",
    ["gpt-4o", "gpt-4", "gpt-3.5-turbo"]
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)


# User input
st.write("Go ahead and ask any question")

user_input = st.text_input("You:")


if user_input:

    response = generate_response(
        user_input,
        api_key,
        llm,
        temperature,
        max_tokens
    )

    st.write("Answer:")
    st.write(response)

else:
    st.write("Please provide the user input")