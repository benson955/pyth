#a string wtih tab spacing in front
tabby_cat = "\tI'm tabbed in."
#a string with new line in between
persian_cat = "I'm split\non a line."
#a string with \ done with escapes
backslash_cat = "I'm \\ a \\ cat."

#a paragraph with tabs, new lines inside
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#a string combining a few of the tricks
print ("this is a \n relatively more complex \'string\' being \\printed\\")

#a format of 3 variables and using in a printing string
formatter = "%s %s %s"
print (formatter %("a", "b", "c"))