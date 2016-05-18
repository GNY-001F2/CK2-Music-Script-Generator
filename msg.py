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

cwd = os.getcwd()


class msg:

    def __init__(self, factor, musicfilename):

        self.__factor = factor
        self.__musicfilename = musicfilename
        self.__songlist = []

    def generate_song_list(self):

        # NOTE: Implementation will only add files with a .ogg ending since
        # CK2 only supports Vorbis-encoded music. It will ignore any
        # subdirectories as well.
        # WARNING: Make sure your music is correctly encoded. This script
        # will only check filenames so it is your responsibility to ensure
        # that the content inside is actually playable by the game - ogg
        # containers with vorbis encoded data

        global cwd
        for fname in os.listdir(cwd):
            dirorfilename = os.path.join(cwd, fname)
            if os.path.isfile(dirorfilename) and dirorfilename[-4:] == ".ogg":
                self.__songlist.append(fname)

    def write_songs_to_file(self):

        # WARNING: This will erase any previously existing file with the same
        # name!

        musicfile = open(self.__musicfilename, "w")
        musicfile.close()

        with open(self.__musicfilename, "a", encoding='cp1252') as musicfile:

            for song in self.__songlist:

                songblock = "song = {\n"
                songblock += "\tname = \""+song+"\"\n\n"
                songblock += "\tchance = {\n"
                songblock += "\t\tmodifier = {\n"
                songblock += "\t\t\tfactor = "+str(self.__factor)+"\n"
                songblock += "\t\t}\n"
                songblock += "\t}\n"
                songblock += "}\n\n"
                musicfile.write(songblock)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate a CK2 music script')
    parser.add_argument("-f", "--factor", type=float, default=1.0,
                        help="the factor of occurrence for the music;\n"
                        "default is 1")
    parser.add_argument("-p", "--path", default=os.getcwd(), help="the "
                        "absolute or relative to current directory path "
                        "where all your music is located;\ndefault is your "
                        "current working directory")
    parser.add_argument("-m", "--musicfile", default="mysongs.txt",
                        help="the name of your music script;\ndefault is "
                        "mysongs.txt")

    args = parser.parse_args()

    if cwd != args.path:

        try:

            os.chdir(args.path)
            cwd = os.getcwd()

        except:

            print("Invalid path specified. Exiting...")
            exit()

    if args.musicfile[-4:] != ".txt":

        print("You did not enter a file name that ends with .txt.")
        print("Please re-run the script with the file name corrected.")
        exit()

    if args.factor < 0:

        print("Invalid factor specified. Please re-run the script with a with "
              "a factor > 0 or let me handle it for you with the default "
              "value (1.0)")
        exit()

    msg_obj = msg(args.factor, args.musicfile)
    msg_obj.generate_song_list()
    msg_obj.write_songs_to_file()
