__author__ = 'aleksander'


fibs = [1, 1]

nextfibref = 2
nextfib = 0
sum = 0

while nextfib <= 4000000:
    nextfib = fibs[nextfibref-2] + fibs[nextfibref-1]
    if nextfib % 2 == 0:
        sum += nextfib
    fibs.append(nextfib)
    nextfibref += 1

print(sum)