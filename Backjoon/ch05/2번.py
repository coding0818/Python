def solve():
    all = [i+1 for i in range(10000)]
    for k in range(len(all)):
        new = k + k // 10 + k % 10
        all.remove(new)
    
    for i in range(len(all)):
        print(all[i])