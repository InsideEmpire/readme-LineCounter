from src.main import app  # 从 src/github_code.py 导入 Flask 应用

# Vercel 将自动运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
