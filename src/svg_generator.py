def generate_svg_image(total_lines: int) -> str:
    """
    生成 SVG 代码
    """
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="150" viewBox="0 0 640 150" role="img">
        <rect width="100%" height="100%" fill="#1e1e2e" rx="10"/>
        <text x="50%" y="35%" fill="#fff" font-size="24" font-family="Segoe UI, Ubuntu, Sans-Serif" text-anchor="middle">
            Wow, you have written
        </text>
        <text x="50%" y="60%" fill="#ffcc00" font-size="32" font-weight="bold" font-family="Segoe UI, Ubuntu, Sans-Serif" text-anchor="middle">
            {total_lines:,}
        </text>
        <text x="50%" y="85%" fill="#fff" font-size="24" font-family="Segoe UI, Ubuntu, Sans-Serif" text-anchor="middle">
            lines of code
        </text>
    </svg>'''