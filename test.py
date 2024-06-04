handle = open("1.txt")

print("/ip firewall address-list")

for line in handle :
    if "route6:" in line:
        continue
    else:
        line = line.split()
        address= line[0]
        print("allow " + address + ";")