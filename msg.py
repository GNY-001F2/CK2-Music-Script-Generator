# CK2 Music Script Generator
# Copyright (C) 2016 Gundam Astraea Type F2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import argparse
import os


class msg:

    def __init__(self, factor, musicfilename):

        self.factor = factor
        self.musicfilename = musicfilename

    # TODO: Implement the functions

    def create_music_script_file(self):

        test = "test"

    def generate_song_list(self):

        # NOTE: Implementation will only add files with a .ogg ending since
        # CK2 only supports Vorbis-encoded music. It will ignore any
        # subdirectories as well.
        self.songlist = []

    def write_songs_to_file(self):

        for song in songlist:

            songblock = ""
            + "song = {\n"
            + "\tname = \""+song+"\"\n\n"
            + "\tchance = {\n"
            + "\t\tmodifier = {\n"
            + "\t\t\tfactor = "+str(self.factor)+"\n"
            + "\t\t}\n"
            + "\t}\n"
            + "}\n"

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate a music script')
    parser.add_argument(["-f", "--factor"], type=float, default=1,
                        help="the factor of occurrence for the music;\n"
                        "default is 1")
    parser.add_argument(["-p", "--path"], default = os.getcwd(), help="the "
                        "absolute directory where all your music is located;\n"
                        "default is your current working directory")
    parser.add_argument(["-m", "--musicfile"], default="mysongs.txt",
                        help="the name of your music script;\ndefault is "
                        "mysongs.txt")
    args = parser.parse_args()

    # TODO: check if the input values are appropriate, otherwise complain and
    # exit the program
    # Specifically, songs file name should end with a .txt, and the path
    # supplied should be valid

    # Handle invalid path
    cwd = os.getcwd()
    if cwd != args.path:
        try:
            cwd = os.chdir(args.path)
        except:
            print("Invalid path specified. Exiting...")
            exit()

    # TODO: check that filename doesn't exceed maximum permitted length
    # TODO: check that the value of factor isn't negative and doesn't exceed
    # the maximum allowed

    msg_obj = msg(args.factor, args.musicfile)
    msg_obj.create_music_script_file()
    msg_obj.generate_song_list()
