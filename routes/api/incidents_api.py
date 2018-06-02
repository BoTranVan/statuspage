from config import app, jsonify, request
from models import incidents

@app.route('/api/incidents', methods=['GET'], defaults={'incident_id':None})
@app.route('/api/incidents/<int:incident_id>', methods=['GET'])
def get_incidents_api(incident_id):
    limit = request.args.get('limit')
    fr = request.args.get('from')
    get_deleted = request.args.get('deleted') or False
    if incident_id is not None and type(incident_id) is int:
        res = incidents.Incident(id=incident_id).get_json(deleted=get_deleted)
        return jsonify(res)
    else:
        res = incidents.Incident().get_json(lim=limit, index=fr, deleted=get_deleted)
        return jsonify(res)


@app.route('/api/incidents', methods=['POST'])
def post_incidents_api():
    if request.is_json:
        payload = request.get_json()
        json_name = None
        if 'name' in payload:
            json_name = payload['name']
        json_message = None
        if 'message' in payload:
            json_message = payload['message']
        json_status = 0
        if 'status' in payload:
            json_status = int(payload['status'])
        json_visible = True
        if 'visible' in payload:
            json_visible = bool(payload['visible'])
        # json_component_id = None
        # if 'component_id' in payload:
        #     json_component_id = payload['component_id']
        # json_component_status = 0
        # if 'component_status' in payload:
        #     json_component_status = payload['component_status']
        # json_notify = None
        # if 'notify' in payload:
        #     json_notify = payload['notify']
        # json_template = None
        # if 'template' in payload:
        #     json_template = payload['template']
        res = incidents.Incident(name=json_name, message=json_message, status=json_status, visible=json_visible).insert()
        # component_id=json_component_idcomponent_status=json_component_status, notify=json_notify, template=json_template
        return jsonify(res)

@app.route('/api/incidents', methods=['DELETE'], defaults={'incident_id':None})
@app.route('/api/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incidents_api(incident_id):
    if incident_id is not None and type(incident_id) is int:
        res = incidents.Incident(id=incident_id).delete()
        return jsonify(res)
    else:
        res = incidents.Incident().delete()
        return jsonify(res)
