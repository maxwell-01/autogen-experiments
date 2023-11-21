import autogen
from utils.get_autogen_config_list import get_autogen_config_list

config_list = get_autogen_config_list(
    filter_dict={
        "model": [
            "gpt-35-turbo-1106",  # azure OAI
            # "gpt-3.5-turbo-1106",# OAI
        ],
    },
)

code_execution_config = {
    "work_dir": "autogen-outputs/one-agent-team-output",
    "use_docker": False,
}

# Create AI coding agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list})

# Create an agent to speak with a human and execute code in a docker
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=code_execution_config,
    # is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith(
    #     "TERMINATE"),
    # human_input_mode="TERMINATE",
)

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA, AAPL and TESLA stock price change YTD.")
