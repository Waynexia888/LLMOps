"""
Author      : Wayne Xia
File Name   : 2_JsonOutputParser使用技巧
Description :
"""

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()


# 1.构建输出json格式类
class Joke(BaseModel):
    joke: str = Field(description="回答用户的冷笑话")
    punchline: str = Field(description="冷笑话的笑点")


# 2.编排提示词
prompt = ChatPromptTemplate.from_template("回答用户的问题。\n{format_instructions}\n{query}\n")

# 3.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 4.创建json输出解析器
parser = JsonOutputParser(pydantic_object=Joke)

# 5.将格式描述嵌入到prompt中
prompt = prompt.partial(format_instructions=parser.get_format_instructions())

# 6.调用模型并解析
prompt_value = prompt.invoke({"query": "请讲一个关于程序员的冷笑话"})
print("prompt_value:", prompt_value.to_string())

ai_message = llm.invoke(prompt_value)
print("ai_message:", ai_message)

joke_json = parser.invoke(ai_message)
print("joke_json:", joke_json)
