#  write your code here 
summer_txt = open("./data/dataset/input.txt", "r")

count = 0
for row in summer_txt:
    if row == "summer\n":
        count += 1

print(count)
