print("Welcome to Chapter 4")
print()
print("The rain had stopped as I drove back to the precinct, evidence ready to be tested")
print('Stepping out of my car I make my way inside')

class station:
    def __init__(room, one, two, three, four, zero):
        room.one = one
        room.two = two
        room.three = three
        room.four = four
        room.zero = zero

    def walk_room_one(room):
        return room.one

    def walk_room_two(room):
        return room.two

    def walk_room_three(room):
        return room.three

    def walk_room_four(room):
        return room.four

    def walk_to_car(room):
        return room.zero

enter_room = station("Walk to lab", "Walk to Chief's office", "Walk to interrogation room", "Walk to backroom", "That's all I can do for today, I should go home to get an early start tomorrow")

# recommended  you cycle through each room before choosing option 0
# if invaild input is entered you may need to restart the program
room_one = "1"
room_two = "2"
room_three = "3"
room_four = "4"
room_zero = "0"

station_room = input("Where should I go? ")

while station_room != " ":

    if station_room == "1":
        print(enter_room.walk_room_one())
        print("(Officer Dean enters lab)")
        print()
        print("Officer Dean: Hey guys, this is the evidence I found.\nAny thing you find let us know as soon as possible \nWe need to find out who shot Officer West")
        print()
        print("(Officer Dean exits lab)")
        station_room = input("Where should I go? ")

    elif station_room == "2":
        print(enter_room.walk_room_two())
        print("(Officer Dean enters Chief's office)")
        print()
        print("Hello Chief")
        print()
        print("Chief: Hello Officer Dean, please sit \nCan you please explain what you witnessed today")
        print("Officer Dean: All I know is I arrived on scene and Officer Hath seemed in shock \nI checked on Officer West and he had no pulse \nI assessed Officer Hath \nGot a description of the suspect \nLooked around and found some evidence")
        print("Chief: Okay, thank you for talking to me you are free to go")
        print()
        print("(Officer Dean exits office)")
        station_room = input("Where should I go? ")

    elif station_room == "3":
        print(enter_room.walk_room_three())
        print()
        print("(Enter interrogation room ")
        print("Detective: Hello Officer, please come in \n Now can you please tell us anything you found on the scene")
        print()
        print("Officer Dean: Of course, I found a bullet about 500 ft from the victim, an abandoned red beanie down an allyway the suspect ran \nI was also able to get a description from Hath on what the suspect looked like")
        print("It is all in my notebook, here you go")
        print("(Slides notebook across table)")
        print("Is there anything else I can do for you?")
        print()
        print("Detective: No that is all, thank you")
        print()
        print("(Officer Dean gets up and exits room)")
        station_room = input("Where should I go? ")

    elif station_room == "4":
        print(enter_room.walk_room_four())
        print("Hey Veronica, are you okay")
        print("Veronica: Oh, Hi Dean, yeah I'm doing okay, I think I'm still in some shock, I can't believe that Brian is gone")
        print()
        print("Dean: I know, I can't either, but don't worry we will find who did this, now go home, take the day off and reset \nCome back tomorrow renewed and ready to find the person who killed Brian")
        print()
        print("Veronica: Thank you Dean, this talk really helped, I'll see you tomorrow")
        station_room = input("Where should I go? ")

    elif station_room == "0":
        print(enter_room.walk_to_car())
        break
# Move on to Chapter 5