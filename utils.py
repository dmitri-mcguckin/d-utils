#!/usr/bin/env python3
from sys import argv as args
from d_utils.associative import *
from ftf_utilities import log, Mode

def usage(msg = None):
    if(msg is not None): print("Error: " + msg)

    log(Mode.ERROR, "usage: ./utils.py <filename>")

args = args[1:]

if(len(args) == 0): usage("no file specified!")
filename = args[0]

mod, labels, matrix = load_matrix(filename)

log(Mode.INFO, "Mod: " + str(mod) +
               "\nLabels: " + str(labels) +
               "\nData: " + str(matrix))

log(Mode.INFO, "Is Associative: " + str(is_associative(labels, matrix)))
