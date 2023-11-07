import openai 

openai.api_key = "any-string-here"
openai.api_base = "http://localhost:8000" # your proxy url

# call gpt-3.5-turbo
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hey"}])

print(response)

# call ollama/llama2
response = openai.ChatCompletion.create(model="ollama/llama2", messages=[{"role": "user", "content": "Hey"}])

print(response)