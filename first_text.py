""" this runs our program """
import cmd
import threading, sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import textwrap
from room import get_room



def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("./music/intro.mp3")
    pygame.mixer.music.play()


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        cmd.Cmd.prompt = ':'
        """cmd.Cmd.doc_header = "" <- change this later """
        """ If no save exists print out motd """
        """ Else we print a return message to continue game"""
        print("""
                    .---..    .       .  .   .  .           .
                    |    |    |        \  \ /  /            |
                    |--- | .-.| .-. .--.\  \  /.-.  .-.  .-.|
                    |    |(   |(.-' |  | \/ \/(   )(   )(   |
                    '---'`-`-'`-`--''  `- ' '  `-'  `-'  `-'`-

================================================================================
""")
        print("Welcome adventurer, to the world of EldenWood!")

        self.loc = get_room(0)
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("You cannot go that way.")
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self):
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)


    def do_n(self, args):
        """Go North"""
        self.move('n')

    def do_s(self, args):
        """Go South"""
        self.move('s')

    def do_e(self, args):
        """Go East"""
        self.move('e')

    def do_w(self, args):
        """Go West"""
        self.move('w')

    def do_quit(self, args):
        """Quits execution of the game """
        print("Thanks for playing!")
        pygame.mixer.stop()
        pygame.mixer.quit()
        return True

if __name__ == "__main__":
    g = Game()
    play_music()
    g.cmdloop()
