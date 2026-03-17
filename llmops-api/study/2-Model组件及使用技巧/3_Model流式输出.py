"""
Author      : Wayne Xia
File Name   : 3_Model流式输出
Description :
"""

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排Prompt
prompt = ChatPromptTemplate.from_template("你能简单介绍下{subject}么?")

# 2.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.流式输出
response = llm.stream(prompt.invoke({"subject": "LLM和LLMOps"}))
for chunk in response:
    print(chunk.content, flush=True, end="")
