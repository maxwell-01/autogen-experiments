import os

from dotenv import load_dotenv


def configure_memgpt():
    # Run this and then paste the contents of the created file into powershell
    load_dotenv()
    env_vars = {
        "AZURE_OPENAI_KEY": os.getenv("AZURE_OPENAI_API_KEY"),
        "AZURE_OPENAI_API_KEY": os.getenv("AZURE_OPENAI_API_KEY"),
        "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_API_BASE"),
        "AZURE_OPENAI_VERSION": os.getenv("AZURE_OPENAI_VERSION"),
        # text embeddings
        "AZURE_OPENAI_DEPLOYMENT": "gpt-35-turbo-1106",
        "AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT": "text-embedding",
    }

    # Generate PowerShell commands to set the environment variables
    commands = [f'$Env:{key} = "{value}"' for key, value in env_vars.items()]

    # Add the 'memgpt configure' command
    commands.append('memgpt configure')

    # Write the commands to a PowerShell script file
    with open('configure-memgpt.ps1', 'w') as f:
        f.write('\n'.join(commands))


configure_memgpt()
