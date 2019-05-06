#所有名片功能函数

'''
将对名片的 新增、查询、修改、删除 等功能封装在不同的函数中
'''
# 所有名片记录的列表
card_list = []

def show_menu():

    """显示菜单
    """
    
    print("*" * 50)
    print("欢迎使用【菜单管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():

    """
    新建名片:
    功能分析:
        提示用户依次输入名片信息
        将名片信息保存到一个字典
        将字典添加到名片列表
        提示名片添加完成
    """
    print("-" * 50)
    print("功能：新建名片")

    # 1. 提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入 QQ 号码：")
    email = input("请输入邮箱：")
    # 2. 将用户信息保存到一个字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}

    # 3. 将用户字典添加到名片列表
    card_list.append(card_dict)

    print(card_list)
    
    # 4. 提示添加成功信息
    print("成功添加 %s 的名片" % card_dict["name"])


def show_all():

    """显示全部
    """
    print("-" * 50)
    print("功能：显示全部")


def search_card():

    """搜索名片
    """
    print("-" * 50)
    print("功能：搜索名片")

