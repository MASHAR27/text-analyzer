print("----Text Analyzer ----")


while True:
    text = input("Please enter your text:  ").strip()
    if len(text) == 0:
        print("Please enter something")
    else:
        break    
  
    

print("You entered: ",text)


print("The number of characters in the text:"  , len(text)) # this is for all the characters even the spaces

# now for all the characters except the spaces
text_without_space = text.replace(" ","")
print("The number of characters in the text excluding the spaces: ",len(text_without_space))
# Removing the punctutations since they don't contribute much in terms of wording
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("!", "")
text = text.replace("?", "")

# Now we giveback the number of words in the text
words = text.split()
word_counter = 0
for i in words:
    word_counter += 1

print("The number of words in the text are: ",word_counter)

# Now I do the vowels counting
vowels_counter = 0
for w in words:
    for ch in w:
        if ch.lower() in "aeiou":
            vowels_counter+= 1
            
            
print("The number of vowels are: ",vowels_counter)            

# Now I want to calculate the number of consonants in the text
cons_counter = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() not in "aeiou":
            cons_counter+= 1
print("The number of consonants in the text:  ",cons_counter)


# Now I count the number of digits present in the text
digit_counter = 0
for d in text:
    if d.isdigit():
        digit_counter +=1 
        
print("The number of digits are: ",digit_counter)        


# Now I will calculate the number of Uppercase and Lowercase characters each
upper_counter = 0
lower_counter = 0

for ch in text:
    if ch.isupper():
        upper_counter += 1
    elif ch.islower():
        lower_counter += 1
        
print(f"The number of Uppercase characters are {upper_counter} and the number of Lowercase characters are {lower_counter}")
            
# Now I find the first and last word in the text
first_word = words[0]
last_word = words[-1]

print(f"First word is {first_word} and the last word is {last_word}")


# Now I want to find whether the user entered Python (case-insensitive) in the text
python_present = False
for word in words:
    if word.lower() == "python":
        python_present = True
        break
    
print(f"Python (the word) present in the text: {python_present}")

# Now I'm going to reverse the entire text character by character
reversed_text_char = text[::-1]
print(f"The reversed text character by character is: {reversed_text_char}")


# Now I will search for a specific character that uses asks 
while True:
    char_search = input("Enter a character to search for in the text:  ").lower()
    if len(char_search) == 1:
        break 
    else:
        print("Please just enter one character")


char_count_times = text.lower().count(char_search)  


print(f"{char_search} appears {char_count_times} times in your text")

# Now searching for a specific word the user enters in the text
word_search = input("Enter a word to search for in the text:  ").lower()

word_counter_search = 0

for w in words:
    if w.lower() == word_search:
        word_counter_search +=1
        
        
print(f"{word_search} appears {word_counter_search} times in the text")

        

    
