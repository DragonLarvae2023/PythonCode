import simple_webbrowser as swb

try:
	x = input()
	swb.Google(query=x)
except:
	swb.Google("empty :(")