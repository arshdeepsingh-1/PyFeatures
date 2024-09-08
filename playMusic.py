import random
import os

# Define the updated music directory path
music_dir = r'D:\usb data\music'
# Using r is just a convenient way to avoid having to double the backslashes in your file paths.

# List all songs in the music directory
song_list = os.listdir(music_dir)

# Ensure that the directory contains enough songs
if not song_list:
    print("No songs found in the directory!")
else:
    # Generate a random number within the range of the song list length
    n = random.randint(0, len(song_list) - 1)
    print(f"Playing song: {song_list[n]}")

    # Play the randomly selected song
    os.startfile(os.path.join(music_dir, song_list[n]))
