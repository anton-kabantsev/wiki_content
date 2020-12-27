import os, content_gen

def read_dir(initial_dir):
    os.chdir(initial_dir)
    dct = {}
    ind = 1
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            if name == 'start.txt':
                #print(name+' ind = '+str(ind))
                dct[ind] = os.path.join(root, name)
                ind = ind + 1
    return(dct)

initial_dir = '/home/h902118933/wiki1.itms.su/docs/data/pages'
dct = read_dir(initial_dir)
ind = 1
while True:
  path_to_file = dct.get(ind)
  if path_to_file == None:
    break
  else:
    lst_ind = path_to_file.rfind('/')
    dir = path_to_file[0:lst_ind]
    #print(dir)
    #print(path_to_file+'_test')
    gen = content_gen.dir_content_gen(initial_dir+'/'+dir, initial_dir+'/'+dir+'/test.txt', 2)
    gen.start_work()
    #print(dir)
  ind = ind + 1