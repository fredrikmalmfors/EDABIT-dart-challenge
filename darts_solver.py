import unittest


def darts_solver(sections, darts, target):
    build = inner(sections, darts, target, darts)
    return build_string(build)


def build_string(solutions):
    output = []
    for sol in solutions:
        sol_str = "-".join(str(x) for x in sol)
        output.append(sol_str)
    return output


def inner(sections, darts, target, maximum):
    res = []
    for score in sections:
        if score == target and darts == 1:
            res.append([score])
        elif score <= target:
            next_arrow = inner(sections, darts-1, target-score, maximum)
            if next_arrow:
                for elem in next_arrow:
                    temp = [score]
                    temp.extend(elem)
                    res.append(temp)
    if len(res) > 1:
        for elem in res:
            elem.sort()
        res_unique = []
        for elem in res:
            if elem not in res_unique:
                res_unique.append(elem)
        res = res_unique
    return res


class Test(unittest.TestCase):

    def testAll(self):
        self.assertEqual(darts_solver([3, 6, 8, 11, 15, 19, 22], 3, 35), ["8-8-19"])
        self.assertEqual(darts_solver([2, 4, 7, 10, 13, 18, 24], 3, 29), ["4-7-18"])
        self.assertEqual(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 40), ["11-11-18"])
        self.assertEqual(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 8), [])
        self.assertEqual(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 32), ["3-11-18", "7-7-18", "7-11-14"])
        self.assertEqual(darts_solver([3, 7, 11, 14, 18, 20, 25, 29, 34], 3, 67), ["18-20-29"])
        self.assertEqual(darts_solver([3, 7, 11, 14, 18, 20, 25], 4, 23), ["3-3-3-14"])


if __name__ == '__main__':
    unittest.main()
