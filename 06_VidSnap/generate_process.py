import os

def text_to_audio(folder):
            print("TTA - ",folder)

def create_reel(folder):
            print("CR - ",folder)

if __name__=="__main__":
        if not os.path.exists("done.txt"):
            open("done.txt", "w").close()

        with open("done.txt","r") as f:
            done_folders=f.readlines()

        done_folders=[x.strip() for x in done_folders]

        folders=os.listdir("/Users/thanvithmk/git clones/Python/Python/CWH/06_VidSnap/user_upload")

        for folder in folders:
            if(folder not in done_folders):
                    text_to_audio(folder)
                    create_reel(folder)
                    
                    with open("done.txt","a") as f:
                        f.write(folder+"\n")
