import re
import openpyxl

def analyze(text_file): #should be in format "title.txt"
    rawf = open(text_file, "r")
    raw = rawf.read() #string data of whole text
    raw = raw.lower() #all capital letters to small letters

    text_list = re.split("\W", raw) #list of constituent words
    text_list = list(filter(lambda x: x != "", text_list)) #deletes empty strings

    wb = openpyxl.Workbook() #new workbook
    ws = wb.active

    freq={} #dictionary that contains words and corresponding frequencies
    for word in text_list:
        if freq.get(word) == None: #if the word isn't checked yet, initialize it with a frequency of 1
            freq[word] = 1
        freq[word] += 1 #new detection, plus one for frequency

    row = 1
    for word, freq in freq.items():
        ws.cell(row = row, column = 1).value = word #left column with words
        ws.cell(row = row, column = 2).value = freq #right column with corresponding frequencies
        row += 1

    wb.save(filename = f"result_{text_file[:-4]}.xlsx") #save the result worksheet
    wb.close()
    rawf.close()

    return 0

if __name__ == "__main__":
    analyze("The_Great_Gatsby.txt")