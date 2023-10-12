# litellm --model ollama/mistral:7b-instruct --api_base http://localhost:11434/

from autogen import AssistantAgent, UserProxyAgent, oai
config_list=[
    {
        "model": "my-fake-model",
        "api_base": "http://localhost:8000/v1/",  #litellm compatible endpoint
        "api_type": "open_ai",
        "api_key": "NULL", # just a placeholder
    }
]

response = oai.Completion.create(config_list=config_list, prompt="Hi")
print(response) # works fine

assistant = AssistantAgent("assistant")
user_proxy = UserProxyAgent("user_proxy")
user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change YTD.", config_list=config_list)
