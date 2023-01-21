# 한 줄 짜리 주석
"""
코드 작성 일자 : 2023년 1월 22일
코드 작성자 : sungmizz
코드 이름 : utils.py
코드 목적 : study
"""


# 함수의 앞에는 빈줄이 2줄 필요함
# 코드의 맨 끝에는 한줄만 필요

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


def pp():
    print("hello")
