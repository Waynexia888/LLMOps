"""
Author      : Wayne Xia
File Name   : 1_手写chain实现简易版本
Description :
"""
from typing import Any

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()


class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        output: Any = input
        for step in self.steps:
            output = step.invoke(output)
            print(step)
            print("执行结果:", output)
            print("===============")

        return output


chain = Chain([prompt, llm, parser])

print(chain.invoke({"query": "你好，你是?"}))
