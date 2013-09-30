import feedparser

for feedurl in file('feedlist.txt'):
  if feedurl.startswith('#'): continue
  feed = feedparser.parse(feedurl)
  if not feed.feed.has_key ('title'):
  	print ("%s\n" % feedurl)
