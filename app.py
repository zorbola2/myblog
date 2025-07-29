from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []
post_id = 1

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post_detail(id):
    post = next((p for p in posts if p['id'] == id), None)
    return render_template('post_detail.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    global post_id
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'id': post_id, 'title': title, 'content': content})
        post_id += 1
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = next((p for p in posts if p['id'] == id), None)
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('index'))
    return render_template('update.html', post=post)

@app.route('/delete/<int:id>')
def delete(id):
    global posts
    posts = [p for p in posts if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)