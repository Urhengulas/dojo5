def countLetters(sentence):
    # initialize array
    count = []
    for i in range(26):
        count.append(0)

    # count letters
    for letter in sentence:
        asci = ord(letter)
        if asci == 32:
            pass
        elif asci <= 90:
            asci -= 65
            count[asci] += 1
        else:
            asci -= 97
            count[asci] += 1

    return count


def main():
    sentence = input("Input sentence: ")  # get the string of the sentence

    letterList = countLetters(sentence)

    # print out letters
    for i in range(len(letterList)):
        print(chr(i+97) * letterList[i], end="")


if __name__ == "__main__":
    main()
    print()