import os

def modify_svg_image(total_lines: int) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件所在目录
    svg_path = os.path.join(base_dir, "svg/demo.svg")  # 计算绝对路径

    try:
        with open(svg_path, "r", encoding="utf-8") as svg_file:
            svg_image = svg_file.read()
    except FileNotFoundError:
        return "File not found"

    return svg_image.replace("{total_lines:,}", f"{total_lines:,}")
