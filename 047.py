def get_missing_letters(word_string):
    # 此处编写你的代码
    full_str = "abcdefghijklmnopqrstuvwxyz"
    output_str = ""
    for element in full_str:
        if element not in word_string:
            output_str += element
    return output_str

# 获取输入的字符串 
word_string = input()

# 调用函数输出结果 
print(get_missing_letters(word_string))
