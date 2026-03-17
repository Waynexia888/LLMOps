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

        prompt = ChatPromptTemplate.from_template("{query}")

        # 2. 构建OpenAI客户端, 并发起请求
        # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        llm = ChatOpenAI(model="gpt-4.1-mini")

        ai_message = llm.invoke(prompt.invoke({"query": req.query.data}))
        parser = StrOutputParser()

        # 3.解析响应内容
        content = parser.parse(ai_message.content)

        return success_json({"content": content})
