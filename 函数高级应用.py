import random
import time
from functools import wraps
from functools import lru_cache

def record_time(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result =func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}的运行时间为{end-start:.6f}秒')
        return result
    return wrapper


def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

@record_time
def main():
    print(fib1(50))

main()

# @record_time
# def download(filename):
#     """下载文件"""
#     print(f'开始下载{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成.')


# @record_time    
# def upload(filename):
#     """上传文件"""
#     print(f'开始上传{filename}.')
#     time.sleep(random.random() * 8)
#     print(f'{filename}上传完成.')


# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')

# download.__wrapped__('hi.pdf')



# def  fac(num):   #递归调用
#     if num in (0,1):
#         return 1
#     return num*fac(num-1)

# print(fac(50))



