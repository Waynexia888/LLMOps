"""
Author      : Wayne Xia
File Name   : 1_回调功能使用技巧
Description :
"""
import dotenv
from langchain_core.callbacks import StdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.构建链
chain = {"query": RunnablePassthrough()} | prompt | llm | StrOutputParser()

# 4.调用链并执行
content = chain.stream(
    "你好，你是？",
    config={"callbacks": [StdOutCallbackHandler()]}
)

for chunk in content:
    pass
