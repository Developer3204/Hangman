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

wantToPlay = input("Hello! Would you like to play a game of hangman??? (Yes or No) ")
while wantToPlay == "Yes" or wantToPlay == "yes":
	numWrong == 0
	numLetters = int((input("How many letters would you like in your word? (Enter any number between 3 and 10) "))
  if numLetters != int:
  	numLetters = int((input("Invalid input, please enter an integer: "))
  myWord = getWord(numLetters)
  myGame = Status(myWord)
  myGuess = input("Please guess a letter or word: ") 
  if (myGuess != myWord) and myGuess != : 
  	print ("Invalid input, please enter another string")
  
  while (myGuess != myWord)) or (allLettersCorrect() != True):
  	myList = checkLetter(myWord,myGuess)
    myGame.changeState(myList) == False
    	numWrong += 1 
    drawHangman(numWrong)
    myGame.showState
    if myGame == myWord:
    	print("Yay! You win!")
    if numWrong == 6:
    	print("Oop, you lose.")
      
	wantToPlay = input("Would you like to play again? (Yes or No) ")

print("Okay, bye.")
quit()