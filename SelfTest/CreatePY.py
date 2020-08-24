print("欢迎使用Python源文件制造器")
FileName = input("请输入想要创建的文件名：")
File = open(FileName + ".py" , 'w')
print("现有相加与相减的源文件编辑功能")
Flag = int(input("请选择想要的功能（相加则填1 ， 相减则填2）："))
if Flag == 1:
    File.write("a = int(input('a:'))")
    File.write("\n")
    File.write("b = int(input('b:'))")
    File.write("\n")
    File.write("print('The result is:' , a + b)")
    File.write("\n")
elif Flag == 2:
    File.write("a = int(input('a:'))")
    File.write("\n")
    File.write("b = int(input('b:'))")
    File.write("\n")
    File.write("print('The result is:' , a - b)")
    File.write("\n")
else:
    print("无效数字！！！")

File.close()