from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for charging stations (Replace this with real-time data from your database or scraping)
charging_stations_data =  [
    {
        'name': 'Charging Station 1',
        'location': 'City A, Country',
        'connectors': ['Type 2', 'CHAdeMO'],
        'charging_rate': 'Fast (50 kW)',
        'occupancy': 'Available'
    },
    {
        'name': 'Charging Station 2',
        'location': 'City B, Country',
        'connectors': ['Type 2', 'CCS'],
        'charging_rate': 'Ultra Fast (150 kW)',
        'occupancy': 'Occupied'
    },
    # Add more charging station data as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charging_station/<int:station_id>')
def charging_station_info(station_id):
    charging_station = charging_stations_data[station_id]
    return render_template('charging_station_info.html', charging_station=charging_station)



@app.route('/search', methods=['POST'])
def search_charging_stations():
    current_location = request.form['current_location']
    # You can implement logic to find nearby charging stations based on the user's current location.
    # For this example, we'll just return the sample data for all charging stations.
    return render_template('search_results.html', charging_stations=charging_stations_data)

@app.route('/battery_range', methods=['POST'])
def battery_range_estimation():
    current_battery_percentage = float(request.form['current_battery_percentage'])
    destination_location = request.form['destination_location']
    # You can implement the battery range estimation logic here.
    # For this example, we'll just assume the battery is enough if the percentage is greater than 20%.
    is_enough_battery = current_battery_percentage > 20
    return render_template('battery_range_results.html', is_enough_battery=is_enough_battery)

if __name__ == '__main__':
    app.run(debug=True)
