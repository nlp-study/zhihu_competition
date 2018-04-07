'''
Created on 2018年4月7日

@author: Administrator
'''
from tools.list_operation import *


def build_topic2id_file(input_path,output_path):
    lines = read_list(input_path)
    iter_num = 0
    topic_list = []
    for line in lines:
        iter_num += 1
        line_list = line.split()
        word = line_list[0]
        topic_list.append(word)
        if iter_num%10000 == 0:
            print('iter_num:',iter_num)
    write_list(topic_list,output_path)
    print("topic_list size:",len(topic_list))
    
def build_topic2id(input_path):
    lines = read_list(input_path)
    iter_num = 0
    topic2id_map = {}
    for line in lines:
        line_list = line.split("\t")
        title = line_list[0]
        topic2id_map[title] = iter_num
        iter_num += 1
    print('topic2id_map size:',len(topic2id_map))
    return topic2id_map

def build_sentence_topic_id_corpus(question_topic_train_path,topic_info_path,output_path):
    topic2id_map = build_topic2id(topic_info_path)
    train_topic_id_list = []
    lines = read_list(question_topic_train_path)
    for line in lines:
        line_list = line.split('\t')
        id = line_list[0]
        topic_line = line_list[1]
        topic_list = topic_line.split(',')
        topic_id_list = [str(topic2id_map[i]) for i in topic_list if i in topic2id_map]
        new_line = id + '\t' + ' '.join(topic_id_list)
        train_topic_id_list.append(new_line)
    write_list(train_topic_id_list, output_path)
    

if __name__ == '__main__':
    input_path = "I:/competition/zhihu/data/ieee_zhihu_cup/topic_info.txt"
    output_path = "../data/topic_info2id.txt"
#     build_topic2id_file(input_path,output_path)
    
    
    question_topic_train_path = "I:/competition/zhihu/data/ieee_zhihu_cup/question_topic_train_set.txt"
    topic_info_path = "I:/competition/zhihu/data/ieee_zhihu_cup/topic_info.txt"
    output_path = "../data/question_topic_train_id.txt"
    build_sentence_topic_id_corpus(question_topic_train_path,topic_info_path,output_path)
    