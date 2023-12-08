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
                # "api_base": os.getenv("AZURE_OPENAI_API_BASE"),
                "base_url": os.getenv("AZURE_OPENAI_API_BASE"),
                "api_version": os.getenv("AZURE_OPENAI_VERSION")
            },
            {
                "model": "gpt-4-azure",
                "api_type": "azure",
                "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                "base_url": os.getenv("AZURE_OPENAI_API_BASE"),
                "api_version": os.getenv("AZURE_OPENAI_VERSION")
            }
        ]
    )
    return autogen.oai.openai_utils.filter_config(config_list, filter_dict)


def get_langchain_config():
    load_dotenv()

    azure_llm = {
        "deployment_name": "gpt-4-azure",
        "model_version": "1106",
        "openai_api_type": "azure",
        "openai_api_base": os.getenv("AZURE_OPENAI_API_BASE"),
        "openai_api_version": os.getenv("AZURE_OPENAI_VERSION"),
        "openai_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    }

    return azure_llm

def get_memgpt_config():
    load_dotenv()
    config_list_memgpt = [
        {
            "preset": None,
            "model": "gpt-35-turbo-1106",
            "model_wrapper": None,
            "context_window": 8000,
            "model_endpoint_type": "azure",
            "azure_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "azure_endpoint": os.getenv("AZURE_OPENAI_API_BASE"),
            "azure_version": os.getenv("AZURE_OPENAI_VERSION"),
            "embedding_endpoint_type": "azure",
            "embedding_endpoint": os.getenv("AZURE_OPENAI_API_BASE"),
        },
    ]
    return config_list_memgpt