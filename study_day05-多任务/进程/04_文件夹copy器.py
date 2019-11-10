"""
使用多进程copy文件夹

"""
from multiprocessing import Manager, Pool
import os


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("开始copy文件： %s 从%s ----> 到%s" % (file_name, old_folder_name, new_folder_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 复制完成，向q中设置文件
    q.put(file_name)


def main():
    # 获取用户copy文件夹的名字
    old_folder_name = input("请输入需要copu的文件夹名称：")
    # 创建新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except Exception as result:
        print(result)
    # 获取文件夹中的所有的文件名称 listdir()
    file_names = os.listdir(old_folder_name)
    # print(file_names)
    # 创建进程池
    pool = Pool(5)
    # 创建队列, 记录复制完成的文件
    q = Manager().Queue()

    # 向进程池中添加copy文件的任务
    for name in file_names:
        pool.apply_async(copy_file, (q, name, old_folder_name, new_folder_name))
    # 复制源文件夹中的文件到新文件夹中去

    pool.close()
    # pool.join()

    # 显示复制的百分比，通过Queue中的记录的文件数来计算
    ok_copy_file = 0
    all_file_num = len(file_names)
    while True:
        finsh_file = q.get()
        ok_copy_file += 1
        print("\r复制文件的完成百分比： %.2f %%" % (ok_copy_file * 100/ all_file_num), end="")
        if ok_copy_file >= all_file_num:
            break

    print()


if __name__ == '__main__':
    main()








