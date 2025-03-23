from src.github_api import *

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