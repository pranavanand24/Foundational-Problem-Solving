def sum0fSeries(n) :
      sum = 0
      for i in range(1 , n+1):
          sum += i*i*i
      return sum

n = 5
print(sum0fSeries(n))