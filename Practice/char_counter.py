import sys


def count_chars(filename):
    with open(filename) as f:
        data = f.read()

    all_chars = len(data)
    
    data = data.replace(" ", "")
    data = data.replace("\t", "")
    data = data.replace("\n", "")

    return all_chars, len(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter filename: ")
    
    # not bad
    # totals = count_chars(filename)
    # print("Total chars:", totals[0])
    # print("Total chars (no spaces):", totals[1])

    # better
    total_all_chars, total_no_spaces = count_chars(filename)
    print("Total chars:", total_all_chars)
    print("Total chars (no spaces):", total_no_spaces)
