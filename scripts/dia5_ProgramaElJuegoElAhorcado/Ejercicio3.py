def argumentos_repetidos(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i-1] == 0:
            return True
    return False

print(argumentos_repetidos(1, 0, 1, 2, 3, 4))
print(argumentos_repetidos(1, 0, 0, 2, 3, 4))