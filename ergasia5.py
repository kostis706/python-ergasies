file_in = open("file1.txt", "r")
words = file_in.read().split()
[(word[1:] + word[:1] + "ay") for word in words if len(word) > 3]
