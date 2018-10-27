import math
arr = ''
l_set = set()


def get_word_index(arg_str, word, start):
    global arr
    index = arg_str.find(word, start)
    if index != -1:
        l_set.add(str(index))
        get_word_index(arg_str, word, index + 1)

    return arr


res = get_word_index('aebcdeeqde', 'e', 1)
print(l_set)
# 四舍五入
print(round(2.6))
