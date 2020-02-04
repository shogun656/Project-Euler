# For question https://leetcode.com/discuss/interview-question/460127/


def top_n_buzzwords(numToys, topToys, toys, numQuotes, quotes):
    toys_dict = {}
    toys_quotes = {}
    for toy in toys:
        toys_dict[toy] = 0
        toys_quotes[toy] = []

    # Count how many times each words in said in the quotes
    count_words(toys_dict, toys_quotes, toys, quotes)

    # get number of quotes each word is in
    reduce_quotes(toys_quotes)

    # Sort the toys
    sorted_toys = sort_toys(toys_dict, toys_quotes)

    # another way to sort is this monstrosity i found online
    # result = [w[0] for w in sorted(toys_freq.items(), key=lambda x: (-x[1][0],-x[1][1],x[0]))[:N]]

    for i in range(0, topToys):
        print(sorted_toys[i][0])


def count_words(toys_dict, toys_quotes, toys, quotes):
    i = 1
    for quote in quotes:
        for word in quote.split():
            # lowercase and remove all special chars
            word = word.lower().translate(None, '!@#$')
            if word in toys:
                toys_dict[word] += 1
                toys_quotes[word].append(i)
        i += 1


def reduce_quotes(toys_quotes):
    for toy, num in toys_quotes.items():
        toys_quotes[toy] = len(set(num))


def sort_toys(toys, toys_quotes):
    sorted_toys = sorted(toys.items(), key=lambda x: x[1])
    sorted_toys.reverse()

    for i in range(0, len(sorted_toys)):
        if i != 0:
            first_toy = sorted_toys[i - 1]
            second_toy = sorted_toys[i]
            # if found the same amount of times
            if first_toy[1] == second_toy[1]:
                # quote check
                if toys_quotes[second_toy[0]] > toys_quotes[first_toy[0]]:
                    sorted_toys[i - 1] = second_toy
                    sorted_toys[i] = first_toy
                elif toys_quotes[second_toy[0]] == toys_quotes[first_toy[0]]:
                    # if toys are mentioned an equal number of times in
                    # quotes, sort alphabetically.
                    if len(second_toy[0]) > len(first_toy[0]):
                        sorted_toys[i - 1] = second_toy
                        sorted_toys[i] = first_toy
    return sorted_toys


if __name__ == "__main__":
    top_n_buzzwords(
        6,
        2,
        ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"],
        6,
        [
            "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
            "The new Elmo dolls are super high quality",
            "Expect the Elsa dolls to be very popular this year, Elsa!",
            "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
            "For parents of older kids, look into buying them a drone",
            "Warcraft is slowly rising in popularity ahead of the holiday season"
        ])
