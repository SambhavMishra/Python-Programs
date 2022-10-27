def findpath(i,j,tree,path,visited):
    start = i
    goal = j
    if start not in visited:
        visited.append(start)
        if start not in tree:
            result = [0,[]]
            return result
        if goal in tree[start]:
            path.append(goal)
            return [1,path,goal]
        else:
            for node in range(len(tree[start])):
                tocheck = tree[start][node]
                search = findpath(tocheck,goal,tree,path,visited)
                if search[0] == 1:
                    idx = search[1].index(search[2])
                    search[1].insert(idx,tree[start][node])
                    search[2] = tree[start][node]
                    return search
                elif search[0] == 0:
                    if node != len(tree[start]):
                        return [0,[]]
                elif search[0] == 2:
                    # print("node increased")
                    node += 1
                    search = 2
            if node == len(tree[start]):
                if search == 2:
                    return [2,[]]
                else:
                    return [0,[]]
    else:
        return [2,[]]
n = int(input())
tree = {}
maxi = -99999
mini = 99999
for nc in range(n-1):
    (x,y) = map(int,input().split())
    if y > maxi:
        maxi = y
    if x < mini:
        mini = x
    if x in tree:
        tree[x].append(y)
    else:
        tree[x] = []
        tree[x].append(y)
    if y in tree:
        tree[y].append(x)
    else:
        tree[y]= []
        tree[y].append(x)
print("Tree = ", tree)
print(f"mini = {mini}, maxi = {maxi}")
for i in range(mini,maxi):
    for j in range(i+1,maxi+1):
        if i == j:
            continue
        else:
            print(f"going {i} to {j}")
            start = i
            goal = j
            path = [start]
            visited = []
            result = findpath(start,goal,tree,path, visited)
            if result[0] == 1:
                print(f"path from {i} to {j} is: {result[1]}")
            else:
                print(f"there is no path from {start} to {goal}")
            
                    
            
