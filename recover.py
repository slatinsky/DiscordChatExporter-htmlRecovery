import os
import re


def recover_html(filename: str, filecontent: str, message_groups_per_page: int):
	regex = re.compile(r"^(.*?<div class=\"?chatlog\"?>)(.*)(<\/div>\s+<div class=\"?postamble\"?>).*$", re.DOTALL)
	top = regex.sub(r'\1', filecontent)
	middle = regex.sub(r'\2', filecontent)
	bottom = regex.sub(r'\3', filecontent)
	delimeter = r"<div class=\"?chatlog__message-group\"?>"
	messages = [delimeter+x for x in re.split(delimeter, middle) if x]

	for i in range(0, len(messages), message_groups_per_page):
		with open('output/' + filename + "_" + str(round(i / message_groups_per_page)).zfill(6) + '.html'.format(i), 'w', encoding='utf-8') as f:
			f.write(top)
			f.write(''.join(messages[i:i+message_groups_per_page]))
			f.write(bottom)


def main():
	message_groups_per_page = 1000
	for filename in os.listdir("input"):
		if filename.endswith(".html"):
			with open(os.path.join("input", filename), 'r', encoding='utf-8') as f:
				filecontent = f.read()
				recover_html(filename, filecontent, message_groups_per_page)


if __name__ == '__main__':
	main()