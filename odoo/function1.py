import time

start_time = time.time()

n = input()
a = 0
for i in range(0, n):
    a = a + float(i) / float(i + 1)
    print(a)
if __name__ == '__main__':
    print("--- %s seconds ---" % (time.time() - start_time))
