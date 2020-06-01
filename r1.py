
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Jerry':
            person = 'Jerry'
            continue
        elif line == 'Laurance':
            person = 'Laurance'
            continue
        if person:
            new.append(person + ':' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w')as f:
        for line in lines:
            f.write(line + '\n')
            write_file(output.txt)

def main():
    lines = read_file('chat.txt')
    lines = convert(lines)
    lines = write_file(filename,lines)