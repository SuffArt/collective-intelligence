from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag,count=5):
  user_dict={}
  # get the top count' popular posts
  for post1 in get_popular(tag=tag)[0:count]:
     # find all users who posted this
     for post2 in get_urlposts post1['href']):
      user=post2['user']
      user_dict[user]={}
  return user_dict