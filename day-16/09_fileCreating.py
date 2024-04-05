import sys


# # only crete the file 1 time 
# # try to again run it crete error file is exit
# file = open("Example.txt","x")

# file.write("Try to X function")

# file.close()


# # crete a file if file is not creted before and then overwrite
# file = open("Example.txt","w")
# file.write("Over write on file!")
# file.close()


# # Append the text
# file = open("Example.txt","a")
# file.write("Add the text! ")
# file.close()


file_name = sys.argv[1]

file = open(file_name,'w')
file.write("happy")
file.close()


# Read the file

# file = open("Example.txt",'r')

# file_text = file.read()
# print(file_text)

# file_text = file.readlines()
# print(file_text)





# Challange: crete a file number.txt and dtore a number
# multiply each number togather and print them

# f = open("number.txt",'w')
# f.write("1\n2\n3\n4\n5")
# f.close()

# f= open("number.txt",'r')

# mul =1
# for text in f:
#     try:
#         text=int(text)
#         mul*=text
#     except Exception as e:
#         pass
# print(mul)

# f.close


# 