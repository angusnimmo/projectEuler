months = [3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]
monthsLeap = [3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6, 2]

day = 2
count = 0

for year in range(1901, 2001):
    if year % 4 == 0:
        for i in monthsLeap:
            if day % 7 == 0:
                count += 1
            day = (day + i + 1) % 7
    else:
        for i in months:
            if day % 7 == 0:
                count += 1
            day = (day + i + 1) % 7

print(count)
