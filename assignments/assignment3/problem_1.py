def subsets(s):
    # Please write your code here
    if len(s) == 0 :
        return [[]]
    
    else:
        prev_subset = subsets(s[:-1])
        return prev_subset + [subset + [s[-1]] for subset in prev_subset]
    


def main():
    print(subsets(["A", "B", "C"]))  # Should print:
    # [[], ['C'], ['B'], ['B', 'C'], ['A'], ['A', 'C'], ['A', 'B'], ['A', 'B', 'C']]

    print(subsets(["K", "L", "M", "Z"]))  # Should print:
    # [[], ['Z'], ['M'], ['M', 'Z'], ['L'], ['L', 'Z'], ['L', 'M'], ['L', 'M', 'Z'], ['K'], ['K', 'Z'], ['K', 'M'],
    # ['K', 'M', 'Z'], ['K', 'L'], ['K', 'L', 'Z'], ['K', 'L', 'M'], ['K', 'L', 'M', 'Z']]


if __name__ == '__main__':
    main()
