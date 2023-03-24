import sys

encode_table = {}

shift_amount = 10

for i in range(ord('0'), ord('9') + 1):
    newchar = chr(i)
    encode_table[newchar] = newchar 
    encode_table[newchar.lower()] = newchar.lower()

for i in range(ord('A'), ord('Z') + 1):
    newchar = chr(i)
    encode_table[newchar] = newchar 
    encode_table[newchar.lower()] = newchar.lower()
encode_table['\''] = '\''
encode_table['.'] = '.'
encode_table[' '] = ' '
encode_table[','] = ','
encode_table['!'] = '!'
encode_table['?'] = '?'
encode_table['/'] = '/'
encode_table['\\'] = '\\'
encode_table['\n'] = '\n'

for i in encode_table.keys():
    encode_table[i] = chr(ord(encode_table[i]) + 10)
encode_table[''] = ''
encode_table['\"'] = '\"'
encode_table['-'] = '-'

decode_table = {}
for k, v in encode_table.items():
    decode_table[v] = k
    
if('-e' in sys.argv or '-d' in sys.argv):
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-e' or sys.argv[i] == '-d':
            index = i
if(sys.argv[index] == '-e'):
    with open(sys.argv[index + 1], 'r') as read_file:
        with open(sys.argv[index + 2], 'w') as write_file:
            lines = read_file.readlines()
            for line in lines:
                newline = ""
                for character in line[::-1]:
                    newline += encode_table[character]
                write_file.write(newline)
elif(sys.argv[index] == '-d'):
    with open(sys.argv[index + 1], 'r') as read_file:
        with open(sys.argv[index + 2], 'w') as write_file:
            lines = read_file.readlines()
            for line in lines:
                newline = ""
                for character in line[::-1]:
                    newline += decode_table[character]
                    
                write_file.write(newline)
else:
    print('Please supply -e or -d')
