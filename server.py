from flask import Flask, render_template_string
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
    <head>
        <title>Button Press Counter</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){
                for (let i = 0; i < 2; i++) {
                    $("#reset-button" + i).click(function(){
                        $.post("/reset/" + i);
                    });
                }
                setInterval(fetchCounts, 500);
                function fetchCounts(){
                    for (let i = 0; i < 2; i++) {
                        $.get("/count/" + i, function(data){
                            $("#actuations" + i).text(data.actuations);
                            $("#actuations_per_min" + i).text(data.actuations_per_min);
                            $("#actuations_per_hr" + i).text(data.actuations_per_hr);
                        });
                    }
                }
            });
        </script>
    </head>
    <body>
        <h1>Motor 0 Actuation Total: <span id="actuations0">0</span></h1>
        <h1>RPM: <span id="actuations_per_min0">0</span></h1>
        <h1>RPH: <span id="actuations_per_hr0">0</span></h1>
        <button id="reset-button0">Reset All</button>

        <h1>Motor 1 Actuation Total: <span id="actuations1">0</span></h1>
        <h1>RPM: <span id="actuations_per_min1">0</span></h1>
        <h1>RPH: <span id="actuations_per_hr1">0</span></h1>
        <button id="reset-button1">Reset All</button>
    </body>
</html>
    """)

@app.route("/count/<int:button_index>")
def count(button_index):
    with open('count{}.csv'.format(button_index), 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            timestamp, actuations, actuations_per_min, actuations_per_hr = row
    return {'timestamp': timestamp, 'actuations': actuations, 'actuations_per_min': actuations_per_min, 'actuations_per_hr': actuations_per_hr}

@app.route("/reset/<int:button_index>", methods=['POST'])
def reset(button_index):
    with open('reset{}.txt'.format(button_index), 'w') as file:
        file.write('reset')
    return '', 204

if __name__ == "__main__":
    app.run(host='0.0.0.0')
