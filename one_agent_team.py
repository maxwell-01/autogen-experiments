import autogen
from get_autogen_config_list import get_autogen_config_list

config_list = get_autogen_config_list(
    filter_dict={
        "model": [
            "gpt-35-turbo-1106", #azure OAI
            # "gpt-3.5-turbo-1106",# OAI
        ],
    },
)

# Create AI coding agent
assistant = autogen.AssistantAgent(name="assistant", llm_config={
    "config_list": config_list})

# Create an agent to speak with a human and execute code in a docker
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "_output", "use_docker": "faucet/python3"},
)

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA, AAPL and TESLA stock price change YTD.")
