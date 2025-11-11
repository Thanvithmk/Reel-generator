import os,time
from text_to_audio import text_to_speech_file

def text_to_audio(folder):
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text=f.read()
    text_to_speech_file(text,folder)
    
def create_reel(folder):
    pass

if __name__=="__main__":
        while True:
            with open("done.txt","r") as f:
                done_folders=f.readlines()
            done_folders=[x.strip() for x in done_folders]
            folders=os.listdir("user_uploads")
            for folder in folders:
                if (folder not in done_folders):
                    text_to_audio(folder)
                    create_reel(folder)
                    with open("done.txt","a") as f:
                        f.write(folder+"\n")
            time.sleep(5)