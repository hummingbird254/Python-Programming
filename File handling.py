
def append_to_file(file_path, words):
    with open(file_path, 'a') as file:
        file.write(' '.join(words) + ' ')

# Example usage
file_path = 'data.txt'
words_to_append = [ ' so', 'much.']
append_to_file(file_path, words_to_append)

data0=open("data.txt", "r+")
real_data=data0.read()
print(real_data)