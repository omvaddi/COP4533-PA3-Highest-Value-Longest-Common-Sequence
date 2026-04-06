import time
import matplotlib.pyplot as plt
import sequence

def main():
    runtimes = []
    for i in range(1, 11):
        start = time.perf_counter()

        char_vals, a, b = sequence.read_file("files/file" + str(i) + ".txt")
        value, subsequence = sequence.find_highest_value_subsequence(char_vals, a, b)
        
        end = time.perf_counter()
        runtimes.append(end-start)

    plt.plot(range(1, 11), runtimes, marker='o')
    plt.xlabel("File number")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime for Weighted LCS on multiple inputs")
    plt.grid(True)
    plt.show()

    for i in runtimes:
        print(i)
if __name__ == '__main__':
    main()