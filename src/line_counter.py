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
        languages_list = await asyncio.gather(*tasks)

        for languages in languages_list:
            total_lines += sum(languages.values())

        return total_lines