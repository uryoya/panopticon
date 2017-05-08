from flask import Flask
from pathlib import Path


project_root = Path('.')
app = Flask(__name__)
app.config.from_pyfile(project_root/'config'/'app.cfg')


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(port=app.config['PORT'], host=app.config['HOST'])

