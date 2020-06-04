# import random
import nltk
nltk.download('words')
from nltk.corpus import words

word_list = words.words()

print(len(word_list))

# chars = ['0'...'9']


# take in plain numbers and the key as the two arguments
def encrypt(plain, key):
    alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
    alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    encrypted_string = ""

    
    # if isinstance

    # plain input of '1234' -> to an encrypted '2345' with key of 1


    for char in plain:
        # need to change the string input of '1' and change it to an integer of 1
        char = str(char)

        if char in alphabet_lowercase:
            char_indx = alphabet_lowercase.find(char)
            new_indx = (char_indx+key) % len(alphabet_lowercase)

            new_char = alphabet_lowercase[new_indx]
            # return(new_char)
            encrypted_string+=new_char
        
        elif char in alphabet_uppercase:
            char_indx = alphabet_uppercase.find(char)
            new_indx = (char_indx+key) % len(alphabet_uppercase)

            new_char = alphabet_uppercase[new_indx]
            # return(new_char)
            encrypted_string+=new_char

        else:
            encrypted_string+=char

    return encrypted_string

# run test to see if the positive and negative key return opposite results, that is how you figure out the key
def decrypt(encoded, key):
    return encrypt(encoded, -key)



def break_code(phrase):
    alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
   
    for key in range(len(alphabet_lowercase)):
        counter = 0

        # something wil be the phrase exactly at first loop
        secret = decrypt(phrase, key)

        # split phrase by spaces into individual words, save into a new list
        secret_list = secret.split(" ")

        for wordszy in secret_list:
            if wordszy in word_list:
                counter +=1

        if (counter/(len(secret_list))) >= 0.5:
            return secret


    # for key in range(10):
    # # run through each decrypt
    #     print(decrypt(phrase, key))
    # pass


# if __name__ == "__main__":
#     encrypted = encrypt("It was the best of times, it was the worst of times", 5)
#     break_code(encrypted)




# manual test of 12345 with a key of 1
    # assert encrypt('12345', 1) == '23456'
    # assert encrypt('23456', -1) == '12345'
    # print("all good")



    # pins = [
    #     "1234",
    #     "9876",
    #     "0000",
    #     "9999",
    # ]

    # for pin in pins:
    #     key = random.randint(1, 9)
    #     print("plain pin", pin)
    #     encrypted_pin = encrypt(pin, key)
    #     print("encrypted_pin", encrypted_pin)
    #     decrypted_pin = decrypt(encrypted_pin, key)
    #     print("decrypted_pin", decrypted_pin)