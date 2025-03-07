# ```
# Python has 4 basic Collections

# 1. tuples
# 2. List   Mutable
# 3. set  mutable
# 4. dictionary mutale
# ```

# Using named tupled
import collections


def main():

    Points = collections.namedtuple("point", "x  y")
    p1 = Points(10, 20)
    p2 = Points(20, 40)
    print(p1, p2)


if __name__ == "__main__":
    main()
