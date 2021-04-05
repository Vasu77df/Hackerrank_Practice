# Find the number of times a substring occurs in a string 
def count_substring(string, sub_string):
    count = 0
    flag = True
    start = 0

    while flag:
        a = string.find(sub_string, start)
        if a == -1:
            flag = False
        else:
            count += 1
            start = a + 1
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    C = count_substring(string, sub_string)
    print(C)
