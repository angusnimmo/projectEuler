test = list(range(2, 5*(9**5)))
store = []

for i in test:
    if i == int(sum([int(j)**5 for j in str(i)])):
        store.append(i)

print(sum(store))
