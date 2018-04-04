'''
Created on 2017年6月8日

@author: Zhang Xiulong
'''
from tools.list_operation import read_list
def statistic_dict_size(dict_path):
    dict = read_list(dict_path)
    print('dict size:',len(dict))
    
    
if __name__ == '__main__':
    dict_path = "/result_data/word_table/meger_2.txt"
    statistic_dict_size(dict_path)