import requests

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