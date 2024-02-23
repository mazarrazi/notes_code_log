pangram = "The quick brown fox jumps over the lazy dog"  
  
# The .split() method can be applied to a string in Python.  
# It is used to split a string into a list of substrings based on a specified delimiter.  
# If no delimiter is specified,  
# it splits the string based on whitespace characters (spaces, tabs, newlines).  
words = pangram.split() # .split() will look for empty space  
print(words)  
  
num = "9,223,372,036,854,775,807"  
  
# splitting the string  
num_list = num.split(",")  
print(num_list)  
  
# joining the string  
values = ",".join(num_list)  
print(values)  
  
# challenge  
# Use a for loop to produce a list of ints, rather than strings.  
# You can either modify the contents of the 'values' list in place,  
# or create a new list of ints.
