"""3. Create a dictionary that maps words to their lengths in a given sentence, 
but with the following limitations:
Students cannot use any string splitting functions (e.g., split())."""


def map_words(sentance):
    dic = {}
    word = ""
    for char in sentance:
        if char == " " or char == '.':
           if word !="":
                
                dic[word] = len(word)
                print(dic)
                print(word)
                word=""

        else:
            word+=char
            print(word)
    
    if word!="":
        dic[word] = len(word)
    return dic


sentance = input("ENter your sentance: ")
word_count = map_words(sentance)
print(word_count)
        
        

