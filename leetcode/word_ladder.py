# https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/


def find_shortest_chain(dictionary, start, target):
    level = 0
    next_word = ''
    for i in range(len(start)):
        change = start[:i] + target[i] + target[i + 1:]
        if change in dictionary:
            next_word = change
            level += 1
            break




if __name__ == '__main__':
    dictionary = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]
    start = "TOON"
    target = "PLEA"
    find_shortest_chain(dictionary, start, target)
