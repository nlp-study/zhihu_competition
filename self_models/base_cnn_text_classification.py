'''
Created on 2018年4月6日

@author: Administrator
'''
import tensorflow as tf
from numpy import shape

batch_size = 300
vocab_size =  300000
embedding_size = 250

class TextBaseCNN(object):
    '''
    classdocs
    '''
    def __init__(self, filter_sizes,num_filters,sequence_length,dropout_keep_prob,num_classes,l2_reg_lambda):
        self.input_x = tf.placeholder(tf.float32, [None,batch_size,None], "CNN_Input_x")
        self.input_y = tf.placeholder(tf.float32, [None,batch_size,None], "CNN_Input_y")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")
        l2_loss = tf.constant(0.0)
        self.dropout_keep_prob = dropout_keep_prob
        
        
        with tf.device('/cpu:0'), tf.name_scope("embedding"):
            self.W = tf.Variable(
                tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0),
                name="W")
            self.embedded_words = tf.nn.embedding_lookup(self.W, self.input_x)
            self.embedded_words_expanded = tf.expand_dims(self.embedded_words, -1)

        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            with tf.name_scope("base-cnn-maxpool-%s"%filter_size):
                #Convolution layer
                filter_shape = [filter_size,embedding_size,1,num_filters]
                W = tf.Variable(initial_value=tf.truncated_normal(filter_shape,stddev=0.1),name="W")
                b = tf.Variable(initial_value=tf.constant(0.1,shape=[num_filters]),name='b')
                conv = tf.nn.conv2d(self.embedded_words_expanded,
                            W,
                            strides=[1,1,1,1],
                            padding= "VALID",
                            name="conv")
                
                #active function
                h = tf.nn.relu(tf.nn.bias_add(conv,b), name="relu")
                # max pooling
                pooled = tf.nn.max_pool(h, 
                                        ksize=[1, sequence_length - filter_size + 1, 1, 1],
                                        strides=[1,1,1,1], 
                                        padding='VALID',
                                        name="pool")
                pooled_outputs.append(pooled)

        num_filters_total = num_filters*len(filter_size)
        self.h_pool = tf.concat(pooled_outputs, 3)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1,num_filters_total])
        
        #Add dropout
        with tf.name_scope('cnn-mlp-dropout'):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)
            
        
        # Final (unnormalized) scores and predictions
#         with tf.name_scope("output"):
#             W = tf.get_variable(
#                 "W",
#                 shape=[num_filters_total, num_classes],
#                 initializer=tf.contrib.layers.xavier_initializer())
#             b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name="b")
#             l2_loss += tf.nn.l2_loss(W)
#             l2_loss += tf.nn.l2_loss(b)
#             self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
#             self.predictions = tf.argmax(self.scores, 1, name="predictions")

        #Final (unnormalized) scores and prdictions
        with tf.name_scope("output"):
            W = tf.get_variable("W", 
                                shape=[num_filters_total,num_classes],
                                 initializer = tf.contrib.layers.xavier_initializer())
            b = tf.Variable(tf.concat(0.1,shape=[num_classes]),name="b")
            l2_loss += tf.nn.l2_loss(W)
            l2_loss += tf.nn.l2_loss(b)
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            self.predictions = tf.argmax(self.scores, 1, name="predictions")
            
#         # Calculate mean cross-entropy loss
#         with tf.name_scope("loss"):
#             losses = tf.nn.softmax_cross_entropy_with_logits(logits=self.scores, labels=self.input_y)
#             self.loss = tf.reduce_mean(losses) + l2_reg_lambda * l2_loss
# 
#         # Accuracy
#         with tf.name_scope("accuracy"):
#             correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y, 1))
#             self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")

            #Calcualte mean cross-entropy loss
            with tf.name_scope("losss"):
                losses = tf.nn.softmax_cross_entropy_with_logits( labels=self.input_y, logits=self.scores)
                self.loss = tf.reduce_max(losses) + l2_reg_lambda * l2_loss
                
            #Accuracy
            with tf.name_scope("accuracy"):
                correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_x,1))
                self.accuracy = tf.reduce_mean(tf.cast(correct_predictions,"float"),name="accuracy")

        
        
        
                
            
        