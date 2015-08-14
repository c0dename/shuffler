import glob
import os
import random

listSongs = (glob.glob("*.mp3"))

numOfSongs = len(listSongs)
print("Found "+str(numOfSongs)+" songs...")
print("---------------------------------------------")
print("Shuffling...")
print("---------------------------------------------")

for i in range(len(listSongs)):
    print("Processing "+str(i+1)+" out of "+str(numOfSongs)+"...")
    newName = random.randrange(0,99999)
    os.rename(listSongs[i],str(newName)+".mp3")


print("---------------------------------------------")
print("Shuffle completed!")
print("---------------------------------------------")
