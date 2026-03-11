def convert_words(s):
    # Create and init variable to return the answer
    s_to_return = ''
    # define previous position pointer
    prev_pos = 0
    # iterate over each character
    for i in range(len(s)):
        # if character is a blank space then I found a new word
        if s[i] == ' ':
            # add the leng of the word to the string to return
            s_to_return += str(i-prev_pos) + ' '
            # update the previous position pointer
            prev_pos = i + 1
        # if I reach the end of the string
        if i == len(s)-1:
            # add the leng of the last word to the string to return
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