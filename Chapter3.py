print("Welcome to Chapter 3")
# after Officer Dean takes all necessary steps he starts to take in the scene
print("Officer Dean takes a step back and takes in the crime scene")
print("He starts to walk around and attempts to find any potential evidence")
print("Officer Dean: First I need to go some gloves and bags in case I find any thing")

class evidence:
    def __init__(evidence, one, two, three, zero):
        evidence.one = one
        evidence.two = two
        evidence.three = three
        evidence.full_list = zero

    def get_ev_one(evidence):
        return evidence.one

    def get_ev_two(evidence):
        return evidence.two

    def get_ev_three(evidence):
        return evidence.three

    def get_full_ev_list(evidence):
        return evidence.fulllist

crime_scene_evidence = evidence("Find bullet", "Find an abandoned hat", "Asses Officer Veronica and Check if she was injured", "All evidence was found")

evidence.one = "1"
evidence.two = "2"
evidence.three = "3"
all_evidence_found = "0"

evidence_found = input("Which direction should I walk in ")

while evidence_found != " ":

    if evidence_found == "1":
        print(crime_scene_evidence.get_ev_one())
        evidence_found = input("Which direction should I walk in ")

    elif  evidence_found == "2":
        print(crime_scene_evidence.get_ev_two())
        evidence_found = input("Which direction should I walk in ")

    elif evidence_found == "3":
        print(crime_scene_evidence.get_ev_three())
        print()
        print("Officer Dean: Veronica were you hit? Do you need to get checked out?")
        print("If there anything else you can tell me about what happened?")
        print("Officer Hath: No I'm fine, this isn't my blood, All I can say is that the gun he used seemed police grade")
        print("He had dark hair, about 5'10, 160 pounds, and was dressed in all black with a red beanie")
        evidence_found = input("Which direction should I walk in ")

    elif evidence_found == "0":
        print("Now that we have found all the evidence available, We just need to wait for the detective to arrive to let them know of my findings")
        break
    else:
        print("This is not an option, please chose an option from above")
        evidence_found = input("Which direction should I walk in ")

# Move on to Chapter 4
