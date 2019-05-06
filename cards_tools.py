#所有名片功能函数

'''
将对名片的 新增、查询、修改、删除 等功能封装在不同的函数中
'''

import logging
logging.basicConfig(level=logging.INFO)

"""使用：
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n) 
"""

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
    logging.debug(card_dict)
    
    # 4. 提示添加成功信息
    print("成功添加 %s 的名片" % card_dict["name"])


def show_all():

    """显示全部:
    功能分析
    循环遍历名片列表，顺序显示每一个字典的信息
    """
    print("-" * 50)
    print("功能：显示全部")

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分隔线
    print("=" * 50)
    
    count = 0

    for card_dict in card_list:
        
        logging.debug('第 %d 个数据' %(count))
        count += 1

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():

    """搜索名片
    """
    print("-" * 50)
    print("功能：搜索名片")

