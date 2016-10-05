# coding=utf-8
# 号后面的文字为注释

# = 为赋值运算符
# 变量命名规则与C相同
x = 2
y = 1.2
z = ""
# print 输出（两部分输出之间自动加空格，结尾自动换行），格式化输出与C中printf() 函数相同
print x, y                  # 2 1.2
print "Hello", "world!"     # Hello world!
print "%d : %.1f" % (x, y)  # 2 : 1.2
# id() 获取常量地址
print id(y)                 # 45502600 每次运行地址不相同
print id(x)                 # 45441768
print id(3)                 # 45441768 内容相同的量地址相同
# + - * / % += -= *= /= %= | ^ & 运算与C相同 // 为整数除法 ** 为求幂运算
print y / x, 3 / x          # 0.6 1
print y // x, y ** x        # 0.0 1.44
# < > <= >= != == 运算与C相同，返回值为bool型，非零为真，零或空值为假
print x < y, x == 2.0       # False True
# and or not 运算与C中 && || ! 运算相同
print True or x < y         # True
# raw_input() 等待输入并返回输入，返回所输入字符串
temp = raw_input("Please input a number: ")
                            # Please input a number: 3
print temp                  # 3

# Python 数据类型：整型 长整型 浮点型 复数型 字符串 列表 元组 字典
# type() 查看数据类型
print type(3)               # <type 'int'>
print type(3L)              # <type 'long'>
print type(3.0)             # <type 'float'>
print type(2 + 1j)          # <type 'complex'>
print type("Hello world")   # <type 'str'>
# 强制类型转换与C相同
print type(long(3))         # <type 'long'>
# 可使用' ' " " """ """ 表示字符串，转义字符与C相同，Python中无ASCLL表示法
print "What's your name?"   # What's your name?
print 'What\'s your name?'  # What's your name?
print 'How does "HELLO" spells?'
                            # How does "HELLO" spells?
mail = """tom:
    i am jack.
    good bye!"""
print mail                  # tom:
                            #    i am jack.
                            #    good bye!
print mail == 'tom:\n    i am jack.\n    good bye!'
                            # True
# [] 用于取序列（字符串属于序列）内容，编号方式与C相同，截取操作采用超尾，首尾空着默认取字符串首尾
print mail[2]               # m
print mail[0:3]             # tom
print mail[:3]              # tom
print mail[5:]              #     i am jack.
                            #     good bye!
print mail[:3:2]            # tm
print mail[-31:-34:-1]      # mot
# 序列的基本操作：len() + * in max() min() cmp()
# 以下用元组举例，对于列表和字典可用相同方法调用，元组缺点为内容不可更改
t = ('guanzp', 20, 'male')
print type(t)               # <type 'tuple'>
print t                     # ('guanzp', 20, 'male')
print t[1]                  # 20
print len("Hello")          # 5
print len(t)                # 3
print "Hello" + "world"     # Helloworld
print t + t                 # ('guanzp', 20, 'male', 'guanzp', 20, 'male')
print "*" * 5               # *****
print t * 2                 # ('guanzp', 20, 'male', 'guanzp', 20, 'male')
print 'a' in 'abcde'        # True
print 2 in t                # False
print max('max')            # x
print max(t)                # male
print min('31245')          # 1
print min(t)                # 20
print cmp('123', 'abc')     # -1
print cmp(t, t)             # 0
name, age, sex = t          # 一种赋值方式
# t[0] = 30     # 错误，无法修改元组内容
# 列表操作：添加 删除 修改
l = ['guanzp', 20, 'male']
print type(l)               # <type 'list'>
print id(l)                 # 49418184
l[0] = 'guant'              # 修改列表元素
print l                     # ['guant', 20, 'male']
print id(l)                 # 49418184 注意地址不变
l.append(20)                # 插入元素到列表尾
print l                     # ['guant', 20, 'male', 20]
l.remove(20)                # 移除列表中第一个出现的元素
print l                     # ['guant', 'male', 20]
l.append('male')
del(l[3])                   # 删除指定下标元素
print l                     # ['guant', 'male', 20]
# 字典 一种哈希表 操作：弹出 清除 删除
d = {'name': 'guanzp', 'age': 20, 'gender': 'male'}
print d                     # {'age': 20, 'gental': 'male', 'name': 'guanzp'}
print type(d)               # <type 'dict'>
print d['gender']           # male
d['tel'] = '18650332252'    # 增加/修改字典元素
print d                     # {'gender': 'male', 'age': 20, 'tel': '18650332252', 'name': 'guanzp'}
d['tel'] = '12345678910'
print d                     # {'gender': 'male', 'age': 20, 'tel': '12345678910', 'name': 'guanzp'}
del(d['tel'])               # 删除指定元素
print d                     # {'gender': 'male', 'age': 20, 'name': 'guanzp'}
print d.get('name', 'error')# guanzp
print d.get('tel', 'error') # error
print d.keys()              # ['gender', 'age', 'name']
print d.values()            # ['male', 20, 'guanzp']
print d.items()             # [('gender', 'male'), ('age', 20), ('name', 'guanzp')]
age = d.pop('age')          # 弹出指定元素并返回该值
print age, d                # 20 {'gender': 'male', 'name': 'guanzp'}
d.clear()                   # 清空字典
print d                     # {}
del(d)                      # 删除字典
# print d   # 错误，提示无此名称的变量

