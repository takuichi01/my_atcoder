def main():
  N, M = (int(x) for x in input().split())
  AB = []
  judge = [0]*N
  neighbor = [[]*N]
  flag = 0

  for _ in range(M):
    abc = list(map(int, input().split()))
    AB.append(abc)

  for ab in AB:
    judge[ab[0]-1] += 1
    judge[ab[1]-1] += 1
    neighbor[ab[0]].append(ab[1])
    neighbor[ab[1]].append(ab[0])

    if judge[ab[0]-1] > 2  or  judge[ab[1]-1] > 2:
      print("No")
      return
    elif judge[ab[0]-1] == 1  or  judge[ab[1]-1] == 1:
      for i in range(ab[0]+1, ab[1]):
        if ab[0] in neighbor  or  ab[1] in neighbor:
          flag+= 1
        if flag == 2:
          print("No")
          return


  print("Yes")
  return


main()