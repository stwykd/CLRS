def counting_sort(s):
    ar = [0]*10
    for i in range(len(s)-1):
        ar[S[i]] += 1
    for j in range(len(ar)-1):
        while ar[j] != 0:
            print j
            ar[j] -= 1


def main():
    s = [1, 4, 3, 2, 4, 3, 8, 3]
    print s
    counting_sort(s)


if __name__ == "__main__":
    main()
