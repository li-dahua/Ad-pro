def are_anagram(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    return word1_sorted == word2_sorted

print("Anagram slover")

two_words = input("enter two space separated word : ")
word1, word2 = two_words.split()

if are_anagram(word1, word2):
    print ("The words are anagram")
else:
    print ("The words are not anagram")
