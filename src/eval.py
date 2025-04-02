from src.github_api import *
import aiohttp
import asyncio

async def get_github_lines(username: str) -> int:
    """
    计算 GitHub 用户的总代码行数
    :param username: username of GitHub
    :return: total code lines of a user
    """
    async with aiohttp.ClientSession() as session:
        repos = await get_github_repos(session, username)
        total_lines = 0

        tasks = [get_repo_languages(session, username, repo['name']) for repo in repos]
        languages_list: list[dict[str, int]] = await asyncio.gather(*tasks)

        for dic in languages_list:
            for language in dic.keys():
                total_lines += estimate_lines(dic[language], language)

        return total_lines

async def get_github_stars(username: str) -> int:
    """
    计算 GitHub 用户的总star数
    :param username: username of GitHub
    :return: total code lines of a user
    """
    async with aiohttp.ClientSession() as session:
        repos = await get_github_repos(session, username)

        tasks = [get_repo_stars(session, username, repo["name"]) for repo in repos]
        stars_list = await asyncio.gather(*tasks)  # 并行获取所有仓库的 Star 数

        return sum(stars_list)  # 计算总 Star 数


def estimate_lines(byte_size: int, lang: str) -> int:
    """根据字节数和编程语言类型估算代码行数"""
    avg_bytes_per_line = {
        # 常见语言
        "Python": 60, "JavaScript": 60, "TypeScript": 60,
        "Java": 100, "C": 100, "C++": 100, "C#": 90,
        "Go": 90, "Rust": 85, "Swift": 95, "Kotlin": 95,
        "PHP": 70, "Ruby": 65, "Perl": 75, "Lua": 50,

        # Web & 标记语言
        "HTML": 50, "CSS": 50, "XML": 50, "Markdown": 40,
        "YAML": 45, "JSON": 50, "TOML": 50,

        # Shell & 脚本语言
        "Shell": 55, "PowerShell": 60, "Batch": 50,

        # 数据库 & 查询语言
        "SQL": 70, "PL/SQL": 80,

        # 低级语言
        "Assembly": 30, "VHDL": 40, "Verilog": 40,

        # 函数式语言
        "Haskell": 75, "Lisp": 60, "Scheme": 55, "Clojure": 65,
        "F#": 80, "Erlang": 85, "Elixir": 80,

        # 其他语言
        "R": 65, "Matlab": 75, "Octave": 75,
        "Dart": 80, "Scala": 90, "Objective-C": 90,

        # 游戏脚本语言
        "GDScript": 55, "Pawn": 50, "ActionScript": 60,
    }

    avg_size = avg_bytes_per_line.get(lang, 80)  # 默认 80 字节/行
    print(f"avg_size: {avg_size}")
    return byte_size // avg_size