import os
initial_dir = '/home/h902118933/wiki1.itms.su/docs/data/pages'
os.chdir(initial_dir)
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if name == 'test.txt':
            print('removed '+os.path.join(root, name))
            os.remove(os.path.join(root, name))
