def count_frequency(lst):
    # 此处编写代码
    count_dict = {}
    for element in lst:
        if element not in count_dict:
            count_dict[element] = 1
        else:
            count_dict[element] += 1
    return count_dict

# 获取用户输入 
lst = list(input().split())

# 调用函数 
print(count_frequency(lst))
