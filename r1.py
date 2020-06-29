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
		if line == '張博智':
			person = '張博智'
			continue
		elif line == '王德爲':
			person = '王德爲'
			continue
		elif line == 'Ching Chen':
			person = 'Ching Chen'
			continue
		elif line == '王千豪':
			person = '王千豪'
			continue
		elif line == '林修亦':
			person = '林修亦'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()