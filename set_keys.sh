#!/bin/bash

# check if .env file exists
# if not, create it
if [ ! -f .env ]; then
  touch .env
fi

# Prompt for API keys
read -p "Enter OPENAI_API_KEY: " openai_key
read -p "Enter SERPAPI_API_KEY: " serpapi_key

# Write to .env file
echo "OPENAI_API_KEY=$openai_key" >> .env
echo "SERPAPI_API_KEY=$serpapi_key" >> .env

echo ".env file updated!"