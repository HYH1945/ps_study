import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

answer = []
for _ in range(p):
    level, n = input().split()
    level = int(level)

    done = False
    if(len(rooms) == 0):
        rooms.append([(level, n)])
        done = True
        continue
    
    for room in rooms:
        room_level = room[0][0]

        if len(room) != m and room_level - 10 <= level <= room_level + 10:
            room.append((level, n))
            done = True
            break
    
    if not done:
        rooms.append([(level, n)])
    

for room in rooms:
    room.sort(key=lambda x: (x[1], x[0]))
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in room:
        print(f'{player[0]} {player[1]}')

