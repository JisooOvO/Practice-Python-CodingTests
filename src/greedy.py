def coin_split(total_value=0):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count = count + (total_value // coin)
        total_value = total_value % coin

    return count

def law_of_large_numbers(p1,p2):
    _, m,k = p1
    p2.sort()
    
    first = p2[-1]
    second = p2[-2]
    result = 0

    while True:
        for i in range(k) :
            if m == 0 : break
            result = result + first
            m = m - 1
        if m == 0 : break
        result = result + second
        m = m - 1

    return result

def count_with_three_in_time(h):
    #초기값
    count = 0
    #계산
    for i in range(h+1) :# index [ )
        for j in range(60)  :
            for k in range(60) :
                if "3" in str(i) + str(j) + str(k) : # in 뒤에 str이 빠름(list 느림)
                    count = count + 1
    #반환값
    return count 

def k_knight(p):
    column = ord(p[0]) - ord('a') + 1
    row = int(p[1])
    result = 0
    steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),
             (2,1),(1,2),(-1,2),(-2,1)]

    for step in steps :
        next_row = row + step[0]
        next_column = column + step[1]
        if 1<= next_row <= 8 and 1<= next_column <= 8 :
            result += 1
    return result

if __name__ == "__main__" :
    pass