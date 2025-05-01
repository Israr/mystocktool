# mystocktool

A basic tool to analyzing Stocks sentiment with Azure OpenAI

# Setup

Before you can use the tool, you need to prvide your API keys and endpoints for your deployment.

```
OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
AZURE_CHAT_MODEL=<your_azure_deployment_name>
MISTRAL_API_KEY=<your_mistral_api_key>
# to use mistral, set the model to mistral
DEFAULT_MODEL=default
```

# Usage

Fetch tweets about a symbol
```
python3 src/stweet.py fetch MSFT
```

Summarize tweets via AI

```
python3 src/stweet.py ai MSFT
```

Ask recommendation about a stock

```
python3 src/stweet.py recommend MSFT
```

Ask generic Ai question

```
python3 src/stweet.py aiq "What is meaning of life?"
```

