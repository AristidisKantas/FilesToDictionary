def fileToDictionary(my_file):
    
    my_file = open(my_file, "r") #import file
    fileString = my_file.read() #read file
    
    dictionary = {} # create empty dictionary
    key = ""
    value = ""
    j = 0
    
    for i in range(len(fileString)):
        if fileString[i] == "\n":
            while fileString[j] != "-":
                key += fileString[j]
                j += 1
            j += 1
            while fileString[j] != "\n":
                value += fileString[j]
                j += 1
            j += 1
            dictionary[key] = value
        key = ""
        value = ""
      
    
    while fileString[j] != "-":
        key += fileString[j]
        j += 1
    j += 1
    while j != len(fileString):
        value += fileString[j]
        j += 1
    dictionary[key] = value
    key = ""
    value = ""    
      
    return dictionary
    
# INPUT AND RUN
dictionary = fileToDictionary("routers.txt")
print(dictionary)