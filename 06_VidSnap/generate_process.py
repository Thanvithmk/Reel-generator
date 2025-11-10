import os

def text_to_audio(folder):
    pass

def create_reel(folder):
    pass

if __name__=="__main__":
    with open("done.txt","r") as f:
        done_folders=f.readlines()
    done_folders=[x.strip() for x in done_folders]
    folders=os.listdir("/Users/thanvithmk/git_clones/Reel-generator/Reel-generator/06_VidSnap/user_uploads")
    for folder in folders:
        if (folder not in done_folders):
            text_to_audio(folder)
            create_reel(folder)
            with open("done.txt","a") as f:
                f.write(folder+"\n")

