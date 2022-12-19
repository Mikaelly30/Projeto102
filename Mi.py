import os 
import shutil

from_dir = "C:/Users/User/Desktop/projetos Mikaelly/Aulas python/Aula102"
to_dir = "C:/Users/User/Desktop/projetos Mikaelly/Aulas python/102"

list_off_files = os.listdir(from_dir)
#print(list_off_files)

for file_name in list_off_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'mi-arrasa-no-py'
        path3 = to_dir + '/' + 'mi-arrasa-no-py' + '/' + file_name

        #print('path1', path1)
        #print('path3', path3)
        if os.path.exists(path2):
            print('movendo' + file_name + '...')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('movendo' + file_name + '...')
            shutil.move(path1, path3)
