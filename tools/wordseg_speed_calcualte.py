'''
Created on 2017年6月5日

@author: Zhang Xiulong
'''
def calculate_speed(doc_size,cost_time):
    speed = 1.0 * doc_size / cost_time
    print('word seg speed is:',speed," M/s")
    
if __name__ == '__main__':
    print('***********finance word seg speed:******************')
    doc_size = 91.7
    cost_time = 66
    calculate_speed(doc_size,cost_time)
    
    