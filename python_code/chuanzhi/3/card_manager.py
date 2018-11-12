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

# 是一个大的容器  存放所有的人的姓名(关注点)
#  ["老王","老李"]
card_list = ["老王"]

# 2 接受用户的数据
while True:
    num = input("请输入您的选项:")

    # 3 处理用户的选项
    if num == "1":
        # 添加名片
        name = input("请输入您想添加的人的姓名:")
        # 添加到仓库里
        card_list.append(name)
        print("添加 %s 完毕" % name)
        print("~"*90)

    elif num == "2":
        # 删除名片
        del_name = input("请输入你要删除的人的姓名:")
        # 查看这个名字是否在列表中
        if del_name in card_list:
            # 如果存在 则删除掉
            card_list.remove(del_name)
            print("%s 删除完毕" % del_name)
        else:
            # 如果不存在
            print("查无此人")

    elif num == "3":
        # 修改名片
        old_name = input("请输入要修改的人的姓名:")
        new_name = input("请输入新的名字:")
        # 查看这个名字是否在列表中
        if old_name in card_list:
            # 求下表位置
            my_index = card_list.index(old_name)
            card_list[my_index] = new_name
            print("已修改成功!")
        else:
            print("查无此人")

    elif num == "4":
        q_name = input('请输入查询名子:\n')
        if q_name in card_list:
            print('存在')
        else:
            print('查无此人')
    elif num == "5":
        for i in card_list:
            print(i)
    elif num == "0":
        # break
        exit('再见')
