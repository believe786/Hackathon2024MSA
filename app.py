from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
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


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)