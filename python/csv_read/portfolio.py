#filename = "/home/bycho/Programs/git-hub/hello-world/python/csv_read/portfolio.csv"
filename = "python/csv_read/portfolio.csv"
portfolio = []

for line in open(filename):
    fields = line.split(",")
    if fields[0] == 'name' or fields[0][0] == '#':
        continue
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name, shares, price)
    portfolio.append(stock)


total = 0.0
for name, shares, price in portfolio:
    total = shares * price

print (portfolio)
print (f" Total price is {total}")