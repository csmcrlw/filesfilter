import os
import re

#папка, из которой нужно взять файлы
source_path = os.path.abspath(input('Source folder: ')) + '\\'

if os.path.exists(source_path):
#папка, куда нужно переместить файлы
    destination_path = os.path.abspath(input('Destination folder: ')) + '\\'
    if os.path.exists(destination_path):
        key_word = input('Key word (for example, python): ')
        filelist = os.listdir(source_path)
    #ищет указанные слова в названии файла вне зависимости от регистра
        regex = re.compile(key_word, re.IGNORECASE)
        for file in filelist:
            if re.search(regex, file):
                os.rename(source_path + file, destination_path + file)
        print('Successfully!')
    else:
        print('Destination folder does not exist!')
else:
    print('Source folder does not exist!')

