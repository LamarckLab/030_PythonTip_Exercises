def is_string_identical(text_string):
    # 此处编写代码
    my_set = set(text_string)
    return len(my_set) == 1

# 获取输入 
text_string = input()
# 调用函数 
print(is_string_identical(text_string))
