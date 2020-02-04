zombie_chart = [
 [1, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0,]]


# make a queue of zombie locations
# apply moves to subsequent locations and add those zombies to the queue
# get zombie count
def main():
    TIME_TILL_DOOM = 0
    ZOMBIE_QUEUE = []

    ZOMBIE_QUEUE = get_all_zombie_locations(zombie_chart)

    while(ZOMBIE_QUEUE):
        beautify(zombie_chart)
        newly_infected_zombies = []

        # Infect Neighboring Zombies
        for i in range(0, len(ZOMBIE_QUEUE)):
            zombie = ZOMBIE_QUEUE[0]

            row = zombie[0]
            col = zombie[1]

            newly_infected_zombies += infect(zombie_chart, row, col)

            ZOMBIE_QUEUE.remove(zombie)

        ZOMBIE_QUEUE += newly_infected_zombies
        TIME_TILL_DOOM += 1

    print("It will take {} Hours till the world ends".format(TIME_TILL_DOOM))


def infect(zombie_chart, row, col):
    # Check Left
    newly_infected_zombies = []

    if (col > 0):
        if not is_zombie(zombie_chart, row, col-1):
            zombie_chart[row][col-1] = 1
            newly_infected_zombies.append([row, col-1])

    # Check Right
    if col < (len(zombie_chart[0])-1):
        if not is_zombie(zombie_chart, row, col+1):
            zombie_chart[row][col+1] = 1
            newly_infected_zombies.append([row, col+1])
    # Check Up
    if row > 0:
        if not is_zombie(zombie_chart, row-1, col):
            zombie_chart[row-1][col] = 1
            newly_infected_zombies.append([row-1, col])
    # Check Down
    if row < len(zombie_chart) -1:
        if not is_zombie(zombie_chart, row+1, col):
            zombie_chart[row+1][col] = 1
            newly_infected_zombies.append([row+1, col])

    return newly_infected_zombies


def is_zombie(zombie_chart, x, y):
    if zombie_chart[x][y]:
        return 1
    else:
        return 0


# Get Location of all current zombies
def get_all_zombie_locations(zombie_chart):
    current_zombies = []

    for row_index, row in enumerate(zombie_chart):
        for col_index, item in enumerate(row):
            if zombie_chart[row_index][col_index]:
                # print("row {} col {}".format(row_index, col_index))
                current_zombies.append([row_index, col_index])
    return current_zombies


def beautify(zombie_chart):
    for row in zombie_chart:
        print(row)

    print("\n")


if __name__ == '__main__':
    main()
