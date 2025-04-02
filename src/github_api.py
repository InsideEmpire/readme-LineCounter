import aiohttp

async def get_github_repos(session: aiohttp.ClientSession, username: str) -> list[dict[str, str]]:
    """
    获取 GitHub 用户的公共仓库信息
    :param session: coroutine session used for get a response from a url
    :param username: username of GitHub
    :return: A json file containing a list of dict
    """
    url = f"https://api.github.com/users/{username}/repos?type=all&per_page=100"
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error: {response.status}")
            return []

        return await response.json()


async def get_repo_languages(session: aiohttp.ClientSession, username: str, repo_name: str) -> dict[str, int]:
    """
    获取仓库的语言使用情况
    :param session: coroutine session used for get a response from a url
    :param username: username of GitHub
    :param repo_name: repository name of a repo
    :return: A json file which is a dict of different languages usage
    """
    url = f"https://api.github.com/repos/{username}/{repo_name}/languages"
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error: {response.status} - {repo_name}")
            return {}

        return await response.json()

async def get_repo_stars(session: aiohttp.ClientSession, username: str, repo_name: str) -> int:
    """
    获取仓库的语言使用情况
    :param session: coroutine session used for get a response from a url
    :param username: username of GitHub
    :param repo_name: repository name of a repo
    :return: A json file which is a dict of different languages usage
    """
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error: {response.status} - {repo_name}")
            return 0

        data = await response.json()
        return data.get("stargazers_count", 0)