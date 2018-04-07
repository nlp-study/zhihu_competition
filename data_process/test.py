'''
Created on 2018��4��6��

@author: Administrator
'''
from tools.list_operation import read_list, write_list

def read_question_train_set(input_path):
    lines = read_list(input_path)
    iter_num = 0
    for line in lines:
        iter_num += 1
#         line_list = line.split('\t')
#         print(line_list)
#         if iter_num == 10:
#             exit()
    print("iter_num:",iter_num)
            
            
def read_question_topic_train(input_path):
    lines = read_list(input_path)
    iter_num = 0
    for line in lines:
        iter_num += 1
#         line_list = line.split('\t')
#         print(line_list)
#         if iter_num == 10:
#             exit()
    print("iter_num:",iter_num)
    
def word_statistic(input_path,output_path):
    all_word_set = set()
    all_word_list= []
    line_num  = 0
    corpus_list = read_list(input_path)
    for line in corpus_list:
        line_num += 1
        line_list = line.split("\t")
        id = line_list[0]
        title = line_list[1]
        new_line = title
        if len(line_list) == 3:
            content = line_list[2]
            new_line = title + ","+content
        new_line_list = new_line.split(',')
        all_word_list  += new_line_list
#         print('new_line_list:',new_line_list)
       
        if len(all_word_list) > 10000:
            temp_word_set = set(all_word_list)
            all_word_set =  all_word_set | temp_word_set
            all_word_list = []
        
        if line_num%10000 == 0:
            print("line_num:",line_num)
    
    all_word_list = list(all_word_set)
    all_word_list = [int(i.replace("w",""))  for i in all_word_list if 'w' in i]
    all_word_list.sort()
    print('all_word_list size:',len(all_word_list))
    write_list(all_word_list,output_path)

def word_embeding_statistic(input_path):
    lines = read_list(input_path)
    iter_num = 0
    for line in lines:
        iter_num += 1
#         line_list = line.split('\t')
        print(line)
        if iter_num == 10:
            exit()
    print("iter_num:",iter_num)
            
if __name__ == '__main__':
#     input_path = "I:/competition/zhihu/data/ieee_zhihu_cup/question_train_set.txt"
#     read_question_train_set(input_path)
#     
#     question_topic_train_path = "I:/competition/zhihu/data/ieee_zhihu_cup/question_topic_train_set.txt"
#     read_question_topic_train(question_topic_train_path)
    
#     input_path = "../data/question_train_word_corpus.txt"
#     output_path = "../data/word_id_statistic.txt"
#     word_statistic(input_path,output_path)
    
    
    word_embeding_path = "I:/competition/zhihu/data/ieee_zhihu_cup/word_embedding.txt"
    word_embeding_statistic(word_embeding_path)
    
    
    