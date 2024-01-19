import random

class Cricket():
    def __init__(self):
        self.balls = 0
        self.runs = 0
        self.target_runs = 0

        self.curr_wickets = 0
        self.ch = ""
        self.freeHit = False

        self.gameOver = False
        self.innings = 1

    def toss(self):
        print("   ### THE TOSS BEGINS ###   ")
        print()
        print("1> Heads")
        print("2> Tails")
        print("3> Let Computer choose")
        print()

        try:
            user_ch = int(input("Enter choice : "))
            comp_ch = random.randint(1,2)
            print()

            if user_ch in [1, 2]:
                if user_ch == comp_ch:
                    print(f'{self.name} won the toss!!')
                    print("1> Batting")
                    print("2> Bowling")
                    print()
                    ch = int(input("Enter choice : "))
                    print()

                    if ch in [1, 2]:
                        self.ch = "Batting" if ch == 1 else "Bowling"
                    else:
                        raise ValueError
                else:
                    print(f'{self.name} lost the toss!!')
                    self.ch = "Batting" if comp_ch == 1 else "Bowling"
                    print(f'Computer chose {"bowling" if self.ch.lower() == "batting" else "batting"}')
                    print()
            elif user_ch == 3:
                self.ch = "Batting" if comp_ch == 1 else "Bowling"
                print(f'Computer chose {"bowling" if self.ch.lower() == "batting" else "batting"}')
                print()

            else:
                raise ValueError
        except ValueError:
            print("Invalid Input | Try Again")
            print()
            self.toss()

        self.start_game()

    def display_score(self):
        print(f'Score : {self.runs}/{self.curr_wickets}', end=" | ")
        print(f'Overs : {self.balls//6}.{self.balls%6}', end=" | ")
        print(f'Run Rate : {float(self.runs) if self.balls <= 6 else self.runs // (self.balls//6)}', end="")
        print(str((" | Target : " + str(self.target_runs)) if self.target_runs > 0 else ""))

    def start_game(self):
        print("   ### THE MATCH BEGINS ###   ")
        print()
        print(f'Game is starting, {self.name} is {self.ch.lower()} first !!')
        print()

        print("Enter your choice (0,1,2,3,4,5,6) : ")
        print()

        while not self.gameOver:
          try:
            self.play_game()
          except ValueError:
            if self.freeHit:
              pass
            else:
              print("Invalid Input | Try Again")
              print()
              self.play()

        self.end_game()

    def play_game(self): 
        self.display_score()
        n = int(input(f'{self.name} : '))

        if n in [1,2,3,4,5,6]:
          comp_ent = random.randint(1,6)
          print(f'Computer : {comp_ent}')
          print()

          self.balls += 1
          if n == comp_ent and not self.freeHit:
            self.curr_wickets += 1

            if self.curr_wickets == self.wickets:
              if not self.innings == 2:
                self.change_innings()
              else:
                self.gameOver = True
          else:
            self.runs += (n if self.ch == "Batting" else comp_ent)

            if self.freeHit:
              self.freeHit = False

          if self.balls//6 == self.overs:
              if not self.innings == 2:
                self.change_innings()
              else:
                self.gameOver = True
          elif self.innings == 2 and self.runs >= self.target_runs:
              self.gameOver = True
        else:
          if self.ch == "Bowling":
            print("[Invalid Input]: That was a No Ball | Free Hit given")
            print()

            self.freeHit = True
          else:
            print("[Invalid Input]: The ball was not hit | No Run given")
            print()

            self.balls += 1

    def change_innings(self):
        self.display_score()

        self.target_runs = self.runs + 1
        self.runs = 0
        self.curr_wickets = 0
        self.balls = 0
        self.ch = "Bowling" if self.ch == "Batting" else "Batting"
        self.innings += 1

        print(f'{self.name if self.ch == "Bowling" else "Computer"} has made {self.target_runs - 1} runs')
        print()
        print(f'2nd innings is starting, {self.name} is {self.ch.lower()} now !!')
        print()

    def end_game(self):
        winner = ""
        if self.ch == "Batting":
          winner = "You" if self.runs > self.target_runs else "Computer"
        else:
          winner = "You" if self.runs < self.target_runs else "Computer"

        if winner == "":
          print("Game Over | Match Tied !!")
          print()
        else:
          print(f'Game Over | {winner} Won !!')
          print()

    def main(self):
        print("     ~~~Hand Cricket~~~     ")
        print()

        self.name = input("Enter your name : ")
        print()

        while True:
            try:
                self.overs = int(input("Enter no.of overs : "))
                self.wickets = int(input("Enter no.of wickets : "))
                print()

                if self.overs == 0 or self.wickets == 0:
                  raise ValueError

                self.toss()

                print("1> Start a new game")
                print("2> Play Again")
                print("3> Exit")
                print()

                ch = int(input("Enter choice : "))
                print()

                if ch == 1:
                    Cricket().main()
                elif ch == 2:
                    Cricket()
                elif ch == 3:
                    exit()
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input | Try Again")
                print()

if __name__ == '__main__':
    Cricket().main()
