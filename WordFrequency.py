f = "text.txt"
f = open(f, "r")


wli = []


for l in f:
    l = l.split()

    for w in l:
        wli.append(w)

wli.sort()

wd = {}

for w in wli:
    wd[w] = wli.count(w)

print("\n{:8}{:8}".format("Word", "Count"))


for w in wd:
    print("{:8}{:^8d}".format(w, wd[w]))

print("")
