'''
Created on 2018年4月6日

@author: Administrator
'''
from tools.list_operation import *

def read_question_train_set(input_path,output_path):
    lines = read_list(input_path)
    iter_num = 0
    word_list = []
    for line in lines:
        iter_num += 1
        line_list = line.split()
        word = line_list[0]
        word_list.append(word)
        if iter_num%10000 == 0:
            print('iter_num:',iter_num)
    write_list(word_list,output_path)
    
def build_word2id(input_path):
    lines = read_list(input_path)
    iter_num = 0
    word2id_map = {}
    for line in lines:
        iter_num += 1
        line_list = line.split()
        word = line_list[0]
        word2id_map[word] = iter_num
        if iter_num%10000 == 0:
            print('iter_num:',iter_num)
    return word2id_map
    

if __name__ == '__main__':
    input_path = "I:/competition/zhihu/data/ieee_zhihu_cup/word_embedding.txt"
    output_path = "../data/word2id.txt"
    read_question_train_set(input_path,output_path)