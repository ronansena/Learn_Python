def count_words(filename):
    """Conta  o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass 
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
    else:  # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']

for filename in filenames: 
    count_words(filename) 

