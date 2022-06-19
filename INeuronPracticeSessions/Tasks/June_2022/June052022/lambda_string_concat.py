# Try to write a lambda function which can return a concatination of all the string that we will pass
concat_string = lambda *s, sep=" ": sep.join(s)
print(concat_string("a", "b", sep=".."))