# if ... else ... 条件表达式，pass 表示不做任何操作
if False:
    print 'OK!'
elif True:
    print "May not."
else:
    pass                    # May not.

# for...else... 循环语句
# range() 函数生成一个列表，末尾参数采用超尾，最后一个参数步长默认为1
print range(5)              # [0, 1, 2, 3, 4]
print range(1, 11, 2)       # [1, 3, 5, 7, 9]
# 以下例子中k参数遍历range()产生的序列，continue break 与C相同，当循环正常结束执行else 语句
sum = 0
for k in range(1, 550):
    if k <= 100:
        sum += k
    else:
        continue
else:
    print sum              # 5050

d = {'name': 'guanzp', 'age': 20, 'gender': 'male'}
for k, v in d.items():
    print k, v              # gender male
                            # age 20
                            # name guanzp

# import 引用关键字，用于引用模块，一般写在文件头
import time
# 以下time在引用模块后才能调用sleep() 函数，循环将隔一秒输出一次数字
for x in range(3):
    print x
    time.sleep(1)           # 0
                            # 1
                            # 2

# while...else... 循环语句
k = raw_input("Please enter a letter, q for quit: ")
while k != 'q' and k != "":
    print k
    k = raw_input("Please enter a letter, q for quit: ")
else:
    print "ending"
                            # Please enter a letter, q for quit: break
                            # break
                            # Please enter a letter, q for quit: hello
                            # hello
                            # Please enter a letter, q for quit: q
                            # ending

# 自定义函数，其中形参实参、局部变量和全局变量概念与C相同，global 可在函数体内强制声明全局变量（至少运行一次函数后才会声明）
# 默认形参与C++相同，函数默认返回None，元组参数为*x，字典形参为**x
def add(a, b = 0, c = 0):
    global g
    g = 1
    if a < b:
        return a + b + c + g
    elif a > b:
        return a - b - c - g
    else:
        pass

# print g   # 编译错误，提示无此名称的变量
print add(1)                # 0
print add(3, c = 2)         # 0
print g                     # 1
print add(1, 1)             # None
# print c   # 错误，提示无此名称的变量

def output1(**d):
    for k in d:
        print "%s: %s" % (k, d[k])

output1(name = 'guanzp', age = 20, gender = 'male')
                            # gender: male
                            # age: 20
                            # name: guanzp

def output2(name, age, gender):
    print 'name:', name
    print 'age:', age
    print 'gender:', gender

t = ('guanzp', 20, 'male')
output2(*t)                 # name: guanzp
                            # age: 20
                            # gender: male

output2(**d)                # name: guanzp
                            # age: 20
                            # gender: male
