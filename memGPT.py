﻿import autogen
import memgpt.autogen.interface as autogen_interface
import memgpt.autogen.memgpt_agent as memgpt_autogen
import memgpt.presets as presets
from memgpt.persistence_manager import InMemoryStateManager

from get_autogen_config_list import get_autogen_config_list

config_list = get_autogen_config_list(
    filter_dict={
        "model": ["gpt-3.5-turbo-1106"],
    },
)

llm_config = {"config_list": config_list, "seed": 42}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
)

persona = "I\'m a 10x engineer at a FAANG tech company."
human = "I\'m a team manager at a FAANG tech company."
interface = autogen_interface.AutoGenInterface() # how MemGPT talks to AutoGen
persistence_manager = InMemoryStateManager()
memgpt_agent = presets.use_preset(presets.DEFAULT, 'gpt-3.5-turbo-1106', persona, human, interface, persistence_manager)

# MemGPT coder
coder = memgpt_autogen.MemGPTAgent(
    name="MemGPT_coder",
    agent=memgpt_agent,
)

# non-MemGPT PM
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="First send the message 'Let's go Mario!'")