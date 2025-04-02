import asyncio
import os

import markdown
from flask import *
from flask import Response

from src.eval import get_github_lines, get_github_stars
from src.svg_modifier import modify_svg_image

app = Flask(__name__)


@app.route('/<username>', methods=['GET'])
def response_img(username: str) -> Response:
    response: Response

    category = request.args.get("category", "lines")
    theme = request.args.get("theme", "sunset")

    if category == "lines":
        data_value = asyncio.run(get_github_lines(username))
    elif category == "stars":
        data_value = asyncio.run(get_github_stars(username))
    else:
        return jsonify({"error": "Invalid category. Use 'lines' or 'stars'."})

        # 检查数据是否有效
    if not data_value:
        return jsonify({"error": "GitHub user not found or no data available."})

        # 生成 SVG 图片
    svg_image = modify_svg_image(data_value, category, theme)

    # 确保返回 SVG 字符串
    if not isinstance(svg_image, str):
        return jsonify({"error": "Failed to generate SVG"})

    return Response(svg_image, mimetype="image/svg+xml")

@app.route("/", methods=["GET"])
def home_page():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件所在目录
    readme_path = os.path.join(base_dir, "../README.md")  # 计算绝对路径
    with open(readme_path, mode="r") as file:
        README = file.read()
        return render_template_string(markdown.markdown(README))

# Vercel 将自动运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
