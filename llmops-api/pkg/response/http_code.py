"""
Author      : Wayne Xia
File Name   : http_code.py
Description :
"""
from enum import Enum


class HttpCode(str, Enum):
    """Http 基础业务状态码"""
    SUCCESS = "success"  # 成功状态
    FAIL = "fail"  # 失败状态
    NOT_FOUND = "not_found"  # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权（即没登录）
    FORBIDDEN = "forbidden"  # 无权限
    VALIDATION_ERROR = "validation_error"  # 数据验证错误
