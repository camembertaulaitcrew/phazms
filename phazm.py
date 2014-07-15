#!/usr/bin/env python

import argparse
import random
import sys
import sqlite3
import datetime

MAX_LEN = 5
MIN_LEN = 2
DB_PATH = 'phazms.db'

class Phazms:
    def __init__(self):
        self.db = sqlite3.connect(DB_PATH)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS phazms(name TEXT, birthdate TEXT)')

    def phazm(self):
        """
        Generates a unique name for phazms.
        """
        chunks = ['Jean', 'Jacques', 'Georges', 'Michel', 'Marcel', 'Raymond', 'Robert', 'Regis', 'Eugene', 'Francois', 'Yves', 'Yvette', 'Gertrude', 'Brigitte', 'Micheline', 'Oui', 'Non', 'Un-Gomme', 'Gros']
        strength = MIN_LEN + int(random.random() * (MAX_LEN - MIN_LEN))
        phazm = ''
        for i in range(strength):
            if i:
                phazm += '-'
            phazm += chunks[int(len(chunks) * random.random())]
        id = 0
        while self.exists(phazm):
            id += 1
        if id > 0:
            phazm = phazm + ' ' + str(id)
        self.register(phazm)
        return phazm

    def exists(self, name):
        return self.cursor.execute("SELECT COUNT(*) FROM phazms WHERE name=?", (name, )).fetchone() == 0

    def register(self, name):
        self.cursor.execute('INSERT INTO phazms(name, birthdate) VALUES(?, ?)', (name, str(datetime.datetime.now())))
        self.db.commit()

if __name__ == '__main__':
    p = Phazms()
    print 'Bienvenue a %s sur la planete Terre, on va bien s\'amuser!' % p.phazm()
