## 메모제이션
# 버퍼 -> 딕셔너리
__fibo_cache_ = {}

# 누적재귀
def fibonacci(n):
    if n in __fibo_cache_ :
        return __fibo_cache_[n]
    else :
        __fibo_cache_[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1) 
        return __fibo_cache_[n]

## 꼬리재귀 -> Python , Js
# 컴파일러에서 강제로 for loop로 치환
def maximum(lst, acc=0) :
    if lst == [] : return acc
    else : maximum(lst[1:], acc if acc > lst[0] else lst[0])
        

if __name__ == "__main__" :
    print(maximum([1,2,3,5,2]))