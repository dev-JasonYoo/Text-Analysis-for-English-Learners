import re

rawf = open("The_Great_Gatsby_short.txt", "r")
raw = rawf.read()
raw = raw.lower()

# text_list = re.findall("\W", raw)
# for i in text_list:
#     print(i)

text_list = re.split("\W", raw)
text_list = list(filter(lambda x: x != "", text_list))

for i in text_list:
    print(i)

result = open("result.txt", "w")

freq={}
for word in text_list:
    if freq.get(word) == None:
        freq[word] = 1
    freq[word] += 1
    result.write(f"{word} {freq[word]}\n")

result.close

ref = open("re_text.txt", "w")
for i in text_list:
    ref.write(i+" ")
ref.close()