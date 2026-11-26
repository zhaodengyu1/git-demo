"""git 练习用的第一个文件。

用法：python hello.py 你的名字
"""

import sys


def greet(name: str) -> str:
    return f"你好，{name}！这是你在 git 里的第一个提交。"


def fizzbuzz(n: int) -> list[str]:
    """返回 1..n 的 FizzBuzz 序列，顺便演示第二次提交。"""
    out: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(greet(name))


if __name__ == "__main__":
    main()
