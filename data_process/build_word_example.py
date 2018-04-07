'''
Created on 2018年4月7日

@author: Administrator
'''
import os
from tools.list_operation import read_list, write_list
import codecs
from data_process.word2id import build_word2id

def read_question_train_set(input_folder,output_path):
    train_set_path = input_folder + os.sep + "question_train_set.txt"
    iter_num = 0
    new_line_list = []
    with codecs.open(train_set_path,'r',"utf-8") as read_file:
        for line in read_file:
            iter_num += 1
            line_list = line.split('\t')
            topic_id = line_list[0]
            title = line_list[2]
            content = line_list[4]
            if len(title) > 0:
                content = content.strip()
                new_line = topic_id + '\t' + title +'\t' + content
                new_line_list.append(new_line)
#             if len(line_list) != 5:
#                 print('line:',line)
#                 exit()
                
    print("iter_num:",iter_num)
    print("new_line_list size:",len(new_line_list))
    write_list(new_line_list,output_path)
    
def transform_title_2_id_corpus(word_embeding_path,input_corpus,output_corpus_path):
    word2id_map = build_word2id(word_embeding_path)
    iter_num = 0
    title_id_corpus_list = []
    with codecs.open(input_corpus,'r',"utf-8") as read_file:
        for line in read_file:
            line_list = line.split('\t')
            topic_id = line_list[0]
            title = line_list[1]
            title_list = title.split(',')
            title_id_list = [str(word2id_map[i]) for i in title_list if i in word2id_map]
            new_line = topic_id + '\t' + ' '.join(title_id_list)
            title_id_corpus_list.append(new_line)
            iter_num += 1
    print("iter_num:",iter_num)
    print("title_id_corpus_list size:",len(title_id_corpus_list))
    write_list(title_id_corpus_list,output_corpus_path)
    
def build_train_corpus(corpus_path,label_path,output_x_path,output_y_path):
    input_x_list = []
    input_y_list = []
    
    label_list = read_list(label_path)
    corpus_id_topic_map = {}
    for line in label_list:
        line_list = line.split('\t')
        topic_id = line_list[0]
        topic_id_line = line_list[1]
        corpus_id_topic_map[topic_id] = topic_id_line
    print('corpus_id_topic_map size:',len(corpus_id_topic_map))
    
    iter_num = 0
    with codecs.open(corpus_path,'r',"utf-8") as read_file:
        for line in read_file:
            iter_num += 1
            line_list = line.split('\t')
            topic_id = line_list[0]
            title_id_line = line_list[1]
            if topic_id in corpus_id_topic_map:
                title_id_line = title_id_line.strip()
                input_x_list.append(title_id_line)
                input_y_list.append(corpus_id_topic_map[topic_id])
    write_list(input_x_list,output_x_path)
    write_list(input_y_list,output_y_path)
    print('input_x_list size:',len(input_x_list))
    print('input_y_list size:',len(input_y_list))
    

            
if __name__ == '__main__':
    input_folder = "I:/competition/zhihu/data/ieee_zhihu_cup"
    output_path = "../data/question_train_word_corpus.txt"
#     read_question_train_set(input_folder,output_path)
    
    
    word_embeding_path = "I:/competition/zhihu/data/ieee_zhihu_cup/word_embedding.txt"
    input_corpus = "../data/question_train_word_corpus.txt"
    topic_info_path = "I:/competition/zhihu/data/ieee_zhihu_cup/topic_info.txt"
    question_topic_train_path = "I:/competition/zhihu/data/ieee_zhihu_cup/question_topic_train_set.txt"
    output_corpus_path = "../data/question_train_title_id_corpus.txt"
    transform_title_2_id_corpus(word_embeding_path,input_corpus,output_corpus_path)
    
    
    
    corpus_path = "../data/question_train_title_id_corpus.txt"
    label_path = "../data/question_topic_train_id.txt"
    output_x_path = "../data/title_id.txt"
    output_y_path = "../data/label_id.txt"
    build_train_corpus(corpus_path,label_path,output_x_path,output_y_path)
    
    
    
    