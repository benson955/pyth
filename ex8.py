#creating a 'template' to pass information in to format accordingly, each data in each block, in order
formatter = "{} {} {} {}"

#passing in numbers, strings, bools, and the formatter string itself, essentially repeating its own process
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
#passing in four strings to put in the brackets
print(formatter.format(
    "Try your", "Own text here", "Maybe a poem", "Or a song about fear"
))
