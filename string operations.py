#In Python 2.7 replace input() to raw_input()
# Reads a string from input and type case them to int 
# after splitting to white-spaces
 
formatted_list = list(map(int, input().split()))
print(formatted_list)
