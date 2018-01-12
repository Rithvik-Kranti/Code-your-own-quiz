#the questions to be answered by the player
questions = ["What should be replaced for __1__?", "What should be substituted in for __2__?", "What should be substituted in for __3__?","What should be substituted in for __4__?","What should be replaced for __5__?","What should be replaced for __6__?","What should be replaced for __7__?"]

#blanks to be filled in
blanks = ['__1__','__2__','__3__','__4__','__5__','__6__','__7__']

#different levels and their respective paragraphs
quiz_paragraph = {'easy':"""The current paragraph reads as such:

Behold '90's kids.Just when we taught we would be done with fantasy movies of J.K Rowling's Harry Potter series, in came George R.R Martin's collaboration with H.B.O ,
__1__ series. The first family house we get introduced to is the House __2__ family. They live at __3__. In __1__, all families have "family words".
The words of House __2__ are : '__4__ is Coming'. Anyone who watches a couple of episodes of this series would feel that House __2__ would rule all the kingdoms one day

""",

'medium':"""The current paragraph reads as such:

When __1__ Lannister, pushes __2__ Stark down, from the tower at the end of first episode, one tends to start hating him.
It's only when __1__ starts his journey with __3__ of Tarth in season 2 , the fans get to know his past and  kind of start admiring him . When they get back to King's 
landing , __4__ Lannister, who is __1__ 's sister, doesn't like the togetherness of __1__ and __3__.
""",

'hard':"""The current paragraph reads as such:

When the Madking and his children were killed during __1__'s Rebellion, liitle did __1__ knew about love between Madking's son, __2__ Targaryen and __3__ Stark's 
sister, __4__ Stark. Various families thought that __3__ Stark was disloyal to __5__ Stark, when he brought home a small boy named : __6__ Snow after 
the war. But during Bran's vision , the fans came to know that , __6__ Snow wasn't actually a bastard son of __3__, but he was the son of the Prince __2__ Targaryen, 
and __4__ Stark. In order to protect __6__ from __1__ Baratheon's wrath on Targaryen family, __3__ passed the name of __7__ Targaryen's (also known as the Madking) 
grandson as his bastard son . __3__ din't even think about his own image to save his sister's son.

"""}


#answers for each level's blanks
answers = {'easy':['Game of Thrones','Stark','Winterfell','Winter'],'medium':['Jaime','Bran','Brienne','Cersei'],'hard':['Robert','Rhaegar','Ned','Lyanna','Catelyn',
'Jon', 'Aerys']}

options = []



#allowing the player to choose the difficulty level
def quiz():
    user_input_difficulty = "Select the difficulty : easy or medium or hard "
    choice = raw_input(user_input_difficulty)
    intro = "You have chosen " + str(choice) 
    print intro
    if choice.lower() == 'hard' or choice.lower() == 'medium' or choice.lower() == 'easy':
        return start(choice)
    else:
        print choice +" is invalid response"
        return quiz()

#allowing the player to choose the number of guesses they'd want
def start(choice):
    user_input_guesses_prompt = "Select the number of guesses you would want "
    guesses_number = raw_input(user_input_guesses_prompt)   
    if int(guesses_number):
        guesses_number = int(guesses_number)
        guess_text = "You will get " + str(guesses_number) + " chances"
        print guess_text
        return option(choice.lower(),0,guesses_number)


def option(choice,option_index,guesses_number):
    #input:chocie,question the player is on,guesses remaining
    #output:winning message, correct answer message, wrong answer message/game over message

    print quiz_paragraph[choice]
    if option_index == len(answers[choice]):
        return win(guesses_number)
    options.append(raw_input(questions[option_index]))
    if options[option_index] == answers[choice][option_index]:
        return right(option_index,choice,guesses_number)
    else:
        return wrong(guesses_number,choice,option_index)


def right(option_index,choice,guesses_number):
    #when it is a right answer:
    #input : number of guesses remaining, and which blank is the player on
    #ouput:option function with guesses remaining
    right_blank_answer = "Correct! " + str(options[option_index]) + " is the right option"
    print right_blank_answer
    quiz_paragraph[choice] = quiz_paragraph[choice].replace(blanks[option_index],options[option_index])
    return option(choice,option_index+1,guesses_number)

def wrong(guesses_number,choice,option_index):
    #when it is a wrong answer:
    #input:number of guesses remaining, and which blank is the player on
    #output:wrong answer or game over message
    wrong_option = options.pop()
    if guesses_number == 0:
        game_over = "Your guesses count is done.Game over"
        return game_over
    else:
        guesses_number -= 1
        wrong_answer_text = wrong_option + " isn't the correct answer!Let's try again; you have " + str(guesses_number) + " guesses left"
        print wrong_answer_text
        return option(choice,option_index,guesses_number)

def win(guesses_number):
    #winning message
    winning_message = "Congrats.You won. And You had " + str(guesses_number) + " guesses remaining."
    return winning_message


print quiz()

