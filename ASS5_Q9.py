def count_word_occurrences(word_list):
    word_counts = {}

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Example usage
user_input = input("Enter a list of words (space-separated): ")
words = user_input.split()

word_occurrences = count_word_occurrences(words)

print("Number of occurrences of each word:")
for word, count in word_occurrences.items():
    print(word, ":", count)
