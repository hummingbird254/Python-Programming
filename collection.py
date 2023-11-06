from collections import Counter
from collections import deque
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict

x = "booyiiiii"
my_count = Counter(x)
print(my_count)

print(my_count.most_common(2))  # prints the most common values
print(my_count.most_common(1)[0][0])  # prints the most common  element

print(list(my_count.elements()))
