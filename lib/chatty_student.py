#!/usr/bin/env python

from student import Student

class ChattyStudent(Student):
    """
    A chatty student who elaborates more when speaking or raising their hand.
    """

    def hello(self):
        """
        Calls the parent's hello() method, then adds a long, chatty message.
        """
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        """
        Calls the parent's raise_hand() method ten times.
        """
        for _ in range(10):
            super().raise_hand()
