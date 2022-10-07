        
score = 0

test = Test()

while True:
    
    print("-----")
    print("[1] add")
    print("[2] substract")
    print("[q] exit")
    print("-----")
    m = input("select menu:")
    if (m=='q'):
        break
    elif (m=='1'):
        score = score + test.addTest()
    elif (m=='2'):
        score = score + test.subTest()
print("Your score is", score)

import random
class Test:
    def addTest(self):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = a + b
        print(a, "+", b, "= ", end="")
        ans = int(input())
        if ans == c:
            return 0
    def subTest(self):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = a - b
        print(a, "-", b, "= ", end="")
        ans = int(input())
        if ans == c:
            return 1
        else:
            return 0