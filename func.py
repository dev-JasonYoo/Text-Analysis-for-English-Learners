import os
from zipfile import ZipFile
import main
import re

def analyze_epub(file_name):
    os.rename('%s' % file_name, file_name[:-4] + "zip")
    with ZipFile(file_name[:-4] + "zip") as zip:
        zip.extractall(file_name[:-4])

    dir = './%s/OEBPS/' % file_name[:-4]

    def is_html(file_name):
        if file_name[-4:] == 'html':
            return True
        else:
            return False

    file_list = list(filter(is_html, os.listdir('./%s/OEBPS' % file_name[:-4])))
    file_list.sort()
    print(file_list)

    for file in file_list:
        if file[-4:] == "html":
            print(file)
            os.rename(dir + file, dir + file[:-4]+'txt')
            file_list[file_list.index(file)] = file[:-4]+'txt'

    file_list = list(map(lambda x: dir + x, file_list))

    print('.......')
    for file in file_list:
        print(file)
    print('.......')

    # html to plain text
    for file in file_list:
        with open(file, 'r') as target:
            orig_text = target.read()

        with open(file, 'w') as target:
            orig_text = target.write(re.sub("<[^<>]*>","",orig_text))

    destination = re.sub(dir, "", file_list[0])
    print(file_list[0])

    with open(destination, "a+") as merged:
        for file in file_list:
            with open(file) as f:
                merged.write(f.read())

    with os.popen("rm -rf %s" % file_name[:-4]) as p:
        pass

    main.analyze(destination)
    
if __name__ == '__main__':
    analyze_epub("pg64317.epub")