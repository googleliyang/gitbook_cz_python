from gevent import monkey
# monkey.patch_all()
import urllib.request
import gevent
import time


def down_img(url):
    """协程函数  下载一张图片"""
    # 2.1 从URL中切割出 图片名称
    "https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/10/2694864718ef0772c36712cd0e12e3a7_big.jpg"
    file_name = url[url.rfind('/')+1:]
    print("图片:%s开始下载" % file_name)
    # 2.2 发起图片下载请求
    response = urllib.request.urlopen(url)

    # 3.3 打开文件  将响应数据写入图片文件中
    with open(file_name, "wb") as file:
        file.write(response.read())
    print("图片:%s下载完成" % file_name)
def main():
    begin = time.time()
    # 1 准备需要下载的图片的网址
    img_list = ["https://rpic.douyucdn.cn/live-cover/roomCover/2018/08/15/a0c1206ae5da0c02a677506af9f41c40_big.jpg",
                "https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/10/2694864718ef0772c36712cd0e12e3a7_big.jpg",
                "https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/17/bb4429f6cc2c517a8862606c54ee3d7c_big.jpg"]
    # 2 创建协程 下载一张图片  down_img(img_list[0])
    # down_img(img_list[1])
    # down_img(img_list[2])
    g1 = gevent.spawn(down_img, img_list[0])
    g2 = gevent.spawn(down_img, img_list[1])
    g3 = gevent.spawn(down_img, img_list[2])

    # 3 等待所有任务执行完成
    gevent.joinall([g1, g2, g3])
    end = time.time()
    print("总共花费了%f秒" % (end-begin))
if __name__ == '__main__':
    main()