from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *


@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
@app.rout("/charts", methods=['GET', 'POST'])
def stocks():
    
    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                #Generate error message as pass to the page
                err = "ERROR: End date cannot be earlier than Start date."
                chart = None
            else:
                #query the api using the form data
                err = None
                 
                #THIS IS WHERE YOU WILL CALL THE METHODS FROM THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE
            

                
                
                if chart_Choice == 1:
                    # Bar code
                    bar_chart = pygal.Bar(x_label_rotation=20)
                    bar_chart.title = 'Stock Data for ' + stock_symbol + ': ' + date_B_Choice + ' to ' + date_E_Choice
                    bar_chart.x_labels = map(str, json_date_key)
                    bar_chart.add('Open', json_open)
                    bar_chart.add('High', json_high)
                    bar_chart.add('Low', json_low)
                    bar_chart.add('Close', json_close)
                    bar_chart.render_in_browser()
                    # line code
                elif chart_Choice == 2:
                    line_chart = pygal.Line(x_label_rotation=20)
                    line_chart.title = 'Stock Data for ' + stock_symbol + ': ' + date_B_Choice + ' to ' + date_E_Choice
                    line_chart.x_labels = map(str, json_date_key)
                    line_chart.add('Open', json_open)
                    line_chart.add('High', json_high)
                    line_chart.add('Low', json_low)
                    line_chart.add('Close', json_close)
                    line_chart.render_in_browser()
                
                
                
                #This chart variable is what is passed to the stock.html page to render the chart returned from the api
                chart = "ASSIGN CHART TO THIS VARIABLE"

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")
