#!/usr/bin/env python

class Student:
    """
    A generic student with basic behaviors like greeting and raising their hand.
    This will act as the superclass for ChattyStudent.
    """

    def hello(self):
        """
        Prints a friendly greeting from the student.
        """
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        """
        Prints a message indicating the student wants to participate.
        """
        print("Pick me!")


class ChattyStudent(Student):
    """
    A student who is much more talkative than a regular student.
    Inherits from Student and adds extra chatting behavior.
    """

    def hello(self):
        """
        Calls the parent's hello() method, then adds extra chatty dialogue.
        """
        super().hello()
        print(" want any spoilers? "
              "Okay well let me just tell you who diedHow are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't...")

    def raise_hand(self):
        """
        Calls the parent's raise_hand() method ten times.
        """
        for _ in range(10):
            super().raise_hand()
