try:
  with open('file1.txt', 'r') as file:
  words = words.split()
  sorted_list = sorted(words, key=len)
  reversed_list = sorted_list[::-1]
  vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
  try:
    long_word_0 = reversed_list[0][::-1] 
    for char in long_word_0:                                    
      if char in vowels:                            
        long_word_0 = long_word_0.replace(char, '') 
    print("1st longest word in the list is: %s" % (long_word_0,))
    try:
      long_word_1 = reversed_list[1][::-1]
      for char in long_word_1:
        if char in vowels:
          long_word_1 = long_word_1.replace(char, '')
      print("2nd longest word in the list is: %s" % (long_word_1,))
      try:
        long_word_2 = reversed_list[2][::-1]
        for char in long_word_2:
          if char in vowels:
            long_word_2 = long_word_2.replace(char, '')
        print("2nd longest word in the list is: %s" % (long_word_2,))
        try:
          long_word_3 = reversed_list[3][::-1]
          for char in long_word_3:
            if char in vowels:
              long_word_3 = long_word_3.replace(char, '')
          print("4th longest word in the list is: %s" % (long_word_3,))
          try:
            long_word_4 = reversed_list[4][::-1]
            for char in long_word_4:
              if char in vowels:
                long_word_4 = long_word_4.replace(char, '')
            print("5th longest word in the list is: %s" % (long_word_4,))