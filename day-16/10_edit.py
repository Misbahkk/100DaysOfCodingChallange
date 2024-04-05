# Edit the file
# we have multiple way to edit the file

# READ

file = open("example.txt",'r')
lines= file.readlines()
file.close()

# edit
# creet a list and add this list on write funtion
# lines = ["Hello\n","I am Misbah\n"]

# 2nd method to edit file to insert
# lines.insert(0,"Assalm alikum\n")

# lines[1] = "Hello Friend\n"

# Add last line \n
# lines[-1]= lines[-1]+"\n"
# # append in last last line
# lines.append('GoodBye!')

# write
file = open("Example.txt",'w')
file.writelines(lines)
file.close()







# challange Multipy all the number in number.txt by 2 an dprint the multipy number in 
# in number.txt

file_number = open("number.txt",'r')
lines = file_number.readlines()

file_number.close()

# Edit the file
for num in range(len(lines)):
    try: 
        number = float(lines[num])*2
        # rewrite the number that multipy with 2
        lines[num] = f'{number}\n'
    except Exception as e:
        pass

    


file_number = open("number.txt",'w')
file_number.writelines(lines)
file_number.close()