# lambda 关键字，用于单行自定义简单函数，可无函数名
# lambda x, y: x + y 等价于 def fun(x, y):@换行并缩进@  return x + y
# 用字典实现switch 语句
fun_d = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
print fun_d['+'](1, 2)       # 3

# 常用内置函数： abs() max() min() divmod() pow() round() callable() isinstance() cmp()
# 类型转化函数： str() list() tuple() hex() oct() chr() ord()
print divmod(10, 3)         # (3, 1)    # 返回10 // 3 和 10 % 3 的值
print pow(2, 3)             # 8         # 返回 2 ** 3 的值
print pow(2, 3, 5)          # 3         # 返回 2 ** 3 % 5 的值
print round(1.25, 1)        # 1.3       # 返回第二个实参位数个小数的四舍五入值
print callable(output2)     # True      # 判断函数是否被定义
print isinstance(d, dict)   # True      # 判断数据类型
print cmp(1, 3)             # -1        # 可比较各种数据类型，返回值为-1 1 0
# 字符串处理函数 str.capitalize() str.replace() str.split()
s = "hello!"
print s.capitalize()        # Hello!    # 返回调用对象的首字母大写字符串
print s.replace('h', 'H', 1)# Hello!    # 返回调用对象所有指定字符串替换后的字符串，最后一个参数默认为-1
s = "192.168.1.123"
print s.split('.', 10)      # ['192', '168', '1', '123']    # 返回调用对象被指定元素分割后的列表，最后一个参数默认-1
# 序列处理函数 filter() zip() map() reduce()
l = range(1, 11)
print filter(lambda x: x % 2 == 0, l)
                            # [2, 4, 6, 8, 10]
                            # 返回原序列满足函数条件的新序列
name = ['milo', 'zou', 'tom']
age = [20, 30, 40]
tel = ['123', '456']
print zip(name, age, tel)   # [('milo', 20, '123'), ('zou', 30, '456')]
                            # 返回参数列表中匹配元组的列表（取最小列表元素匹配）
teln = []
for k in tel:
    teln.append(int(k))
teln.append(789)
print teln                  # [123, 456, 789]
print map(lambda x, y: x + y, age, teln)
                            # [143, 486, 829]   # 返回两个列表对应元素进行函数计算之后的结果列表
print reduce(lambda x, y: x + y, range(1, 101))
                            # 5050      # 取列表中每个元素进行函数操作，返回结果

# python 的多文件操作，现假设已经存在一个guan.py 文件，且其中定义了output4()@换行并缩进@  print 'guan' 函数
# 内置变量 __name__ 当在源文件中调用该变量时，__name__ == ’__main__‘，当文件被import 时，__name__ == 文件名
import guan
guan.output4()              # guan      # 调用import 文件中的方法应用 文件名.函数名(参数列表) 形式调用

# 正则表达式，需要引入re 模块
# re.findall() 从第二个字符串实参中找到符合第一个表达式规则的字符串列表
# . 匹配任何非空白（\t\n\r\f\v）字符
# [] 用来指定一个字符集：[abc], [a-z] 中间不能包含空格
# [^] 补集匹配不在区间范围内的字符
# ^ 匹配行首
# $ 匹配行尾
# \ 将元字符作为一般字符处理，或转义字符
# | “或者”符号，匹配前者或后者
# () 括号内容独立成组进行匹配
# \d == [0-9]   \D == [^0-9]    \s == [\t\n\r\f\v]  \S == [^\t\n\r\f\v] \w == [a-zA-Z0-9]   \W == [^a-zA-Z0-9]
# {n} 之前一位字符重复n次 {a,b} 之前一位字符重复a-b 次
# * == {0,∞}    + == {1,∞}  ? == {0,1}  但*+? 元字符效率比{}效率高
import re
r = r"^010-?[0-9]{5}\d{3}$"
print re.findall(r, "01054687912")
                            # ['01054687912']
