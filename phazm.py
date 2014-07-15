#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import sys
import sqlite3

MAX_LEN = 5
MIN_LEN = 2

def exists(name):
    return False

def register(name):
    return True

def phazm():
    """
    Generates a unique name for phazms.
    """
    chunks = ['Jean', 'Jacques', 'Georges', 'Michel', 'Marcel', 'Raymond', 'Robert', 'Régis', 'Eugène', 'François', 'Yves', 'Yvette', 'Gertrude', 'Brigitte', 'Micheline', 'Oui', 'Non', 'Un-Gomme', 'Gros']
    strength = MIN_LEN + int(random.random() * (MAX_LEN - MIN_LEN))
    phazm = ''
    for i in range(strength):
        if i:
            phazm += '-'
        phazm += chunks[int(len(chunks) * random.random())]
    id = 0
    while exists(phazm):
        id += 1
    phazm = phazm + ' ' + str(id)
    register(phazm)
    return phazm

if __name__ == '__main__':
    print 'Bienvenue à %s sur la planète Terre, on va bien s\'amuser!' % phazm()
