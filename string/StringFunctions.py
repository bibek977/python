story='''Once upon a time there was a king Halard and his queen Lagartha. They loved each other. The end.'''
print(story[0::2])

story1=story.replace(" ",",")
print(story1)
print(story1[0::2])

print(len(story))
print(story.find("er"))
print(story.count("a"))
print(story.endswith("."))
print(story.capitalize())
print(story.replace("Halard","Bibek"))