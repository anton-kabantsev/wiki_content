import os, pathlib

class dir_content_gen(object):
    def __init__(self, initial_dir, path_to_file, depth):
        ''' генератор содержания докувики
            на вход подаем:
            1. initial_dir - начальный каталог от которого будет делаться содержание
            2. path_to_file - файл куда писать содержание
            3. depth - тип int глубина вложенности
        '''
        print('class_ready')
        self.initial_dir = initial_dir
        self.path_to_file = path_to_file
        self.depth = depth

    def take_out_lst_dir(self, root):
        '''Возвращает последнюю директорию из пути'''
        rt = root[root.rfind('/') + 1:len(root) + 1]
        return rt

    def get_caption(self, str):
        '''Получает заголовок отмеченный === === из текстового файла'''
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
            return caption
        else:
            return 'no caption here'

    def content_string(self, str, root):
        '''Возвращает строку содержания с отступами'''
        caption = self.get_caption(str)
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
            str = '  ' + str
            ind = ind - 1
        return str

    def content_cat(self, root):
        '''Возвращает строку содержания с корневым каталогом'''
        str = ''
        dir = self.take_out_lst_dir(root)  # return last dir
        sp = root.count('/')  # counts number of '/'
        str = root[2:len(root) + 1]  # remove './' in the beginning of the path
        str = str.replace('/', ':')
        start_txt = pathlib.Path(root + '/start.txt')
        if start_txt.is_file():
            str = '  * [[' + str + ':start' + '|' + dir + ']]'
        else:
            str = '  * ' + dir
        while sp > 0:
            str = '  ' + str
            sp = sp - 1
        return str

    def list_dir(self, initial_dir, f):
        '''Итерируется по дереву папок, находит txt и пишет файл'''
        os.chdir(initial_dir)
        root_str = ''
        for root, dirs, files in os.walk(".", topdown=True):
            for name in files:
                #print('root is ' + root)
                #print('root_str is ' + root_str)
                if root != root_str:  # than write new category in content
                    if len(root) > 1:
                        cat = self.content_cat(root)
                        if len(cat) > 0:
                            f.write(cat + '\n')
                if name != 'start.txt':
                    str = os.path.join(root, name)
                    # print(str)
                    if len(root) > 1:
                        rt = self.take_out_lst_dir(root)
                    else:
                        rt = self.take_out_lst_dir(initial_dir)
                        str = (self.content_string(str, rt))
                        f.write(str + '\n')
                        root_str = root
    def start_work(self):
        print('class is working')
        fileC = open(self.path_to_file,'w')
        print(fileC)
        self.list_dir(self.initial_dir, fileC)
        fileC.close()
