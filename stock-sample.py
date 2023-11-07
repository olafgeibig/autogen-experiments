# litellm --model ollama/mistral:7b-instruct --api_base http://localhost:11434/
# litellm --model ollama/zephyr:7b-alpha-q5_K_M --api_base http://localhost:11434/

from autogen import AssistantAgent, UserProxyAgent, oai
import openai
import autogen

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "model": ["codebooga-runpod"],
    },
)

llm_config = {
    "seed": 42,  # change the seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "request_timeout": 600,
    "use_cache": True,
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"}, )

user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# user_proxy.initiate_chat(assistant, message="Research the web who is Olaf Geibig and what is his expertise")