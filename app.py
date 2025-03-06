### HSR Artifact Rater Main Script ###
### Author: Stone Provo ###

### Imports ###
import sys ### Sets path for system to find Flask
sys.path.append('C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages')

import flask
from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import modules
from modules import rate_relic, load_char_data
### Imports ###

app = Flask(__name__)
app.config["DEBUG"] = True


# Navigation routes
@app.route("/", methods=["GET"])
def artifact_rater_home():
    return render_template("Artifact_Rater_Home.html")

@app.route("/artifact_rater", methods=["GET"])
def artifact_rater():    
    return render_template("Artifact_Rater.html")

@app.route("/cached_characters", methods=["GET"])
def cached_characters():
    return render_template("Cached_Characters.html")

# Form Submission
@app.route("/submit_relics", methods=["POST"])
def submit_relics():
    # Process form data
    relic_piece = request.form.get("relic_piece")
    relic_set = request.form.get("relic_set")
    ornament_set = request.form.get("ornament_set")
    head_main_stat = request.form.get("main_stat_head")
    hands_main_stat = request.form.get("main_stat_hands")
    body_main_stat = request.form.get("main_stat_body")
    feet_main_stat = request.form.get("main_stat_feet")
    sphere_main_stat = request.form.get("main_stat_sphere")
    rope_main_stat = request.form.get("main_stat_rope")
    sub_stats = request.form.getlist("sub_stat")


    # Determine what relic set the piece is
    if ornament_set == ("None"):
        rSet=relic_set
    elif relic_set == ("None"):
        rSet=ornament_set

    # Figure out which main stat is the important one
    if relic_piece == ("head"):
        mainStat=head_main_stat
    elif relic_piece == ("hands"):
        mainStat=hands_main_stat
    elif relic_piece == ("body"):
        mainStat=body_main_stat
    elif relic_piece == ("feet"):
        mainStat=feet_main_stat
    elif relic_piece == ("planarSphere"):
        mainStat=sphere_main_stat
    elif relic_piece == ("linkRope"):
        mainStat=rope_main_stat

    char_data=load_char_data()
    char_scores=rate_relic(relic_piece,rSet,mainStat,sub_stats,char_data)
    char_scores=sorted(char_scores, key=lambda x: x["score"], reverse=True)

    
    # Return a JSON response
    return render_template("Artifact_Rater.html", scores=char_scores)


if __name__ == '__main__':
    app.run(debug=True)
    # Runs the Flask app when the script is run
