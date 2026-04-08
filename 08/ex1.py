with open(r'/home/yosef/Desktop/base_pyton/empty.txt','w') as file_to_write:
    with open(r'/home/yosef/Desktop/base_pyton/not_empty.txt','r') as file_to_copy_from:
        for line in file_to_copy_from:
            file_to_write.write(line)
        
    
