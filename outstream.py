from typing import List, Tuple, Dict
from overload import overload


def hex_to_rgb(hex_color: str) -> Tuple:
    """
    将十六进制颜色字符串转换为 RGB 元组。
    如果输入格式不符合，返回 (0, 0, 0)。
    """
    # 检查输入是否符合格式（以 # 开头，后面跟着 6 个十六进制字符）
    if isinstance(hex_color, str) and len(hex_color) == 7 and hex_color.startswith('#'):
        try:
            # 提取十六进制部分并转换为 RGB
            r = int(hex_color[1:3], 16)
            g = int(hex_color[3:5], 16)
            b = int(hex_color[5:7], 16)
            return r, g, b
        except ValueError:
            # 如果转换失败，返回全为 0 的元组
            return 0, 0, 0
    else:
        # 如果输入格式不符合，返回全为 0 的元组
        return 0, 0, 0


@overload
def rgb_to_ansi(red: int, green: int, blue: int) -> str:
    # 将颜色从 RGB 值转换为 ANSI 转义码
    return f"\033[38;2;{red};{green};{blue}m"


@overload
def rgb_to_ansi(rgb_tuple: Tuple) -> str:
    # 将颜色从 RGB 元组转换为 ANSI 转义码
    return f"\033[38;2;{rgb_tuple[0]};{rgb_tuple[1]};{rgb_tuple[2]}m"


def gradient_text(text: str, start_color, end_color=None, steps=0) -> str:
    """
    为文本设置渐变色彩。
    :param text:
    :param start_color:
    :param end_color:
    :param steps:
    """
    res = []

    if steps == 0:
        steps = len(text)

    if end_color is None:
        end_color = start_color

    # 生成渐变颜色
    for i in range(steps):
        # 计算当前颜色值
        red = int(start_color[0] + (end_color[0] - start_color[0]) * i / steps)
        green = int(start_color[1] + (end_color[1] - start_color[1]) * i / steps)
        blue = int(start_color[2] + (end_color[2] - start_color[2]) * i / steps)

        # 打印字符
        res.append(f"{rgb_to_ansi(red, green, blue)}{text[i % len(text)]}")

    # 重置颜色
    res.append("\033[0m")

    return "".join(res)


def execute_color(color: str) -> None:
    print(color, end="")
