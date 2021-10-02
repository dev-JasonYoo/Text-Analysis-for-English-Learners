import re
import openpyxl
from nltk.stem import WordNetLemmatizer, PorterStemmer

def analyze(text_file): #should be in format "title.txt"
    rawf = open(text_file, "r")
    raw_txt = rawf.read() #string data of whole text
    raw_txt = raw_txt.lower() #all capital letters to small letters

    text_list = re.split("\W", raw_txt) #list of constituent words
    text_list = list(filter(lambda x: x != "", text_list)) #deletes empty strings
    
    lm = WordNetLemmatizer()
    lm_txt = [lm.lemmatize(word, pos="v") for word in text_list] #lemmatized text
    
    ps = PorterStemmer()
    st_txt = [ps.stem(word = word) for word in lm_txt] #stemmed text
    
    # lem = open("lem.txt", "w") #save lm_txt as txt file
    # for w in text_list:
    #     lem.write(w+"\n")
    # lem.close()
    
    # st = open("st.txt", "w") #save st_txt as txt file
    # for w in text_list:
    #     st.write(w+"\n")
    # st.close()
    
    # diff = open("diff.txt", "w") #save differences PorterStemmer made between lm_txt and st_txt as txt file
    # for i in range(len(lm_txt)):
    #     if lm_txt[i] != st_txt[i]:
    #         diff.write(lm_txt[i] + " " + st_txt[i] + "\n")
    # diff.close()
            

    wb = openpyxl.Workbook() #new workbook
    ws = wb.active

    freq = {} #dictionary that contains words and corresponding frequencies
    count = 0 #index of lm_txt
    for stem in st_txt:
        if freq.get(stem) == None: #if the stem isn't initialized yet, initialize it by 0.
            freq[stem] = {lm_txt[count] : 0}
        elif freq[stem].get(lm_txt[count]) == None: #if the word isn't initialized yet, initialize it by 0.
            freq[stem][lm_txt[count]] = 0
        
        freq[stem][lm_txt[count]] += 1 #new detection, plus one for frequency
        count += 1
        
    
    row = 1 #index of freq
    for stem, words in freq.items():
        ws.cell(row = row, column = 1).value = stem #the first column with stems
        for word, frequency in freq[stem].items():
            ws.cell(row = row, column = 2).value = word #the second column with words, multiple if needed
            ws.cell(row = row, column = 3).value = frequency #the third column with corresponding frequencies    
            row += 1

    wb.save(filename = f"result_{text_file[:-4]}.xlsx") #save the result worksheet
    wb.close()
    rawf.close()

    return 0

if __name__ == "__main__":
    analyze("The_Great_Gatsby.txt")