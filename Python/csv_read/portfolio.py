#filename = "/home/bycho/Programs/git-hub/hello-world/python/csv_read/portfolio.csv"
filename = "Python/csv_read/portfolio.csv"
portfolio = []

ff = open(filename,'r')
for line in ff:
    fields = line.split(",")
    if fields[0] == 'name' or fields[0][0] == '#':
        continue
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name, shares, price)
    portfolio.append(stock)

ff.close()

total = 0.0
total_shares = 0.0
for name, shares, price in portfolio:
    total += shares * price
    total_shares += shares

print (portfolio)
print (f" Total name is {len(portfolio)}")
print (f" Total shares is {total_shares}")
print (f" Total price is {total}")