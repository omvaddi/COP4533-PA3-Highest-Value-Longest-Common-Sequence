def read_file(filename):

    char_vals = {}
    with open(filename, 'r') as f:
        num_characters = int(f.readline().strip())
        
        for _ in range(num_characters):
            char, val = f.readline().strip().split()
            char_vals[char] = int(val)

        a = f.readline().strip()
        b = f.readline().strip()

    return char_vals, a, b

def find_highest_value_subsequence(char_vals, a, b):

    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + char_vals[a[i - 1]]
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    sol = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            sol.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return dp[n][m], ''.join(reversed(sol))



def main():
    file_name = input('Enter the file name: ')
    char_vals, a, b = read_file(file_name)
    value, subsequence = find_highest_value_subsequence(char_vals, a, b)
    print(value)
    print(subsequence)

if __name__ == '__main__':
    main()
