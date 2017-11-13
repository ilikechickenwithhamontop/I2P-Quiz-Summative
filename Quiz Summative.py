lives = 3 #lives variable
score = 0 #score variable
cat_choose = ""#chosen category variable
def instructions(): #Asks user if they want to read the Instructions
    print("Welcome to the Non-Academic Nerd Quiz")
    rule = str(input("Would you like to read the instructions?(yes or no)"))
    if rule.lower() == "yes":
        print ("Instructions: the non-academic nerd quiz is a quiz about nerdy-non academic things.\nYou will be asked to answer questions about the chosen category. If you answer 3 wrong, game over.\n If you answer less than 3 questions wrong by the end of the quiz, you win. Please answer using a, b, c, or d(Refer to the Answer Key for the correct answers)")
        categories()
    elif rule.lower() == "no":
        categories()
    else:
        print("Please enter a valid response")#If answer is invalid it recalls the function
        instructions()

def categories(): #Asks the user to choose a category of questions
    global cat_choose#Declares the cat_choose variable as global
    cat_choose = str(input("Please Choose a Category(Anime, Video Games, or Movies)")) #Reassigns the cat_choose variable to this string value
    if cat_choose.lower() == "anime":
        anime_q1()
    elif cat_choose.lower() == "video games":
        video_games_q1()
    elif cat_choose.lower() == "movies":
        movies_q1()
    else:
        print ("Please enter a valid response")
        categories()

def anime_q1(): #Anime Question 1 Function
    global lives #Calls the lives variable into the function
    global score #Calls the score variable into the function
    correct = str(input("In the anime Naruto, what was the name of the man known as the Copy Cat Ninja?\n a)Mizuku Hiyaki \n b)Kozuku Mitashi\n c)Kakashi Hatake \n d)Naruto Uzumaki)"))
    if correct.lower() == "c":
        score +=1 #Add one to your score if the answer is correct
        anime_q2()

    else:
        lives -=1 #Subtracts one life if answer is incorrect
        print("Incorrect, You have", +lives, "lives")
        if lives == 0: #Lose if lives reach zero
            lose()
        else:
            anime_q2() #continue if lives don't reach zero

def anime_q2():#Anime Question 2 Function
    global lives
    global score
    correct = str(input("What anime is about a group of pirates with a rubber captain?\n a)Bleach \n b)One Piece\n c)Cowboy Bebop \n d)Sailor Moon"))
    if correct.lower() == "b":
        score +=1
        anime_q3()

    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q3()

def anime_q3():#Anime Question 3 Function
    global lives
    global score
    correct = str(input("In the anime Fairy Tail, who was Natsu's dad?\n a)Eneel, King of the Water Dragons \n b)Tatsu \n c)Gray Fullbuster \n d)Igneel, King of the Fire Dragons"))
    if correct.lower() == "d":
        score +=1
        anime_q4()

    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q4()

def anime_q4():#Anime Question 4 Function
    global lives
    global score
    correct = str(input("What Does SAO stand for?\n a)Supreme Aincrad Oculus \n b)Super Amazing Octopus  \n c)Sword Art Online \n d)Swing Act Organisation"))
    if correct.lower() == "c":
        score +=1
        anime_q5()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q5()

def anime_q5():#Anime Question 5 Function
    global lives
    global score
    correct = str(input("Fill the Blank: _____ Deadly Sins\n a)12 \n b)7  \n c)8 \n d)13"))
    if correct.lower() == "b":
        score += 1
        anime_q6()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q6()

def anime_q6():#Anime Question 6 Function
    global lives
    global score
    correct = str(input("How many Dragon balls does it take to summon Shenron?\n a)9 \n b)12  \n c)21 \n d)7"))
    if correct.lower() == "d":
        score +=1
        anime_q7()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q7()

def anime_q7():#Anime Question 7 Function
    global lives
    global score
    correct = str(input("Fill in the blank: Naruto is the ___ Hokage\n a)7 \n b)8  \n c)9 \n d)10"))
    if correct.lower() == "b":
        score +=1
        anime_q8()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q8()

def anime_q8():#Anime Question 8 Function
    global lives
    global score
    correct = str(input("What is required to kill someone using the Death Note? \n a)Their name and what they look like \n b)Their first and last name  \n c)Their name and their best friend \n d)Their name, gender, and age"))
    if correct.lower() == "a":
        score +=1
        anime_q9()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q9()

def anime_q9():#Anime Question 9 Function
    global lives
    global score
    correct = str(input("What is the name of the protagonist in Death Note? \n a)Dark Dakari \n b)Gray Fugashi  \n c)White Watari \n d)Light Yagami"))
    if correct.lower() == "d":
        score +=1
        anime_q10()
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            anime_q10()

def anime_q10():#Anime Question 10 Function
    global lives
    global score
    correct = str(input("Which Animes are referred to as the Big Three? \n a)Dragonball Z, Fairy Tail, SAO \n b)Naruto, Dragonball Z, One Piece  \n c)Naruto, One Piece, Bleach \n d)Bleach, Sailor Moon, Dragon Ball Z Kai"))
    if correct.lower() == "c":
        score += 1
        win() #Last question is correctly answered, you win
    else:
        lives -=1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            win() #If last question is answered incorrectly, but lives have not reach zero, you win

