from flask_frozen import Freezer
from app import app
from os import path

app.config.update(
    FREEZER_IGNORE_MIMETYPE_WARNINGS = True,
    FREEZER_RELATIVE_URLS = False,
    # FREEZER_DESTINATION = path.dirname(path.dirname(__file__)),
    FREEZER_REMOVE_EXTRA_FILES = False
)

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()