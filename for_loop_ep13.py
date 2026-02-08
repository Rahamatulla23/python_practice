#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
#Note : be sure to not double-count words that contain both an a and an e.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0

for word in sentence.split():
    if ('a' in word) or ('e' in word):
        num_a_or_e += 1

print(num_a_or_e)
