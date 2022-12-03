with open('inputs/input03.txt', 'r') as f:
    data = f.readlines()

# Part 1
# Strip newlines
rucksacks = [s.strip() for s in data]
# Split string halfway
compartments = [(set(s[:len(s)//2]),set(s[len(s)//2:])) for s in rucksacks]
# Find intersection of two sets and convert the set back to a string
double_items = [''.join(s[0] & s[1]) for s in compartments]

letters = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26 }
letters = letters | {(key.upper()):(value+26) for (key, value) in letters.items()}

total_priority = sum([letters[s] for s in double_items])
print('Total priority of items:', total_priority)

# Part 2
elf_groups = zip(*(iter(rucksacks),) * 3)
common_items_per_group = [''.join(set(s[0]) & set(s[1]) & set(s[2])) for s in elf_groups]

total_priority_for_badges = sum([letters[s] for s in common_items_per_group])
print('Total priority of badges:', total_priority_for_badges)
