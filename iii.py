def is_isogram(word): 
  
    # Convert the word or sentence in lower case letters. 
    clean_word = word.lower() 
  
    # Make an empty list to append unique letters 
    letter_list = [] 
  
    for letter in clean_word: 
  
        # If letter is an alphabet then only check 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter) 
  
    return True
  
if __name__ == '__main__': 
    print(is_isogram("Machine"))                              
    print(is_isogram("isogram"))                          
    print(is_isogram("GeeksforGeeks"))                      
    print(is_isogram("Alphabet "))                                                
