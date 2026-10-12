
# This program helps to guess the daily wordle word
Libraries used to make the project are 
- 1. Requests
- 2. Random
- 3. String

Requests module to make the get request on the daily wordle API. Getting the response back as a list of dictionaries with every dictionary containing 3 keys, 'slot','guess' and 'result' where 'slot' means the index the character should be present and 'guess' means character present on the index and 'result' will tell us if the right character is present at the right place. 

Result = 'absent' means, that character is not present in the daily word and we guessed it wrong. 
Result = 'present' means, that character is present but don't know where exactly it will be present
Result = 'correct' means, that correct character is present at the correct index

Random module is used to randomly choose 5 letters from the total available letters in the alphabets. 

String module is used to get all possible lower case letters in the alphabets. 

Making a correctletter dictionary which will contain the key as the indexes of the word and the value as the correct character at that index. But, we initialized all of the indexes with # and whenever we get a response back from the API and any of the indexes got the correct character on it we will update that index with that character with the correctletter dictionary. 
