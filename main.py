from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI


def display_title_and_input():
    st.title("Ask any question!")
    return st.text_input("Got any questions for me?")


def initialize_openai_agent():
    llm = OpenAI(temperature=0.6)
    tool_names = ["serpapi"]
    tools = load_tools(tool_names)
    agent = initialize_agent(
        tools, llm, agent="zero-shot-react-description", verbose=True
    )
    return agent


def get_response(agent, prompt):
    if prompt:
        return agent.run(prompt)
    return None


def main():
    prompt = display_title_and_input()
    agent = initialize_openai_agent()
    response = get_response(agent, prompt)
    if response:
        st.write(response)


if __name__ == "__main__":
    current_directory = Path.cwd()
    env_file = current_directory / ".env"
    load_dotenv(env_file)
    main()
