
day1 = list(map(int, open('day01.input').readlines()))

for i in range(len(day1)):
    for j in range(len(day1)-1):
        if (day1[i] + day1[j+1]) == 2020:
            print(day1[i] * day1[j+1])
        for k in range(len(day1)-2):
            if day1[i] + day1[j+1] + day1[k+2] == 2020:
                print(day1[i] * day1[j+1] * day1[k+2])
                exit()
