from collections import Counter
import matplotlib.pyplot as plt


n = int(input())

tags = Counter()

for _ in range(n):
    line = input().split()
    tags_line = line[2:]

    for tag in tags_line:
        tags[tag] += 1

plt.plot(tags)
plt.ylabel('some numbers')
plt.show()

