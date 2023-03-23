from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__, template_folder='templates')
with open('/Users/aryanarora/Desktop/Projs/myproject/docs/openaiAPI.txt') as f:
    openai.api_key = f.read().strip()
    
@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/itinerary', methods=['POST'])
def itinerary():
    location = request.form['location']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    location = location.title()
    prompt = f"Input: Itinerary for {location} from: {start_date} to {end_date}\n\nOutput(give day to day and hour by hour itinerary): \n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.9,
      max_tokens=300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )

    itinerary = response.choices[0].text.strip().replace("\n", "<br>")

    return render_template('after_button.html', itinerary=itinerary, location=location, start_date=start_date, end_date=end_date)
