from flask import Flask
from main import run_full_pipeline

app = Flask(__name__)

@app.route('/log')

def run():
    run_full_pipeline()
    return ''

if __name__ == '__main__':
    app.run()