units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
thousand = 'onethousand'

unitsLen = [len(i) for i in units]
teensLen = [len(i) for i in teens]
tensLen = [len(i) for i in tens]
hundredsLen = [len(i) for i in hundreds]
thousandLen = len(thousand)
andLen = 3

count = 0

for i in unitsLen:
    count += 90 * i
    
for i in teensLen:
    count += 10 * i

for i in tensLen:
    count += 100 * i
    
for i in hundredsLen:
    count += 100 * i
    
count += thousandLen

count += 891 * andLen

print(count)
