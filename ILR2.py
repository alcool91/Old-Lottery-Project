#Lottery simulation program
#4/16/14 made lottery a class, added 4 or 5 digit support
#4/16/14 added support for box type bets, now program assumes all payouts are for box type bets --RESOLVED 4/17
from random import *
import time



class Lottery:
    def __init__(self, digits, betType, betAmt):
        self.digits = digits
        self.betType = betType
        self.betAmt = betAmt

    def winner(self, tries, choice, betType):
        if self.betType.upper() == 'STRAIGHT' or self.betType.upper() == 'S':
            if self.digits == '3':
                if self.betAmt == '1.00':
                    payout = 500
                elif self.betAmt == '0.50':
                    payout = 250
            elif self.digits == '4':
                if self.betAmt == '1.00':
                    payout = 5000
                elif self.betAmt == '0.50':
                    payout = 2500
            elif self.digits == '5':
                if self.betAmt == '1.00':
                    payout = 50000
                elif self.betAmt == '0.50':
                    payout = 25000

#At present I am still working on 5 digit box type bets -- 4/17/14
        if self.betType.upper() == 'BOX' or self.betType.upper() == 'BOXED' or self.betType.upper() == 'B':
            if self.digits == '3':
                if self.betAmt == '1.00':
                    if len(set(choice)) == 3: # 6 way box
                        payout = 83
                    elif len(set(choice)) == 2: # 3 way box
                        payout = 167
                elif self.betAmt == '0.50': 
                    if len(set(choice)) == 3: # 6 way box
                        payout = 41.5
                    elif len(set(choice)) == 2: # 3 way box
                        payout = 83.5
            elif self.digits == '4':
                if self.betAmt == '1.00':
                    if len(set(choice)) == 4: #24 way box
                        payout = 200
                    elif len(set(choice)) == 3: #12 way box
                        payout = 400
                    elif len(set(choice)) == 2:
                        if sorted(choice)[0] == sorted(choice)[1] == sorted(choice)[2]: # 4 way box
                            payout = 1198
                        else: # 6 way box
                            payout = 800 
                elif self.betAmt == '0.50':
                    if len(set(choice)) == 4: #24 way box
                        payout = 100
                    elif len(set(choice)) == 3: #12 way box
                        payout = 200
                    elif len(set(choice)) == 2:
                        if sorted(choice)[0] == sorted(choice)[1] == sorted(choice)[2]: # 4 way box
                            payout = 599
                        else: # 6 way box
                            payout = 400
            elif self.digits == '5':
                if self.betAmt == '1.00':
                    if len(set(choice)) == 5: # 120 way box
                        payout = 417
                    elif len(set(choice)) == 4: # 60 way box
                        payout = 834
                    elif len(set(choice)) == 3: # Still working on all 5 digit box payouts
                        if sorted(choice)[0] == sorted(choice)[1]:
                            pass
                elif self.betAmt == '0.50':
                    payout = 25000

        print "-----" * 10
        print "winner after " + str(tries) + " tries!"
        print "It took you " + str(tries/2) + " days to win!"
        print "your tickets cost $" + str(tries * float(self.betAmt)) + ".00"
        print "Your payout was $" + str(payout) + ".00"
        print "Your Net Revenue was $" + str(payout - (tries * float(self.betAmt))) + ".00"
        print "-----" * 10
        

    def play(self):
        print "<>" * 40
        print "Use 'mp' to play the same 'machine pick' each time"
        print "Use 'ap' to play a new 'machine pick' number each time"
        print "<>" * 40
        guess = raw_input("Choose a lottery number and see how long it takes until you win! >>")
        if guess.upper() == 'MP': #added machine pick option
            if self.digits == '3': #attempt support for 4 and 5 digit numbers
                choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            elif self.digits == '4':
                choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            elif self.digits == '5':
                choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            else:
                pass
        elif guess.upper() == 'AP': #placeholder for autopick in main loop
            pass
        else:
            choice = guess
        tries = 0
        while True:
            if guess.upper() == 'AP': #added machine pick option
                if self.digits == '3': #attempt support for 4 and 5 digit numbers
                    choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
                elif self.digits == '4':
                    choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
                elif self.digits == '5':
                    choice = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            if self.digits == '3': #attempt support for 4 and 5 digit numbers
                winning = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            elif self.digits == '4':
                winning = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            elif self.digits == '5':
                winning = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            print winning, choice
            tries += 1
            if self.digits == '3':
                time.sleep(0.02)
            elif self.digits == '4':
                time.sleep(0.002)
            else:
                time.sleep(0.0005)
            if self.betType.upper() == 'STRAIGHT':
                if winning == choice:
                    self.winner(tries, choice, self.betType)
                    break
            elif self.betType.upper() == 'BOXED' or 'BOX':
                if sorted(winning) == sorted(choice):
                    self.winner(tries, choice, self.betType)
                    break
class Menu:
    def __init__(self):
        #self.game = Lottery(digits, betType, betAmt)
        self.start()
    def start(self):
        print "Welcome to the Lottery!"
        self.digits = raw_input("Would you like to play '3' digit, '4' digit, or '5' digit? >> ")
        self.betType = raw_input("Straight, or Boxed bet type? >> ")
        self.betAmt = raw_input("$0.50, or $1.00? >> ")
        self.game = Lottery(self.digits, self.betType, self.betAmt)
        self.game.play()
        raw_input("Enter to play again")

Menu1 = Menu()
#game = Lottery(digits, betType, betAmt)
if __name__ == '__main__':
    while True:
        Menu1.start()
        
