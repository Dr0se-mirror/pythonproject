import os

def create_file(file_name):
    # 获取当前脚本所在目录的绝对路径
    current_dir = os.path.dirname(__file__)

    # 拼接文件的相对路径
    file_path = os.path.join(current_dir, file_name)

    # 判断文件是否存在
    if os.path.exists(file_path):
        print(f"文件 '{file_name}' 已经存在。")
    else:
        # 创建文件
        with open(file_path, 'w') as file:
            file.write("用户名,密码\n")  # 写入表头

    return file_path

def register_user(file_path):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 检查用户名是否已经存在
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            user, pwd = line.strip().split(',')
            if user == username:
                print("该用户名已存在，请选择其他用户名。")
                return

    # 如果用户名不存在，则写入文件
    with open(file_path, 'a') as file:
        file.write(f"{username},{password}\n")

    print("用户注册成功！")

def login_user(file_path):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 检查用户名和密码是否匹配
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            user, pwd = line.strip().split(',')
            if user == username and pwd == password:
                print("登录成功！")
                return
        print("用户名或密码错误。")

# 文件名
file_name = "user_info.csv"

# 创建文件并返回文件路径
file_path = create_file(file_name)

lorr=input("输入1为登录/0为注册，please！！！")
if lorr == "1":
    # 用户登录
    login_user(file_path)
else:
    register_user(file_path)


