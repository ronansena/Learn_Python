with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read() 
    print(contents.rstrip()) 

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object: 
    for line in file_object:
        print(line)


with open(filename) as file_object: 
    lines = file_object.readlines()
    for line in lines: 
        print(line.rstrip())         

pi_string = ''
for line in lines: 
    pi_string += line.rstrip()

print(pi_string) 
print(len(pi_string)) 

filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object: 
    lines = file_object.readlines()

pi_string = ''

for line in lines: 
    pi_string += line.strip()

print(pi_string[:52] + "...") 
print(len(pi_string)) 

with open(filename) as file_object: 
    
    lines = file_object.readlines()
    pi_string = ''

for line in lines: 
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ") 
if birthday in pi_string: 
    print("Your birthday appears in the first million digits of pi!") 
else:
    print("Your birthday does not appear in the first million digits of pi.") 