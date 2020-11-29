'''This program will ask the user to ask a question and will respond with one of its classic procedures'''
#imports the random function to form the main basis of the '"Magic-8-Ball game"
import random
import time

#creates a list of answers
answers = ["Concentrate and ask again", "It is certain", "It is decidedly so", "Don't count on it", "Without a doubt", "My reply is no", "Yes definitely", "My sources say no", "You may rely on it", "Outlook not so good", "As I see it, yes", "Very doubtful", "Most likely", "Reply hazy, try again", "Outlook good", "Ask again later", "Yes", "Better not tell you now", "Signs point to yes", "Cannot predict now" ]

#defines number of times magic 8 ball delays
pause = [1, 2, 2.5, 3, 4]
#asks user if they want to play
print("I'll only ask this once, choose WISELY!")
print("Would you like the Magic 8 Ball to determine your destiny? (Yes/No)")
user_play = input (" ")
#user_play = input("Asking once, choose WISELY: would you like the Magic 8 Ball to determine your destiny?(Yes/No): ")

#function which sets the conditional for the program to give an answer to the user's question if they decide to play
def fortune_telling():
  #asks user a polar question
  print(input("What would you like to know?: "))
  wait = random.choice(pause)
  time.sleep(wait)
  print(random.choice(answers)) 

#creates a while loop that keep that keep this program running as long as the user does not stop it
while user_play == ("Yes"):
  fortune_telling()

print("Okay, you may proceed to the rest of your day.")
#it is the logic, you neverbreak out of "yes" once you typed it in under fortune_telling
  
#Problems
'''
1.Why is my question asked displayed?
'''
