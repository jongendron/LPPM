import webbrowser
#help(webbrowser)
#webbrowser.open("https://www.python.org/", new=1)
#webbrowser.open_new("https://www.python.org/")

#chrome = webbrowser.get(using='chrome')
#chrome.open_new('https://www.python.org/')

url = 'https://www.python.org/'
browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
browser_path = browser_path + ' %s'
print(browser_path)

webbrowser.get(browser_path).open(url)