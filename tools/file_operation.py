'''
Created on 2016年6月21日

@author: Zhang Xiulong
'''
import shutil 
import os

def copy_file(source_file,target_file):
    if not os.path.exists(source_file):
        print('copy file failure,source file is not exist!')
    shutil.copy(source_file,  target_file)
    
def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  

def clear_folder(input_folder):
    import shutil  
    filelist=os.listdir(input_folder)  
    for f in filelist:  
        filepath = os.path.join(input_folder, f )  
        if os.path.isfile(filepath):  
            os.remove(filepath)  
        elif os.path.isdir(filepath):  
            shutil.rmtree(filepath,True)  
        
     
if __name__ == '__main__':
#     source_file = 'd:/test.txt'
#     target_file = 'd:/test_1.txt'
#     copy_file(source_file,target_file)
    
    input_folder = 'D:/temp/打标签原型'
    clear_folder(input_folder)