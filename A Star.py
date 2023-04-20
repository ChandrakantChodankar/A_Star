tree = [['A', 'H', 7, 0],
        ['A', 'B', 1, 3],
        ['A', 'C', 2, 4],
        ['B', 'D', 4, 2],
        ['B', 'E', 6, 6],
        ['D', 'E', 7, 6],
        ['C', 'F', 3, 3],
        ['C', 'G', 2, 1],
        ['G', 'H', 1, 0],
        ['F', 'H', 2, 0],
        ['D', 'H', 5, 0]]

node = set()
cost = dict()
close = set()
Open = set()
path = dict()

for i in tree:
    node.add(i[0])
    node.add(i[1])
print(node)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

for i in node:
    cost[i] = 999
    path[i] = ' '
Open.add(start)
cost[start] = 0
path[start] = start

def astar(start, goal, tree, Open, close, cost):
    if start in Open:
        Open.remove(start)
        close.add(start)
        for i in tree:
            co = cost[i[0]]+i[2]+i[3]
            if i[0] == start and co < cost[i[1]]:
                Open.add(i[1])
                cost[i[1]] = cost[i[0]]+i[2]+i[3]
                path[i[1]] = path[i[0]]+'->'+i[1]
                cost[i[0]] == 999
        small = min(cost, key=cost.get)
        if small in close:
            astar(small, goal, tree, Open, close, cost)


astar(start, goal, tree, Open, close, cost)
print("The shortest path is ", path[goal])
