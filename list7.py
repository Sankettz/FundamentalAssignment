def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count
strings = ['aba', 'xyz', 'aa', 'oo']
count = count_strings(strings)
print(count)