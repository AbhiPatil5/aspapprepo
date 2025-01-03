import  re
str1="The quick fox born"
str2="The quic fox born"
pattern="quick"
#match= re.match(pattern,str1)  here it check if quick is at start position only
match= re.search(pattern,str1)
if match:
    print("Match Found",match.group())
else:
    print("No match found")

print("-----------------------")
#######################
stringsin = ["The qck fox born","The quick fox born","The quck fox born"]
pattern = r"quick"

for i, checkstr in enumerate(stringsin):
    match = re.search(pattern, checkstr)
    if match:
        print(f"Match found in string {i+1}: {match.group()}")
    else:
        print(f"No match found in string {i+1}")