print("Welcome to Solve That Murder")
print("Your ready to play, yes... ")
print("Well...lets get started")
print()
print("Welcome to Chapter 1")
print()
print("Radio music playing softly in the background along with radio chatter")
print("When suddenly over the radio all that is heard is Officer down, I repeat Officer down")
print()

choice = int(input("Do you want to ask a question, talk to dispatch or turn on your sirens and lights? "))
question = "1"
dispatch = "2"
lights_siren = "3"

if choice == 1:
    print("Who was that over the radio? Who was shot? Where are you?")
    print("This is Officer Hath, Officer West is down,\nWe are located at 1352 W Liden Lane in Chareleston")
    print("Okay, Officer Hath, I was be responding and be there as soon as possible")
elif choice == 2:
    print("Dispatch, this is 4605 I will be responding")
    print("Who was that over the radio and where was their last known location?")
    print("What is the fastest way there dispatch?")
    print("4605 the fastest way there is taking a right on the next street, taking it straight for three miles,")
    print("taking a left at Harrison Street going straight another two miles, you would have arrived at the destination")
elif choice == 3:
    print("I need to find the fastest way to get there")
print()
print("A few minutes later.....")

print("Dispatch this is 4605 Officer Dean responding to Officer Veronica Hath call for man down, I am first on the scene.")
