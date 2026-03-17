"""
Author      : Wayne Xia
File Name   : 1_RunnableParallel使用技巧
Description :
"""

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排2个提示模板
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话，尽可能短")
poem_prompt = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗，尽可能短")

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建输出解析器
parser = StrOutputParser()

# 4.构建两条链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.使用RunnableParallel创建并行可运行
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

# 6.运行并行可运行组件得到响应结果
resp = map_chain.invoke({"subject": "程序员"})

print(resp)
