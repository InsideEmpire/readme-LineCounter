from src.eval import get_github_lines, get_github_stars
import asyncio

# 测试：计算用户的总代码行数
if __name__ == "__main__":
    username = "InsideEmpire"  # 替换为你想查询的 GitHub 用户名
    total_lines = asyncio.run(get_github_lines(username))
    total_stars = asyncio.run(get_github_stars(username))
    print(f"Total lines of code for {username}: {total_lines}")
    print(f"Total stars for {username}: {total_stars}")