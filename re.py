import re
from itertools import product
# Input string.
value = "one 1 two 2 three 3"

# Separate on one or more non-digit characters.
result = re.split("\D+", value)
print type(result)
# Print results.

for element in result:
    print(element)

a= [12,21]
b=[12,32]

print list(product(a,b))
