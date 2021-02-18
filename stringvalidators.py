# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical 
# characters, digits, lowercase and uppercase characters.
def string_checker(s):
    alnum_flag = False
    alpha_flag = False
    digit_flag = False
    lower_flag - False
    upper_flag = True
    for i in range(0, len(s)):
        print(s[i].isalnum())
        print(s[i].isalpha())
        print(s[i].isdigit())
        print(s[i].islower())
        print(s[i].isupper())

if __name__ == "__main__":
    s = input()
    string_checker(s)