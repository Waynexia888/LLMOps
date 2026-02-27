"""
Author      : Wayne Xia
File Name   : app.py
Description :
"""
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http

injector = Injector()

conf = Config()

app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
