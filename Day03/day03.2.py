with open('Day03/input','r') as f: input = f.read()
(wire1, wire2) = input.split('\n')

def make_path(wire):
    directions = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    visited = {}
    current = (0,0)
    steps = 0
    moves = wire.split(',')
    for move in moves:
        direction = directions[move[0]]
        length = int(move[1:])
        for _ in range(0,length):
            steps += 1
            current = (current[0] + direction[0], current[1] + direction[1])
            if current not in visited:
                visited[current] = steps
            
    return visited

(path1, path2) = (make_path(wire1), make_path(wire2))
intersections = set(path1.keys()).intersection(set(path2.keys()))
distances = [path1[x] + path2[x] for x in intersections]
print(min(distances))