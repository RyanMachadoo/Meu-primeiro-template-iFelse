from flask import Flask, render_template
app = Flask('templates')

@app.route('/')
def index():
  return render_template(
    'index.html'
  )
@app.route('/unifran')
def index2():
  return render_template(
    'index2.html'
  )
if __name__ == '__main__':
  app.run(host='0.0.0.0')