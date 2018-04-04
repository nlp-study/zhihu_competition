'''
Created on 2017年8月31日

@author: Zhang Xiulong
'''
import re

def re_test1():
    lines = ["029 88457890","02988457890","(029)88457890","029-88457890","029-8845-7890"]
    for line  in lines:
        pattern = re.compile('[\(]?0[1-9]\d{1,3}[\(]?[-]?[2-9]\d{2,3}[-])?\d{4}')
        match = pattern.match(line)
        if match:
            print('true')
        else:
            print('false')
            
            
def re_test2():
    lines = ["<H1> this  is a </H1>"]
    for line  in lines:
        pattern = re.compile('<(.*?)</(.*?)>')
        match = pattern.match(line)
        if match:
            print('true')
        else:
            print('false')
            
            
def re_test3():
    lines = ["110104199901011274","11010419990101925x","31010419950101849x","140424196401019716","320311770706001"]
    for line  in lines:
        pattern = re.compile('(^\d{18}$)|(^\d{17}(\d|X|x)$)/')
        match = pattern.match(line)
        if match:
            print('true')
        else:
            print('false')
            
if __name__ == '__main__':
    re_test3()   
    
    
    