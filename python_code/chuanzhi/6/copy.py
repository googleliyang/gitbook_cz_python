def copy(file_name, target_path):
    f = open(file_name, 'r+')
    cont = f.read()
    target_file = open(target_path, 'w+')
    target_file.write(cont)
    target_file.close
    f.close()


copy('./copy_files/t.txt', './copy_files/copy_t.txt')
