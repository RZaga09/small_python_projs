# small plagiarism checker in python
# takes a 5-word snippet from the entered text and searched for similarities with the contents of the first ten google search results of the topic
import urllib

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = input("Enter Topic: ")
text = input("Enter Text: ")
words = text.split()

for i in search(query, tld="com", num=10, stop=10, pause=2):
    urls = urllib.request.urlopen(i)
    webpage = urls.read()
    webpage = webpage.decode(encoding="utf-8")
    for j in range(len(words)):
        try:
            segment = (words[j - 1] + " " + words[j] + " " + words[j + 1] +
                       " " + words[j + 2] + " " + words[j + 3])
            if segment in webpage:
                print(f"Plagiarized: {segment} (from {i})")
        except:
            pass
