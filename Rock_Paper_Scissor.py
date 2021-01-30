import random
print("Lets Play Rock, Paper and Scissor...")
print("Winner is only decided whosoever 'USER' or 'COMPUTER' wins 5 points early")
print("Use these Initials...")
print("ROCK-R PAPER-P SCISSOR-S")
li=['R','P','S']
cp=up=0
while(1):
    ui=input("Enter R or P or S-->1 2 3 Go... ").upper()
    ci=random.choice(li)
    print(f"Yours Choice: {ui} Computers Choice: {ci}")
    if((ci=='R' and ui=='S') or (ci=='P' and ui=='R') or (ci=='S' and ui=='P')):
        cp+=1
    elif((ui=='R' and ci=='S') or (ui=='P' and ci=='R') or (ui=='S' and ci=='P')):
        up+=1
    else:
        pass
    print(f"Score: User:{up} Computer:{cp}")
    if(cp==5):
        print(f"Better Luck Next Time....COMPUTER WINS with scoreline {cp}:{up}")
        break
    elif(up==5):
        print(f"HURRAYYYYYY!!!....YOU WIN with scoreline {up}:{cp}")
        break     