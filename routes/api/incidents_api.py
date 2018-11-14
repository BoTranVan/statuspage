#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import app, jsonify, request
from models import incidents


@app.route('/api/incidents', methods=['GET'],
           defaults={'incident_id': None})
@app.route('/api/incidents/<int:incident_id>', methods=['GET'])
def get_incidents_api(incident_id):
    try:
        lim = request.args.get('limit')
        fr = request.args.get('from')
        if type(request.args.get('deleted')) is str:
            get_deleted = True
        else:
            get_deleted = False
        if request.args.get('id') is not None:
            incident_id = int(request.args.get('id'))
        if incident_id is not None and type(incident_id) is int:
            res = incidents.Incident(id=incident_id).
            get_json(deleted=get_deleted)
            return jsonify(res)
        else:
            res = incidents.Incident().
            get_json(limit=lim, index=fr, deleted=get_deleted)
            return jsonify(res)
    except Exception, e:
        return jsonify({'error': {'message': str(e)}})


@app.route('/api/incidents', methods=['POST'])
def post_incidents_api():
    try:
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
            res = incidents.Incident(name=json_name,
                    message=json_message, status=json_status,
                    visible=json_visible).insert()
            return jsonify(res)
        else:
            return jsonify({'error': {'message': 'Expected a json object'
                           }})
    except Exception, e:
        return jsonify({'error': {'message': str(e)}})


@app.route('/api/incidents/<int:incident_id>', methods=['PUT'])
def put_incidents_api(incident_id):
    try:
        if incident_id is not None and type(incident_id) is int:
            if request.is_json:
                target = incidents.Incident(id=incident_id)
                payload = request.get_json()
                if 'name' in payload:
                    target.update(name=payload['name'])
                if 'message' in payload:
                    target.update(message=payload['message'])
                if 'status' in payload:
                    target.update(status=payload['status'])
                if 'visible' in payload:
                    target.update(visible=payload['visible'])
                return jsonify({'data': 'Update succeeded.'})
            else:
                return jsonify({'error': {'message': 'Expected a json object'
                        }})
        else:
            return jsonify({'error': {'message': "Don't determine incident"
                           }})
    except Exception, e:
        print e
        return jsonify({'error': {'message': str(e)}})


@app.route('/api/incidents', methods=['DELETE'],
           defaults={'incident_id': None})
@app.route('/api/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incidents_api(incident_id):
    try:
        if incident_id is not None and type(incident_id) is int:
            res = incidents.Incident(id=incident_id).delete()
            return jsonify(res)
        else:
            res = incidents.Incident().delete()
            return jsonify(res)
    except Exception, e:
        return jsonify({'error': {'message': str(e)}})
