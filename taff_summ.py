raw = [x.split(" ")  for x in open("log_small.txt")]
print(type(raw))

print(raw)

rmp = {}
for ip, traffic in raw:
    if ip in rmp:
            rmp[ip] += int(traffic)
    else:
            rmp[ip] = int(traffic)

print(rmp)

lst = rmp.items()
lst.sort(key = lambda (key, val): key)
print "\n".join(["%s\t%d" % (host, traff) for host, traff in lst])