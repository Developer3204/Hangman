def checkLetter(word, letter):
	word1=word.casefold()
    returninglist=[]
    letters = list(word1)
    for i in range (len(word1)):
        letchecked=letters[i]
        if letter==letchecked:
            returninglist.append(True)
            global hasword = True
        else:
            returninglist.append(False)
    return(returninglist)
class Status:
    def __init__(self, answer):
        self.score = 6
        self.word = answer.lower()
        self.usedLetters = []
        self.currentState = []
        self.isInWord = 0
        for i in range(len(self.word)):
            self.currentState.append(" _ ")

    def showState(self):
        self.state = ""
        self.used = ""
        for i in range(len(self.currentState)):
            self.state = self.state + self.currentState[i]
        for i in range(len(self.usedLetters)):
            self.used = self.used + self.usedLetters[i]
        return self.state + "\nUsed Letters\n" + self.used

    def changeState(self, positionsToChange, guess):
        self.placement = positionsToChange
        self.guess = " " + str(guess) + " "
        self.alreadyGuessed = False
        for i in range(len(self.usedLetters)):
            if self.usedLetters[i] == self.guess:
                self.alreadyGuessed = True
        if not self.alreadyGuessed:
            self.usedLetters.append(self.guess)
        for i in range(len(self.placement)):
            if self.placement[i]:
                self.isInWord = 1
        if self.isInWord == 1:
            for i in range(len(self.word)):
                if self.placement[i]:
                    del self.currentState[i]
                    self.currentState.insert(i, self.guess)
            self.isInWord -= 1
            return True
        else:
            return False

    def allLettersCorrect(self):
        self.currentWord = ""
        for i in range(len(self.placement)):
            self.currentWord = self.currentWord + str(self.currentState[i])
        self.currentWord = self.currentWord.replace(" ", "")
        if self.currentWord == self.word:
            return True
        else:
            return False

	    
wantToPlay = input("Hello! Would you like to play a game of hangman??? (Yes or No) ")
while wantToPlay == "Yes" or wantToPlay == "yes":
	numWrong = 0
	numLetters = int((input("How many letters would you like in your word? (Enter any number between 3 and 10) "))
  while type(numLetters) != 'int' and numLetters < 3 and numLetter > 10:
	try:  
		numLetters = int((input("Invalid input, please enter the right number: "))
	exception ValueError: 
		print("Please enter the the right integer") 
  myWord = getWord(numLetters)
  myGame = Status(myWord)
  if myGuess != myWord and len(myGuess) != 1: 
	print ("Invalid input, please enter another string")
  
  while (myGuess != myWord) or myGame.allLettersCorrect() != True:
	myGuess = input("Please guess a letter or word: ") 
	myList = checkLetter(myWord,myGuess)
    if myGame.changeState(myList, myGuess) == False
	numWrong += 1 
    drawHangman(numWrong)
    myGame.showState()
    if myGame == myWord:
	print("Yay! You win!")
	wantToPlay = input("Would you like to play again? (Yes or No) ")
    if numWrong == 6:
	print("Oop, you lose.")
	wantToPlay = input("Would you like to play again? (Yes or No) ")

print("Okay, bye.")
quit()

