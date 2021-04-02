par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
def count_char(algo):
    algo = algo.lower()
    for n in algo:
        keys = counts.keys()
        if n != " ":
            if n in keys:
                counts[n] += 1
            else:
                counts[n] = 1
    return counts

print(count_char(par))
