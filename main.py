import re
import openpyxl

rawf = open("The_Great_Gatsby.txt", "r")
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

wb.save(filename = "result.xlsx") #save the result worksheet
wb.close()
rawf.close()