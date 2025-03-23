from src.line_counter import get_github_lines

# 测试：计算用户的总代码行数
username = "InsideEmpire"  # 替换为你想查询的 GitHub 用户名
total_lines = get_github_lines(username)
print(f"Total lines of code for {username}: {total_lines}")