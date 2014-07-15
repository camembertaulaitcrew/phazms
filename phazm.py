#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import sys

MAX_LEN = 5
MIN_LEN = 2

def phazm():
    chunks = ['Jean', 'Jacques', 'Georges', 'Michel', 'Marcel', 'Raymond', 'Robert', 'Régis', 'Eugène', 'François', 'Yves', 'Yvette', 'Gertrude', 'Brigitte', 'Micheline']
    strength = MIN_LEN + int(random.random() * (MAX_LEN - MIN_LEN))
    phazm = ''
    for i in range(strength):
        if i:
            phazm += '-'
        phazm += chunks[int(len(chunks) * random.random())]
    return phazm

if __name__ == '__main__':
    print 'Bienvenue à %s sur la planète Terre, on va bien s\'amuser!' % phazm()
