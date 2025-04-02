import os

def modify_svg_image(data_value: int, category: str, theme: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件所在目录
    svg_path = os.path.join(base_dir, f"svg/{category}/{theme}.svg")  # 计算绝对路径

    print(f"base_dir: {base_dir}")

    try:
        with open(svg_path, "r", encoding="utf-8") as svg_file:
            svg_image = svg_file.read()
    except FileNotFoundError:
        return "File not found"

    return svg_image.replace("{data_value}", f"{data_value:,}")
