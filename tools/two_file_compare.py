'''
Created on 2017年12月7日

@author: Zhang Xiulong
'''
from tools.list_operation import read_list, write_list
def compare_file(file_1_path,file_2_path):
    corpus_list_1 = read_list(file_1_path)
    corpus_list_2 = read_list(file_2_path)
    md5_1_set = set()
    md5_2_set = set()
    
    for line in corpus_list_1:
        line_list = line.split('\t')
        if len(line_list) == 2:
            if len(line_list[0]) == len('22d68441d949b94907c41309ffbf01b1'):
                md5_1_set.add(line_list[0])
            
    for line in corpus_list_2:
        line_list = line.split('\t')
        if len(line_list) == 2:
            if len(line_list[0]) == len('22d68441d949b94907c41309ffbf01b1'):
                md5_2_set.add(line_list[0])
            
            
    additive_set = md5_2_set - md5_1_set
    lack_set =  md5_1_set - md5_2_set 
    
    
    print('additive_set size:',len(additive_set))
    print('lack_set size:',len(lack_set))
    write_list(list(additive_set),'../../result_data/temp/additive_set.txt')
    write_list(list(lack_set),'../../result_data/temp/lack_set.txt')
        

if __name__ == '__main__':
    file_1_path = '../../result_data/name_classification/new_fix_tag_compare_result/positive_compare_result.txt'
    file_2_path = '../../result_data/name_classification_result/me_new_fix_seg_result.txt'
    compare_file(file_1_path,file_2_path)
    
    
    
    