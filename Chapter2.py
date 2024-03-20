print("Welcome to Chapter 2")
# Setting the scene before Officer Dean
print("Officer Dean steps out of his car")
print("Rain can be heard hitting the pavement, the wind howling in the distance")
print("Stepping out of his patrol car Officer Dean sees Officer Brian West \nlaying on the ground surround by a pool of blood")
print("his partner Officer Veronica Hath sitting next to him.")
print()
#define the class of questions I would like to choose if option 1 is chosen
class question:
    def __init__(question, who, what, when, where, how):
        question.one = who
        question.two = what
        question.three = when
        question.four = where
        question.five = how

    def get_who(question):
        return question.one

    def get_what(question):
        return question.two

    def get_when(question):
        return question.three

    def get_where(question):
        return question.four
    def get_how(question):
        return question.five

    def fullquestionlist(question):
        return question.one + " " + question.two + " " + question.three + " " + question.four + " " + question.five

questions = question("Did you see who did it?", "What was going on when the shooting occurred?", "\nHow long ago was he shot?","\nWhere were you both going?", "\nHow did the shooting happen?")

# Recommended you cycle through all options before choosing option 4 to move on to chapter 3
# Move on to Chapter 3 if looking for evidence (option 4) is chosen

question = "1"
pulse = "2"
reinforcements = "3"
evidence = "4"

choice = input("Where should I do now? ")

while choice != questions:

    if choice == "1":
        print(questions.fullquestionlist())
        print()
        print("Officer Hath: We were just stopped and this man seemed to be lurking in the alley.")
        print("His sweater was covered in blood, and Brain stepped out to ask the man of he was okay")
        print("The next thing I know he is pulling out a gun and shooting, it all happend so fast, I didn't really get a good look at him")
        print("He then takes of running and I'm in shook and go to pull out my gun but by the time I have he was gone \nThat's when I called for help")
        choice = input("Where should I do? ")
    if choice == "2":
        print("I start towards Officer West body, I see Officer Hath leaning against their patrol car, Officer West laying motionless")
        print("I lower myself to the ground, feeling on Officer West neck looking for a pulse, \nI found none, \nHe is gone...")
        choice = input("Where should I do? ")

    elif choice == "3":
        print("Dispatch I have a 10-999 I need a 10-52 immediately!")
        choice = input("Where should I do? ")

    elif choice == "4":
        print("Lets start looking around and try to find some evidence?")
        break
    else:
        print("This is not an option, please chose an option from above")
        choice = input("Where should I do? ")
# Move on to Chapter 3
