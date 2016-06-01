import random

def monkeys(sl):
    alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = ""
    for i in range(sl):
        string += alphabet[random.randrange(27)]

    return string

def score(goal, s):
    correct = 0
    for i in range(len(goal)):
        if s[i] == goal[i]:
            correct += 1

    correctpct = correct / float(len(goal))
    return correctpct





def main():

    best = 0
    newscore = score("gabriel",monkeys(7))
    while newscore < 1:
        if newscore > best:
            print "%s percent  %s" % (newscore*100, newstring)
            best = newscore
        newstring = monkeys(7)
        newscore = score("gabriel", monkeys(7))

main()
