import os

os.chdir('./copy_files')

for i in os.listdir('./'):
    pos = i.index('.')
    os.rename(i, i[:pos] + '[qi]' + i[pos:])
