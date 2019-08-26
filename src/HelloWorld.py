import random

def random_compliment():
    complimentList = ["kind","lovely","awesome","amazing","one cool cat"]
    randInt = random.randint(0, len(complimentList)-1) 
    return complimentList[randInt]

def main():
    msg = "Hello World! What's your name?"
    print(msg)
    name = input()
    compliment = random_compliment()
    msg2 = "Nice to meet you, " + name + "! You are " + compliment + "!"
    print(msg2)

if __name__ == '__main__':
    main()