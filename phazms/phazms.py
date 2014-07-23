#!/usr/bin/env python

import argparse
import random
import sys
import sqlite3
import datetime

MAX_LEN = 3
MIN_LEN = 2
DB_PATH = 'phazms.db'

class Phazms:
    def __init__(self, db_path=DB_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS phazms(id INTEGER PRIMARY KEY, name TEXT, birthdate TEXT)')

    def phazm(self):
        """
        Generates a unique name for phazms.
        """
        chunks = ['Jean', 'Jacques', 'Georges', 'Michel', 'Marcel', 'Raymond', 'Robert', 'Regis', 'Eugene', 'Francois', 'Yves', 'Yvette', 'Gertrude', 'Brigitte', 'Micheline', 'Oui', 'Non', 'Un-Gomme', 'Gros', 'Phil', 'Phil Coupon']
        strength = MIN_LEN + int(random.random() * (MAX_LEN - MIN_LEN))
        phazm = ''
        for i in range(strength):
            if i:
                phazm += '-'
            phazm += chunks[int(len(chunks) * random.random())]
        id = 1
        while True:
            if id > 1:
                trythis = phazm + ' ' + str(id)
            else:
                trythis = phazm
            if not self.exists(trythis):
                break
            id = id + 1
        if id > 1:
            phazm = phazm + ' ' + str(id)
        return self.register(phazm)

    def raw_to_phazm(self, raw):
        return {'id': raw[0], 'name': raw[1], 'birthdate': raw[2]}

    def get_phazms(self):
        res = []
        for p in self.cursor.execute("SELECT * FROM phazms WHERE 1").fetchall():
            res.append(self.raw_to_phazm(p))
        return res

    def get_phazm(self, id):
        return self.raw_to_phazm(self.cursor.execute("SELECT * FROM phazms WHERE id=?", (id,)).fetchall()[0])

    def exists(self, name):
        return self.cursor.execute("SELECT COUNT(*) FROM phazms WHERE name=?", (name, )).fetchone()[0] > 0

    def register(self, name):
        self.cursor.execute('INSERT INTO phazms(name, birthdate) VALUES(?, ?)', (name, str(datetime.datetime.now())))
        self.db.commit()
        return self.get_phazm(self.cursor.lastrowid)
