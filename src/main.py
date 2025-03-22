from io import BytesIO

import requests
from flask import *
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

def get_github_repos(username: str) -> list[dict[str, str]]:
    '''
    获取 GitHub 用户的公共仓库信息
    :param username: username of GitHub
    :return: A json file containing a list of dict
    '''
    url = f"https://api.github.com/users/{username}/repos?type=all&per_page=100"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []

    return response.json()


def get_repo_languages(username: str, repo_name: str) -> dict[str, int]:
    '''
    获取仓库的语言使用情况
    :param username: username of GitHub
    :param repo_name: repository name of a repo
    :return: A json file which is a dict of different languages usage
    '''
    url = f"https://api.github.com/repos/{username}/{repo_name}/languages"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {repo_name}")
        return {}

    return response.json()


def get_github_lines(username: str) -> int:
    '''
    计算 GitHub 用户的总代码行数
    :param username: username of GitHub
    :return: total code lines of a user
    '''
    repos = get_github_repos(username)
    total_lines = 0

    for repo in repos:
        repo_name = repo['name']
        print(f"Getting languages for repository: {repo_name}")

        # 获取该仓库的语言使用情况
        languages = get_repo_languages(username, repo_name)

        # 累加所有语言的行数
        total_lines += sum(languages.values())

    return total_lines


@app.route('/<username>', methods=['GET'])
def get_user_code(username):
    lines = get_github_lines(username)
    if not lines:
        return jsonify({"error": "GitHub user not found or error occurred."}), 404

    img = generate_image(lines)

    # 将生成的图像保存为 PNG 格式
    img_stream = BytesIO()
    img.save(img_stream, format='PNG')
    img_stream.seek(0)

    return Image.open(img_stream)


def generate_image(code_lines):
    # 创建一个白色背景的图像
    img = Image.new('RGB', (300, 150), color='white')
    draw = ImageDraw.Draw(img)

    # 设置字体（如果服务器上没有默认字体，可以去掉 font 参数）
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # 选择字体（Windows/Mac）
    except IOError:
        font = ImageFont.load_default()  # 备用字体（Linux/无字体环境）

    # 计算文本位置，使其居中
    text = str(code_lines)
    text_width, text_height = draw.textsize(text, font=font)
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # 绘制文字
    draw.text(position, text, fill='black', font=font)

    # 保存图像到字节流
    img_stream = BytesIO()
    img.save(img_stream, format='PNG')
    img_stream.seek(0)

    return img