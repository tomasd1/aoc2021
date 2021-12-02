# Advent of Code 2021, day 2
# PART 1
acc = {"depth": 0, "pos": 0, "aim": 0}
lines = [line.rstrip() for line in open('data02.txt')]

def down(n): acc["depth"] += n
def up(n): acc["depth"] -= n
def forward(n): acc["pos"] += n

for line in lines:
    command, n = line.split()
    locals()[command](int(n))

print(acc["depth"]*acc["pos"])

# PART 2
def down(n): acc["aim"] += n
def up(n): acc["aim"] -= n
def forward(n): acc["pos"] += n; acc["depth"] += acc["aim"] * n;

for line in lines:
    command, n = line.split()
    locals()[command](int(n))

print(acc["depth"]*acc["pos"])