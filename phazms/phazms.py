#!/usr/bin/env python

import argparse
import random
import sys
import sqlite3
import datetime

MAX_LEN = 3
MIN_LEN = 2
DB_PATH = '/tmp/phazms.db'

class Phazms:
    chunks = [
        'Jean', 'Jacques', 'Georges', 'Michel', 'Marcel', 'Raymond',
        'Robert', 'Regis', 'Eugene', 'Francois', 'Yves', 'Yvette',
        'Gertrude', 'Brigitte', 'Micheline', 'Oui', 'Non', 'Un-Gomme',
        'Gros', 'Phil', 'Phil Coupon', 'Gertrude', 'Philemon', 'Daniel',
        'Esteban', 'David', 'Antoine', 'Diego', 'Junior', 'Gerard', 'Charles',
        'Michael', 'Regis', 'Anakin', 'Renaud', 'Yannick', 'Sebastien',
        'Manfred', 'Julien', 'Vadim', 'James', 'Louis', 'Gregoire', 'Vincent',
        'Nicolas', 'Sarah', 'Jeanne', 'Daniel', 'Marie', 'Steve', 'Romain',
        'Pierre', 'Coralie', 'Laurent', 'Esteban', 'Axel', 'Richard', 'Bob',
        'Eude', 'Bastien', 'Yann', 'Edouard', 'Bobby', 'Christian', 'Nathan',
        'Alex', 'Aline', 'Momo', 'Sylvain', 'Mohamed', 'Jackie', 'Michelle',
        'Jacquie', 'Rodolphe', 'Auguste', 'Augustin', 'Hypolite', 'Gregory',
        'Jacqueline', 'Rodrigo', 'Maurice', 'Rocco', 'Chang', 'Bruce', 'Nassim',
        'Gwendal', 'Leo', 'Leonard', 'Enzo', 'Claire', 'Manon', 'Camille',
        'Jonathan', 'Solvik', 'Gordon', 'Murdoch', 'Anakin', 'Kyle', 'Ken',
        'Ryu', 'Agatha',
    ]

    def __init__(self, db_path=DB_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS phazms('
            '  id INTEGER PRIMARY KEY, '
            '  name TEXT, '
            '  birthdate TEXT, '
            '  owner TEXT'
            ')')

    def phazm(self, owner):
        """
        Generates a unique name for phazms.
        """
        strength = MIN_LEN + int(round(random.random(), 0) * (MAX_LEN - MIN_LEN))
        phazm = ''
        for i in range(strength):
            if i:
                phazm += '-'
            phazm += self.chunks[int(len(self.chunks) * random.random())]
        id_ = 1
        while True:
            if id_ > 1:
                trythis = phazm + ' ' + str(id_)
            else:
                trythis = phazm
            if not self.exists(trythis):
                break
            id_ = id_ + 1
        if id_ > 1:
            phazm = phazm + ' ' + str(id_)
        return self.register(phazm, owner)

    def raw_to_phazm(self, raw):
        return {'id': raw[0], 'name': raw[1], 'birthdate': raw[2], 'owner': raw[3]}

    def get_phazms(self):
        res = []
        for p in self.cursor.execute("SELECT * FROM phazms WHERE 1").fetchall():
            res.append(self.raw_to_phazm(p))
        return res

    def get_phazm(self, id_):
        return self.raw_to_phazm(self.cursor.execute(
            "SELECT * FROM phazms WHERE id=?", (id_,)
        ).fetchall()[0])

    def exists(self, name):
        return self.cursor.execute(
            "SELECT COUNT(*) FROM phazms WHERE name=?", (name, )
        ).fetchone()[0] > 0

    def register(self, name, owner):
        self.cursor.execute(
            'INSERT INTO phazms(name, birthdate, owner) VALUES(?, ?, ?)',
            (name, str(datetime.datetime.now()), owner)
        )
        self.db.commit()
        return self.get_phazm(self.cursor.lastrowid)
