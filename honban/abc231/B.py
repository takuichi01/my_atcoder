N = int(input())
koho = {}

for i in range(N):
  S = input()
  
  if S in koho:
    koho[S] += 1
  else:
    koho.setdefault(S, 1)
  
max_k = max(koho, key=koho.get)
print(max_k)
