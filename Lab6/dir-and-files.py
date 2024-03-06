import os
path = '/home/ruslan/Documents/Lab/PP2/Lab6/test.txt'
# print(os.listdir(path))

####################################################################################################

# print('existing:',os.access(path,os.F_OK))
# print('readeable:',os.access(path,os.R_OK))
# print('writttable:',os.access(path,os.W_OK))
# print('executtable:',os.access(path,os.X_OK))

####################################################################################################

# pat = input()
if os.access(path,os.F_OK):
    print(os.path.basename(path))
    print(os.path.dirname(path))

####################################################################################################

# with open('test.txt','w') as file:
#     file.write('something')

# with open('test.txt','r') as file:
#     print(len(file.readlines()))

####################################################################################################

# list = input().split()
# with open('test.txt','a') as file:
#     for i in list:
#         file.write('\n'+i)

####################################################################################################

# for i in range(26):
#     with open(f'./test/{chr(65+i)}.txt','w') as file:
#         file.write('txtfileeee')

####################################################################################################
        
# with open('test.txt','r') as file:
#     with open('test_copy.txt','w') as file1:
#         file1.write(file.read())

####################################################################################################
somepath = ''#path
# print('existing:',os.access(path,os.F_OK))
# if os.access(somepath,os.F_OK):
#     os.remove(somepath)