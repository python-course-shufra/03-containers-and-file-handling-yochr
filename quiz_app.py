import sys
import random


def main():
   import sys
import random


def main():
    # TODO: your code here
    sub = sys.argv[1]
    num = int(sys.argv[2])
    countQues = 1
    countCorrect = 0
    countLine = 1
    q = ""
    correct = ""
    answer = []
    parts = []
    
    file = open(rf'questions\{sub}.txt')
    for f in file:
        if countQues > num:
            break
        countQues += 1
        parts = f.split(";")
        q = parts[0]
        correct = parts[1]
        parts[2].rstrip()
        answer = parts[2].split(",")
        answer.append(correct)
        random.shuffle(answer)
        print(q)
        for a in answer:
            print(f'{countLine}. {a}')
            countLine += 1
        countLine = 1
        if correct == answer[int(input())-1]:
            countCorrect += 1
    print(f'you answer {countCorrect}/{num} correct answer')


main()


if __name__ == '__main__':
    main()
