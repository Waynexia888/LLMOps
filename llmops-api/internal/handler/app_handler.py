"""
Author      : Wayne Xia
File Name   : app_handler.py
Description :
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# from openai import OpenAI
from langchain_openai import ChatOpenAI

from internal.exception import FailException
from internal.schema.app_schema import ResponseReq
from pkg.response import success_json, validate_error_json

load_dotenv()


class AppHandler:
    """应用控制器"""

    def ping(self):
        # return {"ping": "pong"}
        raise FailException("数据未找到")

    def new(self):
        return {"hello": "world"}

    def response(self):
        """聊天接口"""
        # 1.提取用户的输入, POST
        req = ResponseReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2. 构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-4.1-mini")
        parser = StrOutputParser()

        # 3.构建链
        chain = prompt | llm | parser

        # 4.调用链得到结果
        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})
