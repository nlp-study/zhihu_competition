'''
Created on 2017年8月25日

@author: Zhang Xiulong
'''
from tools.list_operation import *

def compare_list(input_1_path,input_2_path):
    dict_1_list = read_list(input_1_path)
    dict_2_list = read_list(input_2_path)
    
#     dict_1_word_list = [x.split('\t')[0] for x in dict_1_list]
#     dict_2_word_list = [x.split('\t')[0] for x in dict_2_list]
    
    dict_1_word_set = set(dict_1_list)
    dict_2_word_set = set(dict_2_list)
    
    
    additive_words = dict_1_word_set - dict_2_word_set
    lack_words = dict_2_word_set - dict_1_word_set
    
    
    additive_words = list(additive_words)
    lack_words = list(lack_words)
    
    
    additive_words.sort()
    lack_words.sort()
    
    write_list(additive_words,'../../result_data/dictionary_compare/additive_words.txt')
    write_list(lack_words,'../../result_data/dictionary_compare/lack_words.txt')
    
    print('additive_words size:',len(additive_words))
    print('lack_words size:',len(lack_words))
    
    
if __name__ == '__main__':
#     input_1_path = 'E:/formal_project_java/word_seg/word_seg_module/nlp-seg/src/main/resources/data/finance_dictionary/CoreNatureFinanceDictionary.ngram.txt'
    
#     input_1_path = '../../result_data/build_word_bank_dictionary/CoreNatureFinanceDictionary.ngram.txt'
#     input_2_path = '../../result_data/build_word_bank_dictionary/raw_bigram.txt'
#     input_1_path = 'E:/formal_project_java/word_seg/word_seg_module/nlp-seg/src/main/resources/data/finance_dictionary/CoreNatureFinanceDictionary.ngram.txt'
#     input_2_path = '../../result_data/build_word_bank_dictionary/CoreNatureFinanceDictionary.ngram1.txt'
#     input_2_path = 'C:/Users/Administrator/Downloads/bigram.txt'
    
     
#     input_1_path = 'E:/formal_project_java/word_seg/word_seg_module/nlp-seg/src/main/resources/data/finance_dictionary/CoreFinanceDictionary.txt'
    input_1_path = '../../result_data/build_word_bank_dictionary/CoreFinanceDictionary.txt'
    input_2_path = '../../result_data/build_word_bank_dictionary/raw_data.txt'
#     input_2_path = '../../result_data/build_word_bank_dictionary/raw_data_old.txt'
#     input_2_path = 'E:/formal_project_java/word_seg/workspace/build_dictionary/data/CoreFinanceDictionary.txt'
#     input_2_path = 'C:/Users/Administrator/Downloads/divided.txt'
    
#     input_2_path = 'E:/temp/ubuntu_machine/workspace/Java/word_seg/word_seg_preprocess/result_data/build_word_bank_dictionary/CoreFinanceDictionary.txt'
    compare_list(input_1_path,input_2_path)
    
    