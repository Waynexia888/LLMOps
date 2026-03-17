"""
Author      : Wayne Xia
File Name   : 2_Model批处理
Description :
"""

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.构建提示模板
prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话")

# 2.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.批处理获取响应
ai_messages = llm.batch([
    prompt.invoke({"subject": "程序员"}),
    prompt.invoke({"subject": "Python"}),
])

for ai_message in ai_messages:
    print(ai_message.content)
