import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")



# Validate date
#pattern = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
pattern=r'[0-9]{1,2},-[0-9]{1,2}-[0-9]{4}'
print(re.search(pattern,'15-21-2021'))