import csv

# covid = [('Country', 'Doses', 'People', 'Percentage'),
# ('India', '186Cr', '84.1Cr', 61),
# ('China', '330Cr' '124Cr', 88.1),
# ('United States', '56.8Cr', '21.9Cr', 66.4),
# ('Brazil', '42.4Cr', '16.2Cr', 76.4),
# ('Indonesia', '39Cr', '16.2Cr', 59.3)]

# f=open('Covid.csv','w')
# wrtr=csv.writer(f)

# for t in covid:
#     wrtr.writerow(t)
    
    
# f.close()

# ==============================================


covid = [
{'Country': 'India', 'Doses': '186Cr', 'People':'84.1Cr', 'Percentage':61},
{'Country': 'China', 'Doses': '330Cr', 'People': '124Cr', 'Percentage': 88.1},
{'Country': 'United States', 'Doses': '56.8Cr', 'People': '21.9Cr', 'Percentage': 66.4},
{'Country': 'Brazil', 'Doses': '42.4C', 'People': '16.2Cr', 'Percentage': 76.4},
{'Country': 'Indonesia', 'Doses': '39Cr', 'People': '16.2Cr', 'Percentage':59.3}
]

f=open('CSVDICT.csv','w',newline='')
fields=['Country','Doses','People','Percentage']

wrtr = csv.DictWriter(f,fields)

wrtr.writeheader()

for d in covid:
    wrtr.writerow(d)
    
f.close()
