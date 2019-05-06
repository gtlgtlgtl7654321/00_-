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

    """新建名片
    """
    print("-" * 50)
    print("功能：新建名片")


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

