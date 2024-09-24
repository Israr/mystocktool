# mystocktool

A basic tool to analyzing Stocks sentiment with Azure OpenAI

# Setup

Before you can use the tool, you need to prvide your API keys and endpoints for your deployment.

```
OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_ENDPOINT=https://xxxxx.openai.azure.com/
AZURE_OPENAI_API_KEY=xxxxxx
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

