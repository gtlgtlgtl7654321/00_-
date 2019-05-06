#主程序功能代码

""" 
程序的入口
每一次启动名片管理系统都通过 main 这个文件启动 
"""
#在 cards_main.py 中使用 import 导入 cards_tools 模块
import cards_tools


#添加一个 无限循环
# 无限循环
# 在开发软件时，如果 不希望程序执行后 立即退出
# 可以在程序中增加一个 无限循环
# 由用户来决定 退出程序的时机
while True:
    
    # TODO(小明) 显示系统菜单
    # 注释TODO ：在 # 后跟上TODO，用于标记需要去做的工作
    cards_tools.show_menu()

    action = input("请选择操作功能：")

    print("您选择的操作是：%s" % action)

    # 根据用户输入决定后续的操作
    if action in ["1", "2", "3"]:
        pass
        
        """ 
        pass 就是一个空语句，不做任何事情，一般用做占位语句
        是为了保持程序结构的完整性 
        """

        '''
        字符串判断
        if action in ["1", "2", "3"]:
        if action == "1" or action == "2" or action == "3":
        使用 in 针对 列表 判断，避免使用 or 拼接复杂的逻辑条件
        没有使用 int 转换用户输入，可以避免 一旦用户输入的不是数字，导致程序运行出错
        '''
        if action == "1":
            cards_tools.new_card()

        elif action == "2":
            cards_tools.show_all()

        elif action == "3":
            cards_tools.search_card()
            
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")

        break
    else:
        print("输入错误，请重新输入")