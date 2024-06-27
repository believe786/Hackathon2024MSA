from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def monitor_my_stress():
  # Define Plot Data 
  labels = [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday',
  ]

  data = [6, 7, 8, 8, 7, 4, 5]
  return render_template(
    template_name_or_list='home.html',
    data=data,
    labels=labels,
    )

@app.route("/analysis")
def analysisOfStressLevel():
  # Define Plot Data 
  # emotionsData = [['Happy', 3],
  #   ['Neutral', 4],
  #   ['Sad', 2],
  #   ['Anxious/Nervous', 5]]

  # # Convert list to dataframe and assign column values
  # emotionsDataDf = pd.DataFrame(emotionsData,
  #   columns=['Emotions','Frequeny'],
  #   index=['a', 'b', 'c', 'd'])
  # # Create Bar chart
  # fig = px.bar(emotionsDataDf, x='Emotions', y='Frequeny', barmode='group')

  # # Create graphJSON
  # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template(
    template_name_or_list='analysisChart.html'
    )


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)