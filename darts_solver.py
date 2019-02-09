import itertools


def darts_solver(sections, darts, target):

    build = inner(sections, darts, target, darts)

    return build_string(build)


def build_string(solutions):

    output = []

    for sol in solutions:
        sol_str = "-".join(sol)
        output.append(sol_str)

    return output


def inner(sections, darts, target, maximum):
    res = []

    for score in sections:
        if score == target and darts == 1:
            res.append([str(score)])
        elif score <= target:
            next_arrow = inner(sections, darts-1, target-score, maximum)
            if next_arrow:
                for elem in next_arrow:
                    temp = [str(score)]
                    temp.extend(elem)
                    res.append(temp)
    if len(res) > 1:
        for elem in res:
            elem.sort()
        res = list(res for res, _ in itertools.groupby(res))
    return res


print(darts_solver([3, 6, 8, 11, 15, 19, 22], 3, 35))
