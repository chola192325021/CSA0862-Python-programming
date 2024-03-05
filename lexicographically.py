def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    def count_strings_helper(n, index):
        if n == 0:
            return 1
        count = 0
        for i in range(index, len(vowels)):
            count += count_strings_helper(n - 1, i)
        return count
    return count_strings_helper(n, 0)
n=eval(input("enter the number:"))
print(count_sorted_vowel_strings(n))
