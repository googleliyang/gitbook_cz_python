import os
import multiprocessing


def copy_file(src_path, dest_path, file):
    """将源目录demo下的file文件数据 拷贝到 目的目录demo-备份下的file文件中去"""
    # 4.1 打开源文件 用以读
    src_file = open(src_path + "/" + file, "rb")

    # 4.2 打开目的文件 用以写
    dest_file = open(dest_path + "/" + file, "wb")

    # 4.3 一边读取文件 一边写入目的文件
    while True:
        file_data = src_file.read(4096)
        if not file_data:
            break
        dest_file.write(file_data)

    # 4.4 关闭文件
    src_file.close()
    dest_file.close()

def main():
    # 一　　先实现单任务文件拷贝工具　　　二　　＋　进程池
    # 1 输入需要备份的目录名  src_path源目录
    src_path = input("请输入需要备份的目录名称:")

    # 2 推导出 创建备份目录名称   dest_path
    dest_path = src_path + '-备份'
    os.mkdir(dest_path)

    # 3 获取到源目录下的所有文件名称 os.listdir()
    file_list = os.listdir(src_path)

    # 4 获取每一个文件名称 file      src_path + file  ——>  dest_path + file
    # 5 重复第4步  直到拷贝完成所有文件
    # ４.1 创建一个进程池
    p = multiprocessing.Pool(3)
    # 4.2 将每个文件拷贝任务都添加到进程池-异步
    for file in file_list:
        # copy_file(src_path, dest_path, file)
        p.apply_async(copy_file, args=(src_path, dest_path, file))
    # 4.3 关闭进程池
    p.close()
    # 4.3 等待所有工作进程完成任务
    p.join()


if __name__ == '__main__':
    main()