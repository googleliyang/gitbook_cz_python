def copy(file_name, target_path):
    f = open(file_name, 'r+')
    target_file = open(target_path, 'w+')
    while True:
        cont = f.read(1024)
        if cont == "":
            break
        target_file.write(cont)
    target_file.close()
    f.close()


copy('./copy_files/t.txt', './copy_files/copy_t.txt')
