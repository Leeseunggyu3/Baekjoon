list = list(input())
sum = 0
count = 0

for i in range(len(list)):
    if count == 0:
        sum += 10
    elif list[i] == list[i-1]:
        sum += 5
    elif list[i] != list[i-1]:
        sum += 10
    count+=1
        
print(sum)