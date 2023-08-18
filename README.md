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
In the terminal, run the bash script: 
  
  `bash set_keys.sh` 

The `set_keys.sh` script will prompt you for your API keys (OpenAI & SerpAPI). 

The script then adds them to the `.env` file in the project directory. 

This way, you can avoid manually exporting the environment variables each time.

# Usage 
After the Export API Keys step is complete, you can run the `main.py` script: 
  
  `streamlit run main.py` 

