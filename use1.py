import linecache
line = linecache.getline("/etc/passwd",44)
fields = line.split(":")
print(fields[0])
