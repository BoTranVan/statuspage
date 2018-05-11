from config import app, jsonify
from models import incidents

@app.route('/api/incidents/', methods=['GET'], defaults={'incident':None})
@app.route('/api/incidents/<int:incident>', methods=['GET'])
def get_incidents_api(incident):
    if incident is not None and type(incident) is int:
        target = incidents.Incident(id=incident).get()
        return jsonify({'res': target})
    else:
        print(type(incident))
        return jsonify({'res': incident})
