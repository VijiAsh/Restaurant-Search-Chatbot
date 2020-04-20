from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import azomatoquery

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ActionCheckLocation(Action):

    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        
        cities=['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh',
                'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 
                'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack','Dehradun','Dhanbad','Bhilai',
                'Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur','Gwalior','Gurgaon','Guwahati',
                'Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur',
                'Kakinada','Kannur','Kanpur','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai',
                'Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida',
                'Patna','Pondicherry','Purulia Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli',
                'Shimla','Siliguri','Solapur','Srinagar','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tiruppur','Ujjain',
                'Bijapur','Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Vellore','Warangal']
        
        cities_lower=[x.lower() for x in cities]
        
        if loc.lower() not in cities_lower:
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
        return


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		zomatoapp = azomatoquery.QueryZomato()
		# Query top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 
		result_json = zomatoapp.search_restaurant(tracker, 5)
		
		# create the response body with resuts from zomato api.
		# The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.
		response=""
		if result_json['results_found'] == 0:
			response= "no results"
		else:
			response="Showing you top rated restaurants:\n"
			count = 1
			for restaurant in result_json['restaurants']:
				response=response+ str(count) + ". \""
				response=response+ str(restaurant['restaurant']['name']) + "\""
				response=response+ "\n\tin "
				response=response+ str(restaurant['restaurant']['location']['address'])
				response=response+ "\n\thas been rated "
				response=response+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+ "\n"
				count += 1
		
		dispatcher.utter_message("-----\n"+response)
		return [SlotSet('location', zomatoapp.loc)]



class ActionSendEmail(Action):

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        zomatoapp = azomatoquery.QueryZomato()
        result_json = zomatoapp.search_restaurant(tracker, 10)
        response=""

        if result_json['results_found'] == 0:
            response= "no results"
        else:
            response="Showing you top rated restaurants:\n"
            count = 1
            for restaurant in result_json['restaurants']:
                response=response+ str(count) + ". \""
                response=response+ str(restaurant['restaurant']['name']) + "\""
                response=response+ "\n\tin "
                response=response+ str(restaurant['restaurant']['location']['address'])
                response=response+ "\n\thas been rated "
                response=response+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+ "\n"
                count += 1

        from_user = 'unave.marunthu01@gmail.com'
        password = 'gbnpgpteqrpsqwie'
        to_user = tracker.get_slot('email')   
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_user, password)
        subject = 'Hello from chatbox'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        body = response
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        server.sendmail(from_user,to_user,text)
        server.close()