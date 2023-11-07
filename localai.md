# LocalAI
https://github.com/mudler/LocalAI

## Runpod
Template dev: https://github.com/fHachenberg/local-ai-ootb
Template: https://runpod.io/gsc?template=uv9mtqnrd0&ref=984wlcra

### Codebboga
MODEL_DOWNLOAD_CONFIG
```
{
    "models": [
        {
            "url": "https://huggingface.co/TheBloke/CodeBooga-34B-v0.1-GGUF/resolve/main/codebooga-34b-v0.1.Q5_K_M.gguf",
            "name": "CodeBooga-34B"
        }
    ],
    "templates": [
        {
            "name": "CodeBooga-34B",
            "content": "You are an experienced seinor developer. You anaylze before you start coding. You follow best practices and write code that is easy to maintain and easy to read and understand.\n### Instruction:\n{{.Input}}\n### Response:\n"
        }
    ]
}
```
MODEL_CONFIG
```
[
    {
        "name": "CodeBooga-34B",
        "parameters": {
            "model": "CodeBooga-34B"
        },
        "context_size": 16384,
        "threads": 18,
        "stopwords": [
            "HUMAN:",
            "### Response:"
        ],
        "roles": {
            "user": "HUMAN:",
            "system": "GPT:"
        },
        "template": {
            "completion": "completion",
            "chat": "ggml-gpt4all-j"
        }
    }
]
```