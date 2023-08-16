# InternetGPT
A simple Streamlit application where users can input any question and get answers using Lanchain and OpenAI. 
If you use ChatGPT, you know that a current limitation is that it's not trained on any information after 2021. 

This app allows you to ask any question via the Streamlit UI. 
SerpAPI is leveraged to allow ChatGPT to access updated internet information after 2021.

# Features
* Interactive Question Interface
* Langchain Integration
* OpenAI Integration
* Internet Access for ChatGPT

# Prerequisites
* Python 3.6 or above
* Poetry 
* Streamlit
* OpenAI API Key
* SerpAPI Api Key

# Installation
Install Poetry:

`curl -sSL https://install.python-poetry.org | python3 -` 

Clone the repository:
  
  `git clone https://github.com/rojerdu-dev/InternetGPT.git`
  
  `cd InternetGPT`

Install Dependencies:
 
  `poetry install`

# Export API Keys
In the terminal, use the `export` command to set your OpenAI and SerpAPI api keys as environment variables:
  `export OpenAI_API_KEY=YOUR_API_KEY_HERE`
  
  `export SERPAPI_API_KEY=YOUR_API_KEY_HERE`

Run Script:
  
  `poetry run python3 main.py`
