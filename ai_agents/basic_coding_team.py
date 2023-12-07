import autogen

from utils.get_LLM_configs import get_autogen_config_list

llm_config_gpt3 = {
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
    "work_dir": "autogen-outputs/basic-coding-team-output",
    "use_docker": False,
}

pm_system_message = "You will help break down the initial idea into a well scoped requirement for the software_developer; Do not involve in future conversations or error fixing. Reply 'TERMINATE' when you are happy that the software meets the requirements."

product_manager = autogen.AssistantAgent(
    name="product_manager",
    system_message=pm_system_message,
    llm_config=llm_config_gpt3,
)
software_developer = autogen.AssistantAgent(
    name="software_developer",
    llm_config=llm_config_gpt3,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=code_execution_config,
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, product_manager, software_developer], messages=[])

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config_gpt3,
    system_message="Group chat manager. Use the product_manager to create the requirements and pass these to the software_developer. Finish your message with TERMINATE when you would like user input."
)


def ask_basic_coding_team(message):
    user_proxy.initiate_chat(
        manager,
        message=message,
    )
    return user_proxy.last_message()["content"]
