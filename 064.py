def common_letters(word1, word2):
    # 此处编写代码
    common_set = set(word1).intersection(set(word2))
    common_str = ""
    for letter in sorted(common_set):
        common_str += letter
    return common_str
# 输入两个单词
word1 = input()
word2 = input()

# 调用函数, 并打印结果
print(common_letters(word1, word2))
