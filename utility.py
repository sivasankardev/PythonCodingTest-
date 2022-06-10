import sys
#Reading command line arguments
args =sys.argv
try:
    option = args[1]
    filename = args[2]
    #Open file for reading
    file = open(filename, encoding='utf-8', errors='ignore')
     # Reading from file
    Content = file.read()
    #Check for the option to display
    if (option=="-l"):        
        Counter = 0  
        CoList = Content.split("\n")    
        for line in CoList:
            if line:
                Counter += 1
        print("This is the number of lines in the file:", Counter)

    elif(option =="-c"):
        #read the content of file
        
        #get the length of the data
        number_of_characters = len(Content)
        print('Number of characters in text file :', number_of_characters)
    elif(option=="-w"):
        words = Content.split()
        print('Number of words in text file :', len(words))
    elif(option=="-n"):
        print("Only numerics in the file are:")
        words = Content.split()
        for word in words:
            if word.isnumeric():
                print(word)
    elif(option=="-a"):
        print("Only Alphabets in the file are:")
        for character in Content:
            if character.isalpha():
                print(character)
    elif(option=="-h"):  
        print("Run the Program in the following format\n py <program name> <Options> <filename> ")
    else:
        print("Invalid Option")
except:
    print("Please provide required arguments:")        





