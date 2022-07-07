import re

# 正则表达式：字符串模式，（判断字符串是否符合一定的标准）

# 创建模式对象
# pat = re.compile('AA') # 此处AA是正则表达式，用来验证字符串
# m = pat.search("CBAA") # search字符串被校验的内容
# 不用创建模式对象的写法
# m = re.search("AA" ,"CBAA") # 前面的字符串是规则（模板），后面的是被校验字符串
# print(m) # <re.Match object; span=(2, 4), match='AA'>

# m = re.findall("a","fsaddwass") # 前面的字符串是规则（模板），后面的是 被检验字符串
# print(m)    #  ['a', 'a']

# m = re.findall('[A-Z]+',"EWqQdfdfdAdde") '+' 代表前一个 字符一次或者无数次扩展
# print(m) # ['EW', 'Q', 'A']

# sub（替换字符串，换行等
m = re.sub("a","A","abcdasdw") #在abcdasdw 找到a 用 A替换掉
print(m) # print(m)

# 建议在正则表达式中，被比较的字符串前面加r，不用担心转义字符的问题
a = "\aabd-\'"
print(a) # abd-'
b = r"\aabd-\'"
print(b) # \aabd-\'