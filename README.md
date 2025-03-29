# readme-LineCounter

这是一个用于统计 GitHub 用户代码行数并生成 SVG 展示卡片的工具。

This is a tool for counting the lines of code of GitHub users and generating SVG display cards.

## 功能 | Features

- 自动抓取指定 GitHub 用户的所有公开仓库
- 统计所有仓库中的代码行数
- 生成美观的 SVG 统计卡片，可直接嵌入到 GitHub Profile README 中

---

- Automatically fetch all public repositories of a specified GitHub user
- Count lines of code across all repositories
- Generate beautiful SVG statistics cards that can be embedded directly in GitHub Profile READMEs

## 演示 | Demo

[![我的代码行数](https://readme-line-counter.vercel.app/InsideEmpire)](https://github.com/InsideEmpire/readme-LineCounter)

将以下链接添加到你的 GitHub Profile README 或任何支持 markdown 的文档中即可显示你的代码行数统计卡片：

Add the following link to your GitHub Profile README or any markdown-supported document to display your code line count card:

```markdown
[![我的代码行数](https://readme-line-counter.vercel.app/{username})](https://github.com/InsideEmpire/readme-LineCounter)
```

请将 `{username}` 替换为你的 GitHub 用户名。

Please replace `{username}` with your GitHub username.

## 使用限制 | Usage Limitations

请注意，GitHub API 有使用频率限制。未经身份验证的请求限制为每小时 60 次，这可能会影响大量请求的处理。

Please note that the GitHub API has rate limits. Unauthenticated requests are limited to 60 per hour, which may affect processing of large numbers of requests.

## 贡献 | Contributing

欢迎提交 Pull Requests 或创建 Issues 来改进此项目。

Feel free to submit Pull Requests or create Issues to improve this project.
