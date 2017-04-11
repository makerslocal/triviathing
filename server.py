#!/usr/bin/env python

from __future__ import print_function

from flask import Flask, jsonify, redirect, request
import json

title_text = "Hello!"
subtitle_text = "Thanks for coming!"
teams = []


app = Flask(__name__)

@app.route('/teams', methods=['GET'])
def get_teams():
	return json.dumps(teams)
@app.route('/teams', methods=['POST'])
def create_team():
	teams.append({
		'name': request.form['name'],
		'emphasis': True,
		'score': 0
	})
	return json.dumps(len(teams)-1)

@app.route('/teams/<id>', methods=['GET'])
def get_team(id):
	return json.dumps(teams[int(id)])
@app.route('/teams/<id>', methods=['POST','PUT'])
def set_team(id):
	id = int(id)
	if 'score' in request.form:
		teams[id]['score'] = int(request.form['score'])
	if 'emphasis' in request.form:
		teams[id]['emphasis'] = (request.form['emphasis'] in ("yes", "true", "True", "checked"))
	return json.dumps(teams[id])

if __name__ == '__main__':
	print("Running")
	app.run(host='0.0.0.0', port=6666, debug=True)

