import argparse;

class msg:
    
    def __init__(self, factor, path, musicfile):
        self.factor = factor;
        self.path = path;
        self.musicfile = musicfile;

    # TODO: Implement the functions

    def create_music_script_file(self):
        
    def generate_song_list(self):
        # NOTE: Implementation will only add files with a .ogg ending since
        # CK2 only supports Vorbis-encoded music. It will ignore any
        # subdirectories as well.
        self.songlist = [];
        
    def write_songs_to_file(self):
        for song in songlist:
            songblock  = "song = {\n"
                       + "\tname = \""+song+"\"\n\n"
                       + "\tchance = {\n"
                       + "\t\tmodifier = {\n"
                       + "\t\t\tfactor = "+self.factor+"\n"
                       + "\t\t}\n"
                       + "\t}\n"
                       + "}\n"
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a music script');
    parser.add_argument(["-f", "--factor"], type=float, default=1,
                        help="the factor of occurrence for the music; "
                        "default is 1");
    parser.add_argument(["-p", "--path"], required=True, help="the directory "
                        "where all your music is located; REQUIRED");
    parser.add_argument(["-m", "--musicfile"], default="mysongs.txt",
                        help="the name of your music script; default is "
                        "mysongs.txt");
    args = parser.parse_args();
    
    # TODO: check if the input values are appropriate, otherwise complain and
    # exit the program
    # Specifically, songs file name should end with a .txt, and the path
    # supplied should be valid
    
    msg_obj = msg(args.factor, args.path, args.musicfile);
    msg_obj.create_music_script_file();
    msg_obj.generate_song_list();
