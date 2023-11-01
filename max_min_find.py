from approximation import uf_func

Uf = uf_func(7, 8)[0]


def max_min_find(uf: list[float]):
    minimal = []
    maximal = []
    count = 0
    for cnt in range(0, 4):
        uf_for = uf[count:]

        for j in range(len(uf_for)):
            if uf_for[j] > uf_for[j + 1]:
                count += j
                maximal.append(uf_for[j])
                break

        for i in range(len(uf_for)):
            if uf_for[i] < uf_for[i + 1]:
                count += i
                minimal.append(uf_for[i])
                break

    return maximal, minimal


# print(max_min_find(Uf))
