def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    if n % k == 0:
        sub_list = list(map(''.join, zip(*[iter(string)]*k)))
        for sub in sub_list:
            print("".join(dict.fromkeys(sub)))
    else:
        print("number error. Please try again")
        
    return

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)