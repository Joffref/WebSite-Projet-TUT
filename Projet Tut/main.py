from flask import Flask, render_template
import folium

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/map')
def mappage():
    i = 0
    j = 0
    coords_list = [47.494352, 6.802859, 47.510758, 6.801416, 47.633792, 6.853809, 47.0, 7.0, 47.1, 7.0, 0]
    altitude = [600, 610, 620, 700, 900]
    basement_coords = (47.494352, 6.802859)
    map = folium.Map(location=basement_coords, tiles='OpenStreetMap', zoom_start=15)
    while coords_list[i] != 0:
        coords = [coords_list[i],coords_list[i+1]]
        folium.Marker(location=coords, popup = "Altitude {}".format(altitude[j])).add_to(map)
        i += 2
        j += 1
    return map._repr_html_()

@app.route('/teams')
def team():
    return render_template("teams.html")

@app.route('/project specification')
def project():
    return render_template("project.html")

@app.route('/testimonial')
def testimonial():
    return render_template("testimonial.html")

if __name__ == '__main__':
    app.run(debug=True)