from flask import Flask,render_template,request
import uuid,os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/thanvithmk/git clones/Python/Python/CWH/06_VidSnap/user_upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create",methods=["GET","POST"])
def create():
    myid=uuid.uuid1()
    if request.method=="POST":
        print(request.files.keys())
        rec_id=request.form.get("uuid")
        desc=request.form.get("text")
        for key,value in request.files.items():
            print(key,value)
            file=request.files[key]
            if file:
                filename = secure_filename(file.filename)
                os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],rec_id, filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'],rec_id,'desc.txt'),'w') as f:
                f.write(desc)

    return render_template('create.html',myid=myid)
app.run(debug=True)