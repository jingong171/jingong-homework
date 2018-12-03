filename1="cats.txt"
filename2="dogs.txt"
print("10-8:")
"""打印内容到屏幕"""
try:
    with open(filename1) as file_object:
        print("The name of the three cats are:\n ")
        for line in file_object:
            print(line)          
except FileNotFoundError:
    """找不到文件时发出友好提示"""
    print("抱歉，未找到文件名")
try:    
    with open(filename2) as file_object:
        print("\nThe name of the three dogs are:\n ")
        for line in file_object:
            print(line)
except FileNotFoundError:
    """找不到文件时发出友好提示"""
    print("抱歉，未找到文件名")
print("\n10-9: ")
try:
    with open(filename1) as file_object:
        print("The name of the three cats are:\n ")
        for line in file_object:
            print(line)
except FileNotFoundError:
    """找不到文件时一言不发"""
    pass
try:
    with open(filename2) as file_object:
        print("\nThe name of the three dogs are:\n ")
        for line in file_object:
            print(line)
except FileNotFoundError:
    """找不到文件时一言不发"""
    pass
