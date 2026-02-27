"""
Author      : Wayne Xia
File Name   : config.py
Description :
"""


class Config:
    def __init__(self):
        # 关闭wtf的CSRF保护
        self.WTF_CSRF_ENABLED = False
