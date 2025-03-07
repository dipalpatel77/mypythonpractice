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

    fruits = ['apple', 'mango', 'orange'
              'banana', 'apple', 'grape', 'banana', 'banana']

    # fruitCounter = collections.defaultdict(int)
    fruitCounter = collections.defaultdict(lambda: 100)

    print(fruitCounter)

    for fruit in fruits:
        fruitCounter[fruit] += 1

    for (k, v) in fruitCounter.items():
        print(k + ":" + str(v))


if __name__ == "__main__":
    main()
