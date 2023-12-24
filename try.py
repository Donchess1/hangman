#!/usr/bin/python3
from category import pick_category
from guess import my_guess
from category import pool


class exam:
    def __init__(self, pool, word, frag):
        self.pool = pool
        self.word = word
        self.frag = frag


word = [*pool]
my_guess()
