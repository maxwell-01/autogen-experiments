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

llm_config_gpt4 = {
    "seed": 42,
    "timeout": 60,
    "config_list": (get_autogen_config_list(
        filter_dict={
            "model": [
                "gpt-4-azure",
            ],
        },
    )),
    "temperature": 0,
}

code_execution_config = {
    "last_n_messages": 10,
    "work_dir": "autogen-outputs/coding-team-output",
    "use_docker": False,
}

user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin. Save the coding file.",
   code_execution_config=False,
)
engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config_gpt3,
)

planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.
The plan may involve an engineer who can write code and a scientist who doesn't write code.
Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
''',
    llm_config=llm_config_gpt3,
)
executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="Executor. Execute the code written by the engineer then save the file and report the result.",
    human_input_mode="NEVER",
    code_execution_config=code_execution_config,
)
critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback.",
    llm_config=llm_config_gpt3,
)
groupchat = autogen.GroupChat(agents=[user_proxy, engineer, executor, planner, critic], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_gpt4)

def ask_coding_team(message):
    user_proxy.initiate_chat(
        manager,
        message=message,
    )
    return user_proxy.last_message()["content"]