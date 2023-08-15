import streamlit as st
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

st.title("Ask any question!")
prompt = st.text_input("Got any questions for me?")

llm = OpenAI(temperature=0.6)

tool_names = ["serpapi"]
tools = load_tools(tool_names)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

if prompt:
    response = agent.run(prompt)
    st.write(response)
