import autogen
from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
from utils.get_LLM_configs import get_autogen_config_list, get_memgpt_config


directory_to_load = 'example-data'
mem_gpt_store_name = "ghyston_docs"
# Set to True if you want to print MemGPT's inner workings.
DEBUG = True

config_list = get_autogen_config_list(
    filter_dict={
        "model": [
            "gpt-35-turbo-1106",
        ],
    },
)

interface_kwargs = {
    "debug": DEBUG,
    "show_inner_thoughts": DEBUG,
    "show_function_outputs": DEBUG,
}

llm_config = {"config_list": config_list, "seed": 42}
llm_config_memgpt = {"config_list": get_memgpt_config(), "seed": 42}

# The user agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    llm_config=llm_config,
    human_input_mode="ALWAYS",
    default_auto_reply="Reply terminate when finished",  # Set a default auto-reply message here (non-empty auto-reply is required for LM Studio)
)

memgpt_agent = create_memgpt_autogen_agent_from_config(
    "MemGPT_agent",
    llm_config=llm_config_memgpt,
    system_message=f"Load data from your archive and answer questions about Ghyston, a technology company in Bristol. I am a 10x researcher who checks the memory and answers careful methodically explaining your reasoning. You are participating in a group chat with a user ({user_proxy.name}).",
    interface_kwargs=interface_kwargs,
    # default_auto_reply="Please summarise",  # Set a default auto-reply message here (non-empty auto-reply is required for LM Studio)
)
# load new files to a store name or attach that store name
# memgpt_agent.load_and_attach(mem_gpt_store_name, "directory", force=True, input_dir=directory_to_load, recursive=True)
# memgpt_agent.attach(mem_gpt_store_name)

def ask_memgpt_agent(message):
    user_proxy.initiate_chat(
        memgpt_agent,
        message=message,
    )
    return user_proxy.last_message()["content"]


ask_memgpt_agent("How are holidays calculated for part-time employees at Ghyston, load data from your archive.")
