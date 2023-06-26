#
# You work at a music streaming service and have been tasked with creating a program to manage user playlists. Your program should allow the user to perform various operations on a set of songs in a playlist, including adding songs, removing songs, and checking if a specific song is in the playlist.
#
# Here are the steps to follow:
#
# 1.	Create an empty set called playlist to store the songs.
# 2.	Use a while loop to repeat the following operations until the user chooses to exit:
# •	Display a menu of options to the user:
# o	Add song
# o	Remove song
# o	Check if song exists
# o	Exit
# •	Ask the user to select an option by entering the corresponding number.
# •	Based on the user's choice, perform the corresponding operation.
# •	Display the result to the user.


playlist = set()

while True:
    print("\nMenu:")
    print("1. Add song")
    print("2. Remove song")
    print("3. Check if song exists")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        song = input("Enter the name of the song to add: ")
        playlist.add(song)
        print(f"The song '{song}' has been added to the playlist.")

    elif choice == 2:
        song = input("Enter the name of the song to remove: ")
        if song in playlist:
            playlist.remove(song)
            print(f"The song '{song}' has been removed from the playlist.")
        else:
            print(f"The song '{song}' is not in the playlist.")

    elif choice == 3:
        song = input("Enter the name of the song to check: ")
        if song in playlist:
            print(f"The song '{song}' is in the playlist.")
        else:
            print(f"The song '{song}' is not in the playlist.")

    elif choice == 4:
        break

print("Thank you for using the playlist manager!")

