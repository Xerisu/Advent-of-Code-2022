with open("mountain.txt", "r") as input:
    mountain = input.readlines()

def print_list(l):
    for row in l:
        for n in row:
            print(str(n), end="")
        #print("")

def print_list_2(l):
    for row in l:
        for n in row:
            print(str(n).rjust(8, ' '), end=" ")
        print("")

def bfs(start, end, list, if_visited, parents):
    Q = []
    if_visited[start[0]][start[1]] = True
    Q.append(start)
    while len(Q) != 0:
        v = Q.pop()

        if v == end:
            length = 0
            while(v != start):
                v = parents[v[0]][v[1]]
                length += 1
            return length
            
        if v[0] != 0:
            if if_visited[v[0] - 1][v[1]] == False and list[v[0] - 1][v[1]] - list[v[0]][v[1]] <= 1:
                if_visited[v[0] - 1][v[1]] = True
                parents[v[0] - 1][v[1]] = v
                Q.insert(0, ((v[0] - 1, v[1])))
        if v[1] != 0:
            if if_visited[v[0]][v[1] - 1] == False and list[v[0]][v[1] - 1] - list[v[0]][v[1]] <= 1:
                if_visited[v[0]][v[1] - 1] = True
                parents[v[0]][v[1] - 1] = v
                Q.insert(0, (v[0], v[1] - 1))
        if v[0] != len(list) - 1:
            if if_visited[v[0] + 1][v[1]] == False and list[v[0] + 1][v[1]] - list[v[0]][v[1]] <= 1:
                if_visited[v[0] + 1][v[1]] = True
                parents[v[0] + 1][v[1]] = v
                Q.insert(0, (v[0] + 1, v[1]))
        if v[1] != len(list[0]) - 1:
            if (not if_visited[v[0]][v[1] + 1]) and list[v[0] ][v[1] + 1] - list[v[0]][v[1]] <= 1:
                if_visited[v[0]][v[1] + 1] = True
                parents[v[0]][v[1] + 1] = v
                Q.insert(0, (v[0], v[1] + 1))

def bfs2(start, end_value, list, if_visited, parents):
    Q = []
    if_visited[start[0]][start[1]] = True
    Q.append(start)
    while len(Q) != 0:
        v = Q.pop()
        if list[v[0]][v[1]] == end_value:
            length = 0
            while(v != start):
                v = parents[v[0]][v[1]]
                length += 1
            return length
            
        if v[0] != 0:
            if if_visited[v[0] - 1][v[1]] == False and list[v[0]][v[1]] - list[v[0] - 1][v[1]] <= 1:
                if_visited[v[0] - 1][v[1]] = True
                parents[v[0] - 1][v[1]] = v
                Q.insert(0, ((v[0] - 1, v[1])))
        if v[1] != 0:
            if if_visited[v[0]][v[1] - 1] == False and list[v[0]][v[1]] - list[v[0]][v[1] - 1] <= 1:
                if_visited[v[0]][v[1] - 1] = True
                parents[v[0]][v[1] - 1] = v
                Q.insert(0, (v[0], v[1] - 1))
        if v[0] != len(list) - 1:
            if if_visited[v[0] + 1][v[1]] == False and list[v[0]][v[1]] - list[v[0] + 1][v[1]]  <= 1:
                if_visited[v[0] + 1][v[1]] = True
                parents[v[0] + 1][v[1]] = v
                Q.insert(0, (v[0] + 1, v[1]))
        if v[1] != len(list[0]) - 1:
            if (not if_visited[v[0]][v[1] + 1]) and list[v[0]][v[1]] - list[v[0] ][v[1] + 1] <= 1:
                if_visited[v[0]][v[1] + 1] = True
                parents[v[0]][v[1] + 1] = v
                Q.insert(0, (v[0], v[1] + 1))

mountain = [m.strip() for m in mountain]
mountain = [[char for char in m] for m in mountain]

if_visited = []
parents = []
starting_point = None
ending_point = None
for i in range(len(mountain)):
    if_visited.append([])
    parents.append([])
    for j in range(len(mountain[0])):
        if mountain[i][j] == "S":
            starting_point = (i,j)
            mountain[i][j] = "a"
        if mountain[i][j] == "E":
            ending_point = (i,j)
            mountain[i][j] = "z"
        mountain[i][j] = ord(mountain[i][j]) - ord("a")
        if_visited[i].append(False)
        parents[i].append(None)


min_len = bfs2(ending_point, 0, mountain, if_visited, parents)


print(min_len)
