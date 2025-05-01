# mystocktool

A basic tool to analyzing Stocks sentiment with Azure OpenAI

# Setup

## Prerequisites
install the following packages

```bash
pip install -r requirements.txt
```

Before you can use the tool, you need to prvide your API keys and endpoints for your deployment. You can use this either Azure OpenAI or Mistral.

For Azure OpenAI , you need to set the following environment variables in your `.env` file:

```
cat > src/.env << EOF
OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
AZURE_CHAT_MODEL=<your_azure_deployment_name>
EOF
```

For Mistral, you need to set the following environment variables in your `.env` file:

```
cat > src/.env << EOF
MISTRAL_API_KEY=<your_mistral_api_key>
DEFAULT_MODEL=mistral
EOF
```

You can get your free mistral API key from  [mistral.ai](https://console.mistral.ai/api-keys)

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

