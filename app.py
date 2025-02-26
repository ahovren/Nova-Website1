from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/terms_of_service')
def terms_of_service():
    return render_template('terms_of_service.html')

if __name__ == '__main__':
    app.run(debug=False)
    app.config['PROPAGATE_EXCEPTIONS'] = False
