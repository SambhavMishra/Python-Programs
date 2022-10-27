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
t = int(input())
for tc in range(t):
    n = int(input())
    tree = {}
    values = {}
    maxi = -99999
    mini = 99999
    for nc in range(n-1):
        (x,y,t,v) = map(int,input().split())
        if t == 1:
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
            values[(x,y)] = values[(y,x)] = v
    # print("Tree = ", tree)
    # print("Values = ", values)
    # print(f"mini = {mini}, maxi = {maxi}")
    total = 0
    for i in range(mini,maxi):
        for j in range(i+1,maxi+1):
            if i == j:
                continue
            else:
                # print(f"going {i} to {j}")
                start = i
                goal = j
                path = [start]
                visited = []
                result = findpath(start,goal,tree,path, visited)
                if result[0] == 1:
                    # print(f"path from {i} to {j} is: {result[1]}")
                    cost = 0
                    path = result[1]
                    n = len(path)
                    for k in range(n-1):
                        cost += values[(path[k],path[k+1])]
                    # print("cost of traversal = ", cost)
                    total += cost
    print(total)
            
                    
            
