from app import app, db
from app.modules.mod_auth.models import User
from app.modules.mod_buckets.models import Bucket, Link, LinkList


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Bucket': Bucket, 'Link': Link, 'LinkList': LinkList}
