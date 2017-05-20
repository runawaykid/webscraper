# Open map of address in browser
# test

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

print address

webbrowser.open('https://www.google.com/maps/place/' + address)
