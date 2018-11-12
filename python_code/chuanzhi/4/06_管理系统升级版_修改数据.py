# 是一个大的容器  存放所有的人的姓名(关注点)
#  [{},{},{},{}]
card_list = []

# {
#     name : lw,
#     age  : 18,
#     addr : qq
#
# }

while True:
    # 1 显示界面
    print('=======================')
    print('欢迎使用 名片管理系统 v1.0')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查看某人是否存在')
    print('5.查看所有名字')
    print('0.退出系统')
    print('=======================')

    # 2 接受用户的数据
    num = input("请输入您的选项:")

    # 3 处理用户的选项
    if num == "1":
        # 添加名片
        name = input("请输入您想添加的人的姓名:")
        age = input("请输入您想添加的人的年龄:")
        addr = input("请输入您想添加的人的住址:")

        # 先定义一个字典
        my_dict = {}
        # { "name": xxx }
        my_dict["name"] = name
        my_dict["age"] = age
        my_dict["addr"] = addr

        # 向列表中添加字典 (人的信息)
        card_list.append(my_dict)

        print("添加成功")
        print("~" * 100)

    elif num == "2":
        # 删除名片
        del_name = input("请输入你要删除的人的姓名:")
        # 查看这个名字是否在列表中
        #  [{},{},{},{}]
        # {
        #     name : lw,
        #     age  : 18,
        #     addr : qq
        #
        # }
        # for循环中i代表字典 ==> 某个人
        for i in card_list:
            #              i["name"]==> 人名
            if del_name == i["name"]:
                card_list.remove(i)  # 删除的整个人
                print("删除完毕!!!")
                break  # 跳出循环
        else:
            # 没有此人
            print("查无此人")

    elif num == "3":
        # 修改名片
        old_name = input("请输入要修改的人的姓名:")
        new_name = input("请输入新的名字:")
        # 查看这个名字是否在列表中
        #  [{},{},{},{}]
        # {
        #     name : lw,
        #     age  : 18,
        #     addr : qq
        #
        # }
        for i in card_list:
            if old_name == i["name"]:
                i["name"] = new_name
                print("修改完毕")
                break
        else:
            print("查无此人")

    elif num == "4":
        # 查看某人是否存在
        find_name = input("请输入您想查找的人的姓名:")
        # 查找是不是有此人
        for i in card_list:
            if find_name == i["name"]:
                print("有这个人!!!")
                break
        else:
            print("查无此人")

    elif num == "5":
        # 查看所有人的姓名
        for i in card_list:
            print("姓名:%s " % i["name"], end='')
            print("年龄:%s " % i["age"], end='')
            print("地址:%s " % i["addr"], end='')
            print()

        print("~" * 90)

    elif num == "0":
        print("谢谢使用...欢迎下次来玩")
        break
