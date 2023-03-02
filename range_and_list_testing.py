place = [2]
stack = []
bad = 0

for i in range(3, 20):
    for item in place:
        numb = i//item
        leftover = i - (numb*item)
        if leftover == 0:
            bad = 1
    if bad == 0:
        place.append(i)
        bad = 0
    else:
        bad = 0

