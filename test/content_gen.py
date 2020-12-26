import os, pathlib
#
def take_out_lst_dir(root):
    rt = root[root.rfind('/') + 1:len(root) + 1]
    return rt

def get_caption(str):
    txt = open(str, 'r')
    caption = ''
    for st in txt:
        if st.find('=') == 0:
            for lt in st:
                if lt != '=':
                    caption = caption + lt
            break
    caption = caption.strip()
    if len(caption) > 0:
        return (caption)
    else:
        return ('no caption here')


def content_string(str, root):
    caption = get_caption(str)
    # print('caption is : '+caption)
    str = str[1:len(str) + 1]
    str = str[1:len(str) - 4]
    str = str.replace('/', ':')
    ind = 1
    for lt in str:
        if lt == ':':
            ind = ind + 1
    str = '  * [[' + str + '|' + caption + ']]'
    while ind > 0:
        str = ' ' + str
        ind = ind - 1
    return str

def content_cat(root):
    str = ''
    dir = take_out_lst_dir(root) # return last dir
    sp = root.count('/') # counts number of '/'
    str = root[2:len(root) + 1] # remove './' in the beginning of the path
    str = str.replace('/', ':')
    start_txt = pathlib.Path(root+'/start.txt')
    if start_txt.is_file():
        str = '  * [[' + str +':start'+ '|' + dir + ']]'
    else:
        str = '  * ' + dir
    while sp > 0:
        str = ' ' + str
        sp = sp - 1
    return  str

def take_out_lst_dir(root):
    rt = root[root.rfind('/') + 1:len(root) + 1]
    return rt

def list_dir(initial_dir, f):
    os.chdir(initial_dir)
    root_str = ''
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print('root is '+root)
            print('root_str is '+root_str)
            if root != root_str: # than write new category in content
                   if len(root) > 1:
                       cat = content_cat(root)
                       if len(cat) > 0:
                           f.write(cat+'\n')
            if name != 'start.txt':
                str = os.path.join(root, name)
                # print(str)
                if len(root) > 1:
                    rt = take_out_lst_dir(root)
                else:
                    rt = take_out_lst_dir(initial_dir)
                str = (content_string(str, rt))
                f.write(str + '\n')
            root_str = root


f = open('./pages_list.txt', 'w')
initial_dir = './wiki1.itms.su/docs/data/pages'
list_dir(initial_dir, f)
f.close()
