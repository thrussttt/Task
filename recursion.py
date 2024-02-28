# Задача:
# Реализуйте рекурсивную функцию для нахождения всех перестановок данной строки символов.

def permutations(s):
    if len(s) <= 1:
        return [s]

    perms = []
    for i, c in enumerate(s):
        for perm in permutations(s[:i] + s[i + 1:]):
            perms.append(c + perm)
    return perms