r = r"\d+.?\d* ?[\+\-\*/] ?\d+.?[0123456789]*"
print re.findall(r, "30.22+123.55 and 15 + 122 and 15 /+ 13 and 3.0 + 11")
                            # ['30.22+123.55', '15 + 122 ', '3.0 + 11']
# compile() 编译正则表达式，使匹配效率更高，更灵活
r_c = re.compile(r"\d+.?\d* ?[\+\-\*/] ?\d+.?[0123456789]*")
print r_c.findall("30.2 / 123.5")
                            # ['30.2 / 123.5']
r_c = re.compile(r"cctv", re.I)
print r_c.findall("CcTv")   # ['CcTv']  # 忽略大小写匹配
# 正则表达式常用方法：
# re.match()                返回行首匹配的match 对象
# re.search()               返回全字符串匹配的match 对象
# re.finditer()             返回首次遇到匹配字符串的迭代器
# SRE_Match.group()         返回首次匹配字符串
# SRE_Match.start()         返回首次匹配字符串首部
# SRE_Match.end()           返回首次匹配尾部位置（超尾）
# SRE_Match.span()          返回(SRE_Match.start(), SRE_Match.span()) 元组
r_c_m = r_c.search("hello Cctv hello, CCTV")
print r_c_m.group(), r_c_m.start(), r_c_m.end(), r_c_m.span()
                            # Cctv 6 10 (6, 10)
# re顶级函数调用（从re文件调用，而不是re对象调用） match() search() sub() subn() split() findall()
print re.sub(r, "expression", "30.22+123.55 and 15 + 122 and 15 /+ 13 and 3.0 + 11")
                            # expression and expressionand 15 /+ 13 and expression
print re.split(r'[\+\-\*'r'/]', "30.22+123.55 and 15 + 122 and 15 /+ 13 and 3.0 + 11")
                            # ['30.22', '123.55 and 15 ', ' 122 and 15 ', '', ' 13 and 3.0 ', ' 11']
# 编译标志，在re.compile(r"...", re....) 第二个参数和 re.findall(r"....", "...", re....) 第三个参数中使用
# re.S 使.匹配包括换行在内的所有字符
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别匹配，法语或其他符号
# re.M 多行匹配（影响^行首匹配和$行尾匹配符号）
# re.X 能够使用REs的 verbose 状态，使之被组织得更清晰易懂
r = r"www.cctv.com|^www.cctv.cn|^cctv"
s = "www\ncctv\ncom"
print re.findall(r, s)      # []
print re.findall(r, s, re.S)# ['www\ncctv\ncom']
s = """www.cctv.com hello
hello cctv
cctv hello"""
print re.findall(r, s)      # ['www.cctv.com']
print re.findall(r, s, re.M)# ['www.cctv.com', 'cctv', 'cctv']
# 正则表达式应用：网络爬虫
import urllib
r = r'<img src="(.{1,100}\.jpg)"'
r_c = re.compile(r)
l = r_c.findall(urllib.urlopen('http://image.baidu.com/').read())
for k in range(len(l)):
    print "%d: %s" % (k + 1, l[k])
    urllib.urlretrieve(l[k], "%d.jpg" % k)
                            # 1: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%94%AF%E7%BE%8E%E6%91%84%E5%BD%B183.jpg
                            # 2: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%AE%A0%E7%89%A983.jpg
                            # 3: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%88%98%E6%B6%9B83.jpg
                            # 4: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%8A%A8%E6%BC%AB83.jpg
                            # 5: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%A3%81%E7%BA%B883.jpg
                            # 6: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%A4%B4%E5%83%8F83.jpg
                            # 7: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E9%A3%8E%E6%99%AF83.jpg
                            # 8: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E5%B0%8F%E6%B8%85%E6%96%B0.jpg
                            # 9: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/%E6%98%9F%E7%A9%BA83.jpg
                            # 10: http://img0.bdstatic.com/img/image/shouye/xiaoxiao/PPT83.jpg

