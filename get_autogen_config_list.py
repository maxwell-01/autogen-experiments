import os

import autogen.oai.openai_utils
from dotenv import load_dotenv


def get_autogen_config_list(filter_dict):
    load_dotenv()
    config_list = (
        [
            {
                "model": "gpt-3.5-turbo-1106",
                "api_key": os.getenv("OPENAI_API_KEY")
            },
            {
                "model": "gpt-4",
                "api_key": os.getenv("OPENAI_API_KEY")
            },
            {
                "model": "gpt-35-turbo-1106",
                "api_type": "azure",
                "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                "api_base": os.getenv("AZURE_OPENAI_API_BASE"),
                "api_version": "2023-09-01-preview"
            }
        ]
    )
    return autogen.oai.openai_utils.filter_config(config_list, filter_dict)
