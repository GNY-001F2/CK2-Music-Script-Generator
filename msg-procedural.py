# CK2 Music Script Generator, procedural version
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

if __name__ == "__main__":

    import argparse
    import os

    cwd = os.getcwd()

    parser = \
        argparse.ArgumentParser(description="Generate a CK2 music script",
                                formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", "--factor", type=float, default=1.0,
                        help="The factor of occurrence for the music; "
                        "default is 1.")
    parser.add_argument("-p", "--path", default=os.getcwd(), help="the "
                        "Absolute or relative to current directory path "
                        "where all your music is located; default is your "
                        "current working directory.")
    parser.add_argument("-m", "--musicfile", default="mysongs.txt",
                        help="the name of your music script; default is "
                        "mysongs.txt.\n"
                        "WARNING: This will erase any previous file with the"
                        "same name!")
    parser.add_argument("--conditionfactor", type=float, default=None,
                        help="If set, it will add an initial value of factor "
                        "= <your input value> after the chance attribute")
    parser.add_argument("--conditionfile", default=None, help="If set, it will"
                        " replace the default modifier with your custom "
                        "modifiers for all songs. The file should either be "
                        "stored in the location the music files being written "
                        "to the script.\n"
                        "This will automatically set CONDITIONFACTOR to 1.0 "
                        "if you do not specify a custom CONDITIONFACTOR.")

    args = parser.parse_args()

    if cwd != args.path:

        try:

            os.chdir(args.path)
            cwd = os.getcwd()

        except:

            print("Invalid path specified. Exiting...")
            exit()

    if args.conditionfactor:

        cfset = True

    else:

        cfset = False

    if args.conditionfile:

            try:

                with open(args.conditionfile, 'r'):

                    if not cfset:

                        args.conditionfactor = 1.0

            except:

                print("Your conditionfile does not exist. Either create it or "
                      "use the default modifiers.")
                exit()

    if cfset:

        if args.conditionfactor < 0:
            print("Invalid conditionfactor specified. Please re-run the "
                  "script with a with a conditionfactor > 0 or don't set one.")
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

    __factor = args.factor
    __musicfile = args.musicfile
    __conditionfactor = args.conditionfactor
    __conditionfile = args.conditionfile
    __songlist = []

    # NOTE: Implementation will only add files with a .ogg ending since
    # CK2 only supports Vorbis-encoded music. It will ignore any
    # subdirectories as well.
    # WARNING: Make sure your music is correctly encoded. This script
    # will only check filenames so it is your responsibility to ensure
    # that the content inside is actually playable by the game - ogg
    # containers with vorbis encoded data

    for fname in os.listdir(cwd):
        dirorfilename = os.path.join(cwd, fname)
        if os.path.isfile(dirorfilename) and dirorfilename[-4:] == ".ogg":
                __songlist.append(fname)

    # WARNING: This will erase any previously existing file with the same
    # name!
    musicfile = open(__musicfile, "w")
    musicfile.close()

    with open(__musicfile, "a", encoding='cp1252') as musicfile:

        for song in __songlist:

            # NOTE: This script uses four-space indentations

            songblock = "song = {\n"
            songblock += "    name = \""+song+"\"\n"
            songblock += "    chance = {\n"

            if __conditionfactor:

                songblock += "        factor = "
                songblock += str(__conditionfactor)+"\n"

            if not __conditionfile:

                songblock += "        modifier = {\n"
                songblock += "            factor = "
                songblock += str(__factor)+"\n"
                songblock += "        }\n"

            else:

                with open(__conditionfile, "r") as conditionfile:

                    for line in conditionfile:

                        songblock += "        "+line

            songblock += "    }\n"
            songblock += "}\n\n"
            musicfile.write(songblock)
