

def get_mul(num):
    if num == 1:
        return 1
    else:
        return get_mul(num - 1) * num


print(get_mul(6))
