'''
Created on Feb 17, 2017

@author: zhang
'''
from tools.list_operation import *

import random

def select_words(original_dict_path,word_size,output_path):
    original_dict_list = read_list(original_dict_path)
    sample_set = set()
    
    while True:
        index = random.randint(0, len(original_dict_list))
        sample_set.add(original_dict_list[index])
        if len(sample_set) > word_size:
            break;
    
    sampe_word_list = list(sample_set)
    sampe_word_list = [x.split("\t")[0] for x in sampe_word_list]
    sampe_word_list.sort()
    write_list(sampe_word_list,output_path)
    print('sample end')
    

if __name__ == '__main__':
    original_dict_path = '../../result_data/merge_dictionary/CoreFinanceDictionary.txt'
    word_size = 200000
    output_path = "../../result_data/temp/sample_words.txt"
    select_words(original_dict_path,word_size,output_path)
    
    