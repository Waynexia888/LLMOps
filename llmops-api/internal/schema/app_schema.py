"""
Author      : Wayne Xia
File Name   : app_schema.py
Description :
"""
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, length


class ResponseReq(FlaskForm):
    """聊天接口请求认证"""
    # query必填，长度最大2000
    query = StringField("query", validators=[
        DataRequired(message="请输入你的提问，必填"),
        length(max=2000, message="提问最大长度是2000字符")
    ])
