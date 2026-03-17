"""
Author      : Wayne Xia
File Name   : 1_LLM和ChatModel使用技巧
Description :
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.生成内容
prompt_value = prompt.invoke({"query": "现在是几点，请讲一个关于程序员的冷笑话"})
ai_message = llm.invoke(prompt_value)

# 4.提取内容
print("type:", ai_message.type)
print("content:", ai_message.content)
print("response_metadata:", ai_message.response_metadata)
