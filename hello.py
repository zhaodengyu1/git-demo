"""git 练习用的第一个文件。

用法：python hello.py 你的名字
"""

import sys


def greet(name: str) -> str:
    return f"你好，{name}！这是你在 git 里的第一个提交。"


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(greet(name))


if __name__ == "__main__":
    main()
