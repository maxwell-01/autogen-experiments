import autogen
from utils.get_LLM_configs import get_autogen_config_list

llm_config = {
    "seed": 42,
    "timeout": 60,
    "config_list": (get_autogen_config_list(
        filter_dict={
            "model": [
                "gpt-35-turbo-1106",
            ],
        },
    )),
    "temperature": 0,
}

code_execution_config = {
    "work_dir": "../autogen-outputs/one-agent-team-output",
    "use_docker": False,
}

# Create AI coding agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

# Create an agent to speak with a human and execute code in a docker
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=code_execution_config,
)

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA, AAPL and TSLA stock price change YTD.")
