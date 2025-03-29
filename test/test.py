from src.line_counter import get_github_lines
import asyncio

# 测试：计算用户的总代码行数
if __name__ == "__main__":
    username = "InsideEmpire"  # 替换为你想查询的 GitHub 用户名
    total_lines = asyncio.run(get_github_lines(username))
    print(f"Total lines of code for {username}: {total_lines}")