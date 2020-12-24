import random
import csv

def Transpose(A):                           # Get matrix A as an input and return a transpose matrix of A
    row = len(A)
    col = len(A[0])
    A_T = list()
    for j in range(col):
        temp = list()
        for i in range(row):
            temp.append(A[i][j])
        A_T.append(temp)
    return A_T

class dist:
    def __init__(self):
        self.probList = list()              # List that has problem lists of chapters for element
        self.distNum = list()
        self.chapterNum = 0                 # The number of chapters
        self.ppC = list()                   # The max number of problems per chapters
        self.date = 0                       # Period
        self.probDist = list()              # Final result that will be written to the csv file.
        self.distT = list()                 # Final result that is transposed

    def init(self):
        self.probList = list()  # List that has problem lists of chapters for element
        self.distNum = list()
        self.chapterNum = 0  # The number of chapters
        self.ppC = list()  # The max number of problems per chapters
        self.date = 0  # Period
        self.probDist = list()  # Final result that will be written to the csv file.
        self.distT = list()  # Final result that is transposed

    def getProb(self):                      # Get sequence of problems divided by ',' and make a problem list.
        inputstrlist = input("Please enter your all problems separated by slash('/')\n- ").strip().split("/")
        for inputStr in inputstrlist:
            temp = inputStr.split()
            self.probList.append(temp)
        self.chapterNum = len(inputstrlist)

    def shuffle(self):                      # Shuffle the problem list, it must be called after function 'getProb'
        for list1 in self.probList:
            random.shuffle(list1)

    def getSequence(self):                  # Get sequence for problem distribution, which should be called after
        for list1 in self.probList:         # 'getProb' and 'getMaxNum'
            pnum = len(list1)//self.date
            rest = len(list1) % self.date
            temp_list = [pnum for i in range(self.date)]
            for i in range(rest):
                temp_list[i] += 1
            random.shuffle(temp_list)
            self.distNum.append(temp_list)

    def getPeriod(self):                    # Get period for distribution
        while True:
            try:
                self.date = int(input("Please enter the period you're planning (number): "))
                break
            except ValueError:
                print("Your input is invalid")

    def getMaxNum(self):                    # Get maximum number of problem for each chapter.
        for list1 in self.probList:
            totalpnum = len(list1)
            max_pnum = (totalpnum + self.date - 1)//self.date
            self.ppC.append(max_pnum)

    def make_dist(self):                    # Make distribution, not yet transpose
        for i in range(self.date):
            one_day = list()
            one_day.append("Day {0}".format(i+1))
            for cnum in range(self.chapterNum):
                one_day.append("Ch. {0}".format(cnum+1))
                pnum = self.distNum[cnum][i]
                for j in range(pnum):
                        one_day.append(str(self.probList[cnum].pop()))
                if pnum < self.ppC[cnum]:
                    one_day.append("")
            self.probDist.append(one_day)

    def distTrans(self):
        self.distT = Transpose(self.probDist)

    def make_print(self):
        print(self.probDist)

    def make_Tprint(self):
        print(self.distT)

    def make_csv(self):
        f = open('Problem.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        for list1 in self.distT:
            wr.writerow(list1)
        f.close()

    def main_dist(self):
        self.getProb()
        self.getPeriod()
        self.getMaxNum()
        self.shuffle()
        self.getSequence()
        self.make_dist()
        self.distTrans()
        self.make_print()

    def main_csv(self):
        self.getProb()
        self.getPeriod()
        self.getMaxNum()
        self.shuffle()
        self.getSequence()
        self.make_dist()
        self.distTrans()
        self.make_csv()

    def make(self):
        self.getProb()
        self.getPeriod()
        self.getMaxNum()
        self.shuffle()
        self.getSequence()
        self.make_dist()
        self.distTrans()


def main():
    while True:
        istr = input("Please enter the command: ").strip()
        if istr == "quit" or istr == "exit":
            exit(0)
        elif istr == "do":
            mydist2 = dist()
            mydist2.main_csv()
            print("Done\n")
        elif istr == "make":
            mydist1 = dist()
            mydist1.make()
            print("Done\n")
        elif istr == "print":
            mydist1.make_print()
            print("Done\n")
        elif istr == "makefile":
            mydist1.main_csv()
            print("Done\n")
        elif istr == "init":
            mydist1.init()
            print("Done\n")
        elif istr == "help":
            print("make: make new distribution\nprint: print distribution made\nmakefile: make csv file\nexit: exit")
        else:
            print("Invalid command. If you want to know about commands, please enter 'help'")


if __name__ == "__main__":
    main()






