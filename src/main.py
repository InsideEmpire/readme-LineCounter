import requests


# 获取 GitHub 用户的公共仓库信息
def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos?type=all&per_page=100"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []

    return response.json()


# 获取仓库的语言使用情况
def get_repo_languages(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/languages"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {repo_name}")
        return {}

    return response.json()


# 计算 GitHub 用户的总代码行数
def get_github_lines(username):
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


