#!/usr/bin/env python3

class Human:
    def __init__(self):
        self.health = 10
        self.food = 10
        self.sleep = 10

    def sleep(self,amount_of_sleep=8):
        pass

    def cycle(self):
        self.food -= 1
        self.sleep -= 1
        pass

def Main():
    print("Hello!")