def video_games_q1():#Video Games Question 1 Function
    global lives
    global score
    correct = str(input("How many diamonds do you need to make a Diamond Block in Minecraft?\n a)9 \n b)21 \n c)42 \n d)4"))
    if correct.lower() == "a":
        score +=1
        video_games_q2()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            video_games_q2()

def video_games_q2():#Video Games Question 2 Function
    global lives
    global score
    correct = str(input("Who was the first new support hero released after the launch of Overwatch?\n a)Lucio \n b)Ana \n c)Mercy \n d)Winston"))
    if correct.lower() == "b":
        score +=1
        video_games_q3()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            video_games_q3()

def video_games_q3():#Video Games Question 3 Function
    global lives
    global score
    correct = str(input("When was league of legends released?\n a)October 27, 2009 \n b) December 27, 2010 \n c)October 31, 2009 \n d)January 1, 2008"))
    if correct.lower() == "a":
        score +=1
        video_games_q4()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            video_games_q4()

def video_games_q4():#Video Games Question 4 Function
    global lives
    global score
    correct = str(input("What is Mojang's most famous game?\n a)Scrolls \n b)Overwatch \n c)Minecraft \n d)Five Nights at Freddy's"))
    if correct.lower() == "c":
        score +=1
        video_games_q5()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            video_games_q5()

def video_games_q5():#Video Games Question 5 Function
    global lives
    global score
    correct = str(input("What games was one of the most popular in 2016 and is a location-based augmented reality game?\n a)Job Simulator \n b)Ordinal Scale \n c)Auggy \n d) Pokémon Go"))
    if correct.lower() == "d":
        score +=1
        win()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            win()

def movies_q1():#Movies Question 1 Function
    global lives
    global score
    correct = str(input("Who played John McClane in Die Hard?\n a)Bruce Willis \n b) Johnny B Goode \n c)Leonardo Di Caprio \n d)OJ Simpson"))
    if correct.lower() == "a":
        score +=1
        movies_q2()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            movies_q2()

def movies_q2():#Movies Question 2 Function
    global lives
    global score
    correct = str(input("Who played Anakin Skywalker in the prequels of Star Wars?\n a)Harrison Ford \n b)Ewan McGregor \n c)The Rock \n d)Hayden Christensen"))
    if correct.lower() == "d":
        score +=1
        movies_q3()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            movies_q3()
def movies_q3():#Movies Question 3 Function
    global lives
    global score
    correct = str(input("What song does Marty Mcfly play on the electric guitar at the end of Back to the Future part I?\n a)Back in Black \n b)Highway to Hell \n c)Johhny B Goode \n d)You Shook Me All Night Long"))
    if correct.lower() == "c":
        score +=1
        movies_q4()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            movies_q4()

def movies_q4():#Movies Question 4 Function
    global lives
    global score
    correct = str(input("Who was called first to get sorted into a Hogwarts House?\n a)Hermione Granger \n b)Harry Potter \n c)Neville Longbottom \n d)Ronald Weasley"))
    if correct.lower() == "a":
        score +=1
        movies_q5()
    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            movies_q5()

def movies_q5():#Movies Question 5 Function
    global lives
    global score
    correct = str(input("Which of these has become a popular catch phrase in the Star Wars Movies?\n a)Nooooooo! \n b)I am your father \n c)May the fourth be with you \n d)I have a bad feeling about this"))
    if correct.lower() == "d":
        score += 1
        win()

    else:
        lives -= 1
        print("Incorrect, You have", +lives, "lives")
        if lives == 0:
            lose()
        else:
            win()

def lose():
    global lives
    global score
    restart = str(input("You lose, would you like to restart?")) #Asks user whether they would like to restart
    if restart.lower() == "yes":
        lives +=3
        score *=0
        instructions()
    elif restart.lower() == "no":
        print("Aw ok. Bye")
    else:
        print("Please Enter a Valid Answer")
        lose()
def win():#Win
    print("CONGRATULATIONS! YOU WON!")
    scoreboard = str(input("Would you like to submit your score?"))
    if scoreboard == "yes":
        scores()
    elif scoreboard.lower == "no":
        print("Aw ok. Bye")
    else:
        print("Please Enter a valid answer")
        win()
def scores():
    global score#Declares score variable global
    global cat_choose#Declares cat_choose variable global
    global lives#Declares lives variable global
    name = str(input("What is your name?"))#Asks user for name
    f = open("txtfile.txt","w")#Opens the txt file in the write mode
    f.write(str(cat_choose))#prints Category chosen in the categories function
    f.write(":")
    f.write(str(name))#Prints name
    f.write(" scored ")
    f.write(str(score))#Prints Score
    f.write(" points with ")
    f.write(str(lives))#Prints lives
    f.write(" lives remaining")
    f.close()#Closes the txt file
    f = open("txtfile.txt","r")#Opens the txt file in the read mode
    print(f.read())#Prints what's being read in the txt file
    f.close()#Closes txt file
instructions()

