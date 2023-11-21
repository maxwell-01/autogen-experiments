import autogen

from utils.get_autogen_config_list import get_autogen_config_list

config_list = get_autogen_config_list(
    filter_dict={
        "model": [
            "gpt-35-turbo-1106", #azure OAI
            # "gpt-3.5-turbo-1106",# OAI
        ],
    },
)

llm_config = {
    "seed": 42,
    "timeout": 60,
    "config_list": config_list,
    "temperature": 0,
}

code_execution_config = {
    "work_dir": "autogen-outputs/coding-team-output",
    "use_docker": "python:3",
}

product_manager = autogen.AssistantAgent(
    name="product_manager",
    system_message="You will help break down the initial idea into a well scoped requirement for the software_developer; Do not involve in future conversations or error fixing. Reply 'TERMINATE' when you are happy that the software meets the requirements.",
    llm_config=llm_config,
)
software_developer = autogen.AssistantAgent(
    name="software_developer",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=code_execution_config,
    is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith(
        "TERMINATE"),
    human_input_mode="TERMINATE",
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, product_manager, software_developer], messages=[])

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
    system_message="Group chat manager. Use the product_manager to create the requirements and pass these to the software_developer. Finish your message with TERMINATE when you would like user input."
)


def ask_coding_team(message):
    user_proxy.initiate_chat(
        manager,
        message=message,
    )
    return user_proxy.last_message()["content"]
