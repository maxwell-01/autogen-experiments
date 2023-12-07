# autogen-experiments

## Setup
Install dependencies:
1. pip install pyautogen
2. pip install docker

Create your environment variables
1. create a .env file in the root of the project
2. add your api keys and urls eg:
```
OPENAI_API_KEY=sk-api_key_here
AZURE_OPENAI_API_KEY=api_key_here
AZURE_OPENAI_API_BASE=azure_api_base_url_here
AZURE_OPENAI_VERSION="..."
```

You can add additional models to get_autogen_config_list.py, be sure to add any additional api keys or urls to 
your `.env` file.





