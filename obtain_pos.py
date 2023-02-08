

def get_julia_pos():
    with open('pos_jul.txt') as f:
        lines = f.readlines()

    return [complex(line) for line in lines]


def get_man_pos():
    with open('pos_man.txt') as f:
        lines = f.readlines()

    coord = [float(line.split()[1]) for line in lines]
    positions = [coord[x:x+4] for x in range(0, len(coord), 4)]
    return [[(pos[0]+pos[1])/2, (pos[2]+pos[3])/2, (pos[3]-pos[2])/2] for pos in positions]
