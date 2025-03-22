from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)


def generate_image(code_lines):
    # 创建一个白色背景的图像
    img = Image.new('RGB', (300, 150), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    text = str(code_lines)

    # 使用 textbbox 来计算文本大小
    bbox = draw.textbbox((0, 0), text, font=font)  # 获取文本的边界框
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 计算文本位置，使其居中
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
    draw.text(position, text, fill='black', font=font)

    # 保存图像到字节流
    img_stream = BytesIO()
    img.save(img_stream, format='PNG')
    img_stream.seek(0)

    return img_stream


@app.route('/generate_image_test/<int:code_lines>')
def generate_image_route(code_lines):
    img_stream = generate_image(code_lines)
    return send_file(img_stream, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
