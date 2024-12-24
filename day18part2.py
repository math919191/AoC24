
import re
import heapq

from math import inf

def get_vertices(width, height, blocked_list):
    for x in range(width):
        for y in range(height):
            if (x,y) not in blocked_list:
                yield x,y

def add(coor, coor2):
    return coor[0] + coor2[0], coor[1] + coor2[1]


up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)
dirs = [up, right, down, left]


with open('input/day18.txt') as f: s = f.read()
# systems = s.split('\n\n')
machine_regex = re.compile(
    r"(\d+),(\d+)"
)



coors = machine_regex.findall(s)
blocked_list = []

# width = 7
# height = 7
# num_blocks = 12

width = 71
height = 71
num_blocks = 1024

for match in coors:
    p1, p2 = int(match[0]), int(match[1])
    blocked_list.append((p1, p2))

counter = 0
while True:
    dist = {}
    prev = {}
    # for all u in V
        # make u inf
        # make u prev nil

    for coor in get_vertices(width=width, height=height, blocked_list=blocked_list[:num_blocks + counter]):
        dist[coor] = inf
        prev[coor] = None

    # set the dist for the start to 0
    dist[0,0] = 0

    pq = []
    # make a queue (H) with all V
    for coor in get_vertices(width=width, height=height, blocked_list=blocked_list[:num_blocks + counter]):
        heapq.heappush(pq, (dist[coor], coor))

    # while H is not empty
    while pq:
        # u = get the minimum of H
        _, u = heapq.heappop(pq)
        # for all edges of (u,v) in E
        for dir in dirs:
            v = add(u, dir)
            if not v in prev: continue

            # if dist(v) > dist(u) + l(u,v)
            if dist[v] > dist[u] + 1:
                # dist(v) = dist(u) + l(u,v)
                dist[v] = dist[u] + 1
                prev[v] = u
                # decreaseKey(H,v)
                heapq.heappush(pq, (dist[v], v))

    back_track = []
    curr = (width-1, height-1)

    if prev[curr] is None:
        print(counter + num_blocks - 1)
        print(coors[counter + num_blocks - 1 ])
        break

    print(counter)

    while curr != (0,0):
        back_track.append(curr)
        curr = prev[curr]

    while True:
        counter += 1
        next_to_be_added = blocked_list[num_blocks + counter - 1]
        if next_to_be_added in back_track:
            break
    print(counter)

# ('20', '12') is the correct answer (: