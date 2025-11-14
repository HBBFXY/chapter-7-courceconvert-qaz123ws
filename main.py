import keyword

# 源文件和目标文件的路径
source_file = "random_int.py"
target_file = "random_int_converted.py"

# 读取源文件内容
with open(source_file, "r") as f:
    lines = f.readlines()

converted_lines = []
for line in lines:
    converted_line = ""
    word = ""
    for char in line:
        if char.isalnum() or char == "_":
            word += char
        else:
            # 判断当前单词是否为保留字
            if word and keyword.iskeyword(word):
                converted_line += word
            else:
                # 非保留字则转换为大写
                converted_line += word.upper()
            converted_line += char
            word = ""
    # 处理行末尾可能剩余的单词
    if word:
        if keyword.iskeyword(word):
            converted_line += word
        else:
            converted_line += word.upper()
    converted_lines.append(converted_line)

# 将转换后的内容写入目标文件
with open(target_file, "w") as f:
    f.writelines(converted_lines)

print(f"转换完成，已保存到 {target_file}")
