import sys


todo = []
try:
    file = open("TO-Do-List.txt","r")
    todo = file.readlines()
    file.close()
except:
    pass

print(todo)


# Add
if len(sys.argv) >= 3 and sys.argv[1].lower() =="add":
    todo.append(f"{sys.argv[2]}\n")

print(todo)

# Remove
if len(sys.argv) >= 3 and sys.argv[1].lower() =="remove":
    try:
        index_to_delete = int(sys.argv[2])
        if index_to_delete>0:
            index_to_delete -=1
            del(todo[index_to_delete])
        else:
            print("Wring Number")

    except Exception as e:
        print(e)
        sys.exit[1]
    


print(todo)


# # Mark as completed 
# if len(sys.argv) >= 3 and sys.argv[1].lower() =="mark as completed":
#     try:
#         take_num = int(sys.argv[2])
#         if take_num>0 and take_num<=len(todo):
            
#             todo.append(f"{todo[take_num-1]} - Completed")

#     except:
#         pass


file = open("TO-Do-List.txt","w")
file.writelines(todo)
file.close()



# Print the todo list

if len(todo) == 0:
    print("*****Your To DO List is empty*****")
else:
    print("This IS Your To Do List")
    for x in range(len(todo)):
        print(f"{x + 1}. {todo[x]}")
