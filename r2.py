def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines


def convert(lines):
	person = None
	andrew_word_count = 0
	andrew_s_count = 0
	andrew_i_count = 0
	kyle_word_count = 0
	kyle_s_count = 0
	kyle_i_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'KYLE':
			if s[2] == '貼圖':
				kyle_s_count += 1
			else:
				for m in s[2:]:
					kyle_word_count += len(m)
		elif name == 'Andrew':
			if s[2] == '貼圖':
				andrew_s_count += 1
			else:
				for m in s[2:]:
					andrew_word_count += len(m)

	print('Kyle sent ', kyle_word_count, 'word(s)')
	print('Kyle sent ', kyle_s_count, 'sitcker(s)')
	print('Kyle sent ', kyle_i_count, 'image(s)')
	print('Andrew sent ', andrew_word_count, 'word(s)')
	print('Andrew sent ', andrew_s_count, 'sticker(s)')
	print('Andrew sent ', andrew_i_count, 'image(s)')
	return lines


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]KYLE1.txt')
	lines = convert(lines)
	write_file('output1.txt', lines)

main()