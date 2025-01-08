def musicList(musicList):
    print("Available Songs are :")
    for i in musicList:
        print("- ", i)
    
list = ["Lonely", "Cry", "Chunnari Chunnari", "Aurora", "F.R.I.E.N.D.S"]

print("Are there any songs available?")
answer = input()
if answer == "no": print("Sorry, no songs for now-") 
if answer == "yes" : musicList(list)

print("Do u want to play any of the songs?")
wantOrNot = input()
songName = ""
if wantOrNot == "yes" :
    print("Which one? Type the song name.....")
    songName = input()
    if songName != "":
        print(songName, "Playing Now......")
else :
    print("Suit Yourself-")


count = 0
for i in list :
    count += 1
    if songName == i :
        print(songName, "is", count, "number song from the list of available songs-")