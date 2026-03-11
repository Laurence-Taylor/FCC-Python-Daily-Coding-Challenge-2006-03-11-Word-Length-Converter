def convert_words(s):
    s_to_return = ''
    list_s = list(s)
    prev_pos = 0
    for i in range(len(list_s)):
        if list_s[i] == ' ':
            s_to_return += str(i-prev_pos) + ' '
            prev_pos = i + 1
        if i == len(list_s)-1:
            s_to_return += str(i-prev_pos+1)
    return s_to_return

if __name__ == '__main__':
    print(convert_words("hello world"))
    print('-------')
    print(convert_words("Thanks and happy coding"))
    print('-------')
    print(convert_words("The quick brown fox jumps over the lazy dog"))
    print('-------')
    print(convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"))