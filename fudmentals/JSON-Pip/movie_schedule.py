current_movie = {
    'Scary movie': '12:00pm',
    'Saw': '3:00pm',
    'Halloween': '6:00pm',
}

print("We're showing the flowwing movies")
for key in current_movie:
    print(key)

movie = input('What movie would uyou like the showtime for?\n')

showtime = current_movie.get(movie)
if showtime == None:
    print("Request showtime isn't playing")
else:
    print(movie, "is playing at", showtime)