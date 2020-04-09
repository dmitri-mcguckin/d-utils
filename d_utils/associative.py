from ftf_utilities import log, Mode

def operation(a, b, mod): return (a * b) % mod

def load_matrix(filename):
    file = open(filename)
    raw = file.read()
    file.close()

    pieces = list(map(lambda x: int(x.strip()), raw.split(',')))
    mod = pieces[0]
    alphabet = pieces[1:]
    matrix = []

    for x in alphabet:
        row = []
        for y in alphabet: row.append(operation(x, y, mod))
        matrix.append(row)

    return mod, alphabet, matrix

def is_associative_closed(mod, alphabet, matrix):
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                x = operation(operation(a, b, mod), c, mod)
                y = operation(a, operation(b, c, mod), mod)

                if(x not in alphabet or y not in alphabet):
                    log(Mode.ERROR, "Failed closure test:\n\ta: " + str(a) + ", b: " + str(b) + ", c: " + str(c) + "\n\tx: " + str(x) + "\n\ty: " + str(y))
                    return False

                if(x != y):
                    log(Mode.ERROR, "Failed associativity test:\n\tAlphabet: " + str(alphabet) + "\n\t(" + str(a) + " * " + str(b) + ") * " + str(c) + " = " + str(operation(operation(a, b, mod), c, mod)) + "\n\t" + str(a) + " * (" + str(b) + " * " + str(c) + ") = " + str(operation(a, operation(b, c, mod), mod)))
                    return False
    return True

def get_identity(alphabet, matrix):
    for i, row in enumerate(matrix):
        if(row == alphabet):
            col = []
            for x in range(len(matrix)): col.append(matrix[x][i])
            if(col == alphabet): return alphabet[i]

def get_inverse(e, alphabet):
    # e_i = alphabet.index(e)
    # for i, x in enumerate(alphabet):
    #     if()
    return
