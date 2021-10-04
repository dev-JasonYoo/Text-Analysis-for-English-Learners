from func import *

def analyze(file_name):
    extension = file_name.split('.')[-1]

    if extension == 'txt':
        analyze_txt(file_name)
    
    if extension == 'epub':
        analyze_epub(file_name)
    
    if extension == 'pdf':
        analyze_pdf(file_name)
    
    return 0

if __name__ == "__main__":
    analyze("pg64317.epub")