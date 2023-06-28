def arrange_coins(n):
    k = 0
    while n >= k:
        n -= k
        k += 1

    return k - 1


n = 5
complete_rows = arrange_coins(n)
print(complete_rows)
