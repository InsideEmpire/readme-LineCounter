import asyncio

import markdown
from flask import *
from flask import Response

from src.line_counter import get_github_lines
from src.svg_modifier import modify_svg_image

app = Flask(__name__)


@app.route('/<username>', methods=['GET'])
def get_user_code(username: str) -> Response:
    """
    获取用户 GitHub 代码行数，并返回 SVG 统计卡片
    """
    lines = asyncio.run(get_github_lines(username))

    # 检查 lines 是否为 None 或 0
    if not lines:
        return jsonify({"error": "GitHub user not found or no code available."})

    # svg_image = generate_svg_image(lines)
    svg_image = modify_svg_image(lines)

    # 确保返回 SVG 字符串
    if not isinstance(svg_image, str):
        return jsonify({"error": "Failed to generate SVG"})

    return Response(svg_image, mimetype="image/svg+xml")

@app.route("/", methods=["GET"])
def home_page():
    with open("../README.md", mode="r") as file:
        README = file.read()
        return render_template_string(markdown.markdown(README))

# Vercel 将自动运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
