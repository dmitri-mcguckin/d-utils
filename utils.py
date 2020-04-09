#!/usr/bin/env python3
from sys import argv as args
from d_utils.associative import *
from ftf_utilities import log, Mode

def usage(msg = None):
    if(msg is not None): print("Error: " + msg)

    log(Mode.ERROR, "usage: ./utils.py <filename>")

def draw_matrix(alphabet, matrix):
    print("\t-", end=" ")
    for a in alphabet: print(str(a), end=" ")
    print("")

    for i, row in enumerate(matrix):
        print("\t" + str(alphabet[i]), end=" ")
        for col in row:
            print(str(col), end=" ")
        print("")

args = args[1:]

if(len(args) == 0): usage("no file specified!")
filename = args[0]

mod, alphabet, matrix = load_matrix(filename)

log(Mode.INFO, "Mod: " + str(mod) +
               "\nLabels: " + str(alphabet) +
               "\nGenerated Matrix: ")

draw_matrix(alphabet, matrix)

associative = is_associative_closed(mod, alphabet, matrix)
log(Mode.INFO, "Is Associative and Closed: " + str(associative))

if(associative):
    identity = get_identity(alphabet, matrix)
    log(Mode.INFO, "Identity: " + str(identity))

    if(identity is not None):
        inverse = get_inverse(identity, alphabet)
        log(Mode.INFO, "Inverse: " + str(inverse))
