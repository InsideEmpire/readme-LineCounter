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

## 技术栈 | Tech Stack

- 后端 | Backend: [Flask](https://flask.palletsprojects.com/)
- API 调用 | API Calls: [Requests](https://requests.readthedocs.io/)
- 图像生成 | Image Generation: SVG
- 部署 | Deployment: [Vercel](https://vercel.com/)

## 本地开发 | Local Development

### 环境要求 | Requirements

- Python 3.12+

### 安装依赖 | Install Dependencies

```bash
pip install -r requirements.txt
```

### 运行测试 | Run Tests

测试单个用户的代码行数 | Test code line count for a single user:
```bash
python test/test.py
```

测试 API 和 SVG 卡片生成 | Test API and SVG card generation:
```bash
python test/test_card.py
```

然后访问 `http://127.0.0.1:8888/{username}` 查看生成的卡片。

Then visit `http://127.0.0.1:8888/{username}` to view the generated card.

## 部署 | Deployment

此项目使用 Vercel 进行部署，配置已在 vercel.json 中设置。只需将代码推送到 GitHub 并在 Vercel 中导入此仓库即可完成部署。

This project is deployed using Vercel, with configuration already set in vercel.json. Simply push your code to GitHub and import this repository in Vercel to complete the deployment.

## 项目结构 | Project Structure

```
.
├── api/
│   └── index.py       # API 入口点 | API entry point
├── src/
│   ├── github_api.py  # GitHub API 交互 | GitHub API interaction
│   ├── line_counter.py# 代码行数统计 | Code line counting
│   └── svg_generator.py # SVG 生成器 | SVG generator
├── test/
│   ├── test.py        # 基本测试 | Basic test
│   └── test_card.py   # API 测试 | API test
├── requirements.txt   # 依赖项 | Dependencies
└── vercel.json        # Vercel 配置 | Vercel configuration
```

## 使用限制 | Usage Limitations

请注意，GitHub API 有使用频率限制。未经身份验证的请求限制为每小时 60 次，这可能会影响大量请求的处理。

Please note that the GitHub API has rate limits. Unauthenticated requests are limited to 60 per hour, which may affect processing of large numbers of requests.

## 贡献 | Contributing

欢迎提交 Pull Requests 或创建 Issues 来改进此项目。

Feel free to submit Pull Requests or create Issues to improve this project.
