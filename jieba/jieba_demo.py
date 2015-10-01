# encoding=utf-8
import jieba

jieba.set_dictionary("./dict.txt.big")

while True:
    sentence = input("Enter the sentence: ")
    seg_list = jieba.cut(sentence)
    print("斷字結果：" + "/ ".join(seg_list)) 

