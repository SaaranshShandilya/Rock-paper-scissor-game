import random

outcomes = ["rock", "paper", "scissor"]

i = random.randint(0,2)
comp = outcomes[i]

cp_pts = 0
pl_pts = 0
run = 1
while(run):
    inp = str(input("Choose between rock/paper/scissor..."))

    if (inp.lower() == "rock"):
        if(comp.lower() == "rock"):
            print(f"Its a draw, computer chose {comp}")
        elif(comp.lower() == "paper"):
            print(f"You loose, computer chose {comp}")
            cp_pts = cp_pts +1
        elif(comp.lower() == "scissor"):
            print(f"You won, computer chose {comp}")
            pl_pts = pl_pts + 1
    elif(inp.lower() == "paper"):
        if(comp.lower() == "rock"):
            print(f"You won, computer chose {comp}")
            pl_pts = pl_pts + 1
        elif(comp.lower() == "paper"):
            print(f"Its a draw, computer chose {comp}")
        elif(comp.lower() == "scissor"):
            print(f"You loose, computer chose {comp}")
            cp_pts = cp_pts +1
    elif(inp.lower() == "scissor"):
        if(comp.lower() == "rock"):
            print(f"You loose, computer chose {comp}")
            cp_pts = cp_pts +1
        elif(comp.lower() == "paper"):
            print(f"You won, computer chose {comp}")
            pl_pts = pl_pts + 1
        elif(comp.lower() == "scissor"):
            print(f"Its a draw, computer chose {comp}")
    
    ch = str(input("Do you want to play more(Y/N)?"))

    if(ch.lower() == "n"):
        run = 0
        print(f"Final scores are : \nComputer : {cp_pts} \t Player : {pl_pts}")
        if(cp_pts>pl_pts):
            print("The computer won")
        elif(cp_pts == pl_pts):
            print ("Its a draw")
        else:
            print("The player won")
        break

