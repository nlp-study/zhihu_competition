'''
Created on 2018年4月7日

@author: Administrator
'''
import numpy as np
from tools.list_operation import read_list
padd_word_id = 411721
sentence_len = 120
batch_size = 100
label_size = 1999


def select_cropus(input_corpus_path,input_label_corpus_path,data_size):
    corpus_list = read_list(input_corpus_path)
    label_list = read_list(input_label_corpus_path)
    
    corpus_list = corpus_list[:data_size]
    label_list = label_list[:data_size]
    
    raw_corpus_list = [i.split() for i in corpus_list]
    raw_label_list = [i.split() for i in label_list ]
    
    
    padd_corpus_list = padd_corpus(raw_corpus_list)
    processed_label_list = process_y(raw_label_list)
    
    raw_corpus_array = np.array(padd_corpus_list)
    raw_label_array = np.array(processed_label_list)
    
    shuffle_indices = np.random.permutation(np.arange(data_size))
    
    corpus_array = raw_corpus_array[shuffle_indices]
    labels_array = raw_label_array[shuffle_indices]
    
    train_size = int(data_size*0.9)
    print('data_size:',data_size)
    print('train_size:',train_size)
    
    train_corpus_array = corpus_array[:train_size]
    train_labels_array = labels_array[:train_size]
    eval_corpus_array = corpus_array[train_size:]
    eval_labels_array = labels_array[train_size:]
    
    return train_corpus_array,train_labels_array,eval_corpus_array,eval_labels_array
    
    
    
def padd_corpus(raw_corpus_list):
    padd_corpus_list = []
    for temp_list in raw_corpus_list:
        new_list = temp_list
        if len(temp_list) < sentence_len:
            new_list += [padd_word_id]*(sentence_len-len(temp_list))
        else:
            new_list = temp_list[:sentence_len]
        padd_corpus_list.append(new_list)
    return padd_corpus_list

def process_y(raw_label_list):
    y_list = []
    for i in range(len(raw_label_list)):
        temp_list = [0]*label_size
        topic_id = raw_label_list[i][0]
        topic_id = int(topic_id)
        temp_list[topic_id] = 1
        y_list.append(temp_list)
    return y_list


def generate_batch(input_x,input_y):
    data_size = len(input_x)
    num_batches_per_epoch = int((data_size-1)/batch_size) + 1
    
    for batch_num in range(num_batches_per_epoch):
        start_index = batch_num * batch_size
        end_index = min((batch_num + 1) * batch_size, data_size)
        yield input_x[start_index:end_index],input_y[start_index:end_index]
    

input_corpus_path = "../data/title_id.txt"
input_label_corpus_path  = "../data/label_id.txt"
data_size = 300000
train_corpus_array,train_labels_array,eval_corpus_array,eval_labels_array = select_cropus(input_corpus_path,input_label_corpus_path,data_size)


