# Writing a lambda function


# also we write this lambda funtion into funtion like this

# def echo_word(word1,echo):
#     words =word1*echo
#     return words

# ************************************************

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1 ,echo: word1*echo)

# Call echo_word: result
result = echo_word("hey",5)

# Print result
print(result)

