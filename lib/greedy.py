def coin_split(total_value=0):
    # 초기 값
    count = 0
    coin_types = [500,100,50,10]
    # 계산
    for coin in coin_types :
        count = count + (total_value // coin)
        total_value = total_value % coin
    # 반환 값
    return count
    # Pure Function