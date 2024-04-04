import sys


# bY sys.argv we get over file name and when we typr python file-name any input so the print the input
# try to run this code and unerstand whay happendd


# for argumnet in sys.argv:
#     print(argumnet)

# calculate the multiply of all inputs 

total = 1
del(sys.argv[0])
for  argumnet in sys.argv:
    try:
       number = int(argumnet)
       total*= number
    except Exception as e:
        print(e)
        print("Only Allow Integer numbers")
        # we canot take any argument 
        sys.exit(1)
print(total)