#! /home/ikhan/anaconda3/bin/python
import os
import typer
from langchain_openai import  AzureChatOpenAI
import requests
from dotenv import load_dotenv
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

load_dotenv()

app = typer.Typer()

def post_process(response):
    result = response.content
    result = result.replace("AI:", "")
    result = result.replace("System:", "")
    return result

def ai_respone(llm_q):
    model = os.getenv("DEFAULT_MODEL")
    if model == "default":
        print("Using default model")
        model = os.getenv("AZURE_CHAT_MODEL")
        llm = AzureChatOpenAI(model_name=model, deployment_name=model)
        result = post_process(llm.invoke(llm_q))
    elif model == "mistral":
        print("Using Mistral model")
        from mistralai import Mistral
        api_key = os.environ["MISTRAL_API_KEY"]
        model = "mistral-large-latest"
        client = Mistral(api_key=api_key)
        chat_response = client.chat.complete(
            model= model,
            messages = [
                {
                    "role": "user",
                    "content": llm_q
                },
            ])
        result = chat_response.choices[0].message.content
    else:
        print("Invalid model")
        return
    return result


def fetch_messages(symbol):
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["messages"]

def create_ctx_from_messages(messages):
    context = ""
    for m in messages:
        context += f"{m['user']['username']}: {m['body']}\n\n"
    return context

@app.command("recommend", help="Ask AI to provide recommendation on a stock symbol")
def recommend(symbol):
    question = "What is verdict on " + symbol
    system_template = """You are a helpful AI that knows a lot about stocks. You are asked
a question about a stock, Look at the context below and try to provide a helpful and informative answer.
You can provide a recommendation to Buy, Sell, or Neutral. If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
{context}"""
    msgs = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    # model = 'gpt-35-turbo'
    model = 'gpt-40-08-06'
    llm = AzureChatOpenAI(model_name=model, deployment_name=model)
    messages = fetch_messages(symbol)
    context = create_ctx_from_messages(messages)
    prompt_template = ChatPromptTemplate.from_messages(msgs)
    llm_q = prompt_template.format(context=context, question=question)
    result = ai_respone(llm_q)
    print(result)

@app.command("ai", help="Ask AI to provide summary about a stock symbol")
def ai(symbol, question=None):
    if question is None:
       question = "What is new with " + symbol
    system_template = """You are a helpful AI that knows a lot about stocks. You are asked
a question about a stock, Look at the context below and try to provide a helpful and informative answer.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use five sentences maximum and keep the answer as concise as possible.
For longer answers, You should use bullet points in your answer for readability.
----------------
{context}"""
    msgs = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    # model = 'gpt-35-turbo'
    model = 'gpt-40-08-06'
    llm = AzureChatOpenAI(model_name=model, deployment_name=model)
    messages = fetch_messages(symbol)
    context = create_ctx_from_messages(messages)
    prompt_template = ChatPromptTemplate.from_messages(msgs)
    llm_q = prompt_template.format(context=context, question=question)
    result = ai_respone(llm_q)
    print(result)
    
@app.command("aiq")
def aiq(question):
    system_template = """You are a helpful AI assistant. You are asked a question and you provide a helpful and informative answer. """
    msgs = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    model = os.getenv("AZURE_CHAT_MODEL")
    llm = AzureChatOpenAI(model_name=model, deployment_name=model)
    prompt_template = ChatPromptTemplate.from_messages(msgs)
    llm_q = prompt_template.format(question=question)
    result = ai_respone(llm_q)
    print(result)


@app.command("fetch", help="fetch tweets from stocktwits for a given symbol")
def fetch(symbol):
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
    # fetch data from url using requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    data = response.json()
    for m in data["messages"]:
        print(f"{m['user']['username']}: {m['body']}")


if __name__ == '__main__':
    app()

