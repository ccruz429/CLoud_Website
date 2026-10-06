import webbrowser
movie = input("Enter the name of the movie you want to search for: ")
url = f"https://www.youtube.com/results?search_query={movie}"
webbrowser.open(url)
print(f"Searching for '{movie}' on YouTube...")