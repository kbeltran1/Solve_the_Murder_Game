print("Welcome to Chapter 5")
print()
print("The nest day Dean sat at his desk, listening to the chatter, the fingers pressing again keys, and murmurs of people talking about what happened")
print()
print("(After some time Dean gets up from his desk to see if any new information is available)")

class explore:
    def __init__(check, one, two, three, four, zero):
        check.one = one
        check.two = two
        check.three = three
        check.four = four
        check.zero = zero

    def room_one(check):
        return check.one

    def room_two(check):
        return check.two

    def room_three(check):
        return check.three

    def go_to_computer(check):
        return check.four

    def exit_game(check):
        return check.zero



exploring_station = explore("Walk to detective office", "Go to lab", "Talk to Vanessa", "You have IDed the shooter, now let go back to our desk and investigate", "Arrest the shooter")

room_one = "1"
room_two = "2"
room_three = "3"
go_to_computer = "4"
exit_game = "0"
fingerprint = "yes"
none = "no"
new_info = input("Where should I check? ")

while new_info != "":

    if new_info == "1":
        print(exploring_station.room_one)
        print("(Officer Dean gets up and walk to detective office)")
        print()
        print("Dean: Hello detective, were you able to find anything from the information I gave you")
        print()
        print("Detective: Yes Officer Dean, we ere able to lift prints from the hat, find where the gun came from, and get more eyewitnesses on where the shooter went.")
        print("All we can do now is wait for the lab to find a match in our system, you can go check the lab and see if they have the results")
        new_info = input("Where should I check? ")


    if new_info == "2":
        print(exploring_station.room_two())
        print("(Dean enters lab)")
        print("Dean: Hey guys did you find anything?")
        answer = input("Lab: ")
        if answer == "yes":
            print("Yes we found a print and ran it through out system. It came back to a Leo Davis. ")
            new_info = input("Where should I check? ")
        elif answer == "no":
            print("No we could not pull anything, maybe you should return to see scene and see if you can find anything new")
            new_info = input("Where should I check? ")
# Should return to Chapter 3 if all evidence was not collected, then run through chapter 4 and 5 again

    elif new_info == "3":
        print(exploring_station.room_three)
        print()
        print("Dean: Hey Vanessa, sorry to bother you, but could we talk for a minute?")
        print("Vanessa: Yeah, sure, what's going on?")
        print("Dean: I just wanted to ask if there was anything else you could remember about what happened yesterday?")
        print("Vanessa: Well they only thing I can think of is the gun who shot the gun didn't seem nervous to shoot, As if it was not his first time shooting someone.")
        print("Dean: So we may be looking at someone with a criminal history?")
        print("Vanessa:That's what it seems like to me")
        print("Dean: Thank you for that information")
        print()
        print("(Dean gets up and leaves)")
        new_info = input("Where should I check? ")

    if new_info == "4":
        print(exploring_station.go_to_computer())
        print()
        print("Leo Davis: 32, male, repeat offender with priors including: assault, battery, and owning an unregistered gun")
        new_info = input("Where should I check? ")

    if new_info == "0":
        print(exploring_station.exit_game())
        print("A few days later...")
        print()
        print("Leo Davis, 32, was arrested for the shooting anf murder of Officer Brian West")
        print("Detective: Good job Officer Dean, thank you for all the help")
        break
