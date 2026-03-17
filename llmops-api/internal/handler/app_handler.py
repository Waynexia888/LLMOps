"""
Author      : Wayne Xia
File Name   : app_handler.py
Description :
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

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
        # 1.提取用户的输入
        req = ResponseReq()
        if not req.validate():
            return validate_error_json(req.errors)

        print("req--------------------", req.query.data)
        query = req.query.data

        # 2. 构建OpenAI客户端
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # 3. 发起请求
        content = client.responses.create(
            model="gpt-4.1-mini",
            instructions="你是一个聊天机器人，请根据用户的输入回复对应的信息。",
            input=query,
        )

        return success_json({"content": content.output_text})
