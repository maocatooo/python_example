import os
from jinja2 import Environment
from jinja2 import FileSystemLoader

BASE_DIR = os.path.dirname(__file__)


def render(params: dict):
    env = Environment(loader=FileSystemLoader(BASE_DIR))
    # 给 params 添加额外参数
    params.update({
        "title": 1
    })
    template = env.get_template("template.html")
    content = template.render(**params)
    return content
