from flask import Flask, redirect, render_template, request
import pytube

app = Flask(__name__)



@app.route('/', methods = ['POST', 'GET'])
def download():
    if request.method == 'POST':
        try:
            global title
            ask = request.form.get('link', '')
            path = request.form.get('path', '')
            name = request.form.get('filename', '')
            youtube = pytube.YouTube(ask)
            title = youtube.title
            youtube.streams.first().download(output_path=path)
            return render_template('base.html', title= title, name = name)
        except Exception as e:
            return "<h1>You must Enter a link</h1>"
    return render_template('base.html')




if __name__ == '__main__':
    app.run(debug=True)
