"""
Author      : Wayne Xia
File Name   : app_handler.py
Description :
"""
import os

from dotenv import load_dotenv
from flask import request
from openai import OpenAI

load_dotenv()


class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"ping": "pong"}

    def new(self):
        return {"hello": "world"}

    def response(self):
        """聊天接口"""
        # 1.提取用户的输入
        query = request.json.get("query")

        # 2. 构建OpenAI客户端
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # 3. 发起请求
        resp = client.responses.create(
            model="gpt-4.1-mini",
            instructions="你是一个聊天机器人，请根据用户的输入回复对应的信息。",
            input=query,
        )
        return resp.output_text
