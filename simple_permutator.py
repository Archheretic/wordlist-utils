def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

out = open("permutations.txt", "w+")

for p in permute(["Henry", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "June", " ", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", " ", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", " ", "10", "1975"]):
    out.write("".join(p) + '\n')



for p in permute(["Henry", "June", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "June", " ", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "06", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "june", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["henry", "June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "06", " ", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "06.", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "Juni", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Henry", "juni", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["henry", "Juni", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "June", " ", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "June", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "June", " ", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "06", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "june", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["arne", "June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "June", "10", "1975"]):
    out.write("".join(p) + '\n')


for p in permute(["Arne", "Juni", "10", "1975"]):
    out.write("".join(p) + '\n')


for p in permute(["arne", "Juni", "10", "1975"]):
    out.write("".join(p) + '\n')


for p in permute(["Arne", "juni", "10", "1975"]):
    out.write("".join(p) + '\n')


for p in permute(["Arne", "06", " ", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Arne", "06.", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["June", "10", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["June", "10.", "1975"]):
    out.write("".join(p) + '\n')

for p in permute(["Juni", "10", "1975"]):
    out.write("".join(p) + '\n')