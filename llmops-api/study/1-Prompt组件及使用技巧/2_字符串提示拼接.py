"""
Author      : Wayne Xia
File Name   : 2_字符串提示拼接
Description :
"""

from langchain_core.prompts import PromptTemplate

prompt = (
        PromptTemplate.from_template("请将一个关于{subject}的冷笑话")
        + "，让我开心下"
        + "\n使用{language}语言。"
)

print(prompt)

print(prompt.format(subject="程序员", language="中文"))