# 深拷贝与浅拷贝
import copy
a = [1, 2, 3, [4, 5, 6]]
b = a                       # 浅拷贝，引用拷贝
c = copy.copy(a)            # 中等程度拷贝，但只是做第一层拷贝
d = copy.deepcopy(a)        # 深拷贝，效率低，可对所有层次进行拷贝
a[3].append(7)
a.append(8)
print a                     # [1, 2, 3, [4, 5, 6, 7], 8]
print b                     # [1, 2, 3, [4, 5, 6, 7], 8]
print c                     # [1, 2, 3, [4, 5, 6, 7]]
print d                     # [1, 2, 3, [4, 5, 6]]

# 文件与目录
# open() 第一个参数为打开文件名，第二个参数为打开模式，默认为r，返回文件对象
# r 只读 r+ 读写
# w 写入，先删除源文件，再重新写入，如果文件没有则创建
# w+ 读写，先删除源文件，再重新写入，如果文件没有则创建（可以写入输出）
# a 写入，在文件末尾追加新的内容，文件不存在则创建
# a+ 读写，在文件末尾追加新的内容，文件不存在则创建
# b 打开二进制文件，与r, w, a, +结合使用
# 以上字符串表示模式与C 中文件打开模式类似
# String = FileObj.read([size])         # 读取文件size 字节内容，size 默认为-1，并将文件操作标记（C 中的文件指针）标记到size 位置（默认文件尾）
# String = FileObj.readline([size])     # 按行读取size 字节文件内容，size 默认为-1，并将文件操作标记移至下一行
# FileObj.close()                       # 关闭文件
# List = FileObj.readlines([size])      # 把文件每行作为一个list 成员，并返回list ，并将文件操作标记移到size 位置（默认文件尾）
# FileObj.next()                        # 将文件操作标记下移一行
# FileObj.write(string)                 # 把string 写入文件（不自动添加换行符和空格）
# FileObj.writelines(List)              # 把List 内容写入文件，每个元素末尾添加一个换行
# FileObj.seek(偏移量, 0/1/2)            # 指定文件指针位置，0表示文件头，1表示当前位置，2表示文件尾，同C
# FileObj.flush()                       # 不关闭文件刷新文件内容
# 文件操作应用：现假设在C:\Users\13238\Desktop\pythoncaogao 目录下已创建一个名为cat a.t 的文件内容为：
# hello world
# hello hello world
# 将其中行首'hello' 字符串替换为‘beautiful’
f = open('C:\\Users\\13238\\Desktop\\pythoncaogao\\cat a.t', 'r+')
r = re.compile(r'^hello', re.M)
s = re.sub(r, 'beautiful', f.read())
f.seek(0, 0)
f.write(s)
f.seek(0, 0)
print f.read()

# 系统操作，os 模块
import os
# os.mkdir('C:\\Users\\13238\\Desktop\\pythoncaogao\\caogao')
# os.makedirs('C:\\Users\\13238\\Desktop\\pythoncaogao\\a\\b\\c')
print os.listdir('.')
print os.path.isdir('C:\\Users\\13238\\Desktop\\pythoncaogao\\a\\b')
print os.getcwd()
# os.chdir('/')
# os 模块练习：遍历目录
def dir(path):
    filelist = os.listdir(path)
    os.chdir(path)
    fpath = os.getcwd()
    l = []
    for i in range(len(filelist)):
        if os.path.isdir(filelist[i]):
            l += dir(path + '\\' + filelist[i])
            os.chdir(path)
        else:
            l.append(fpath + '\\' + filelist[i])
    return l

l = dir('C:\\Users\\13238\\Desktop')
for k in l:
    print k

# os.removedirs('C:\\Users\\13238\\Desktop\\pythoncaogao\\a\\b\\c')
# os.rmdir('C:\\Users\\13238\\Desktop\\pythoncaogao\\caogao')

# try...except...finally 和raise 异常处理
filename = raw_input('请输入要打开文件名: ')
try:
    f = open(filename)
    print hello
except IOError, msg:
    print '您要打开的文件不存在'
except NameError, msg:
    print '变量调用错误'
    f.close()
finally:
    print 'ha'