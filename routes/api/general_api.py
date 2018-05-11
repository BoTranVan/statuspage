from config import app, jsonify


@app.route('/api/ping')
def ping():
    res = {'data': 'pong'}
    return jsonify(res)


@app.route('/api/version')
def version():
    res = {
        'meta': {
            'on_latest': True,
            'latest': {
                'tag_name': 'v1.0',
                'prelease': False,
                'draft': False
            }
        },
        'data': '1.0.1-dev'
    }
    return jsonify(res)
