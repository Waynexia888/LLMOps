"""
Author      : Wayne Xia
File Name   : 2_LCEL表达式简化版本
Description :
"""

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

chain = prompt | llm | parser
# 等价于以下写法
composed_chain_with_pipe = (
    RunnableParallel({"query": RunnablePassthrough()})
    .pipe(prompt)
    .pipe(llm)
    .pipe(parser)
)

print(chain.invoke({"query": "你好，你是？"}))
