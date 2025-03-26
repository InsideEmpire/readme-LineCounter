def modify_svg_image(total_lines: int) -> str:
    try:
        with open("../src/svg/demo.svg", "r", encoding="utf-8") as svg_file:
            svg_image = svg_file.read()
    except FileNotFoundError:
        svg_image = "File not found"

    new_svg_image = svg_image.replace("{total_lines:,}", f"{total_lines:,}")

    return new_svg_image