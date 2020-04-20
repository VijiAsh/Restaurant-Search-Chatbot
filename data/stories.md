## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiashk@gmail.com"}
    - slot{"email":"vijiashk@gmail.com"}
    - action_send_email
    - utter_info_emailsent
    - action_restart


## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai","cuisine":"american"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"cuisine":"american"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* deny
    - utter_email_deny
    - action_restart


## location price specified
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price":"Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiash@gmail.com"}
    - slot{"email":"vijiash@gmail.com"}
    - action_send_email
    - utter_info_emailsent
    - action_restart

## location price specified
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nYauatcha in Raheja Towers, Bandra Kurla Complex, Mumbai has been rated 4.7\n And the average price for two people is: 2800\nPa Pa Ya in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nPa Pa Ya in G-2, Ground Floor, Third, North Avenue, Maker Maxity, Bandra Kurla Complex, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nHakkasan in 206, Krystal, Waterfield Road, Linking Road, Bandra West has been rated 4.5\n And the average price for two people is: 2600\nMamagoto in 133, Ground Floor, Gazebo House, Hill Road, Bandra West, Mumbai, Maharashtra has been rated 4.5\n And the average price for two people is: 1500\nPa Pa Ya in Hotel Diplomat, Whitehouse Building, 24 - 26, B.K Boman Behram Marg, Apollo Bunder, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2000\nJia The Oriental Kitchen in 2, Dhanraj Mahal, C. S. Marg, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2500\nShaollin Temple in Krishna Avtar Building, Plot F/3, Palm Beach Road, Sector 14, CBD-Belapur, Navi Mumbai has been rated 4.4\n And the average price for two people is: 1000\nChina Bistro in Ground Floor, Infinity Shopping Complex, Vasant Vihar, Thane West has been rated 4.4\n And the average price for two people is: 1500\nThe Fatty Bao in Shop 1, Ground Floor, Sentinel Building, Hiranandani Business Park, Powai, Mumbai has been rated 4.3\n And the average price for two people is: 1800\n"}
    - utter_ask_sendemail
* deny
    - utter_email_deny
    - action_restart


## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* deny
    - utter_email_deny


## complete path 3
* greet
    - utter_greet
* restaurant_search{"location": "chennai","cuisine": "south indian"}
    - action_check_location
    - slot{"location": "south indian"}
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiash@gmail.com"}
    - slot{"email":"vijiash@gmail.com"}
    - action_send_email
    - utter_info_emailsent


## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai","cuisine": "Italian"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiash@gmail.com"}
    - slot{"email":"vijiash@gmail.com"}
    - action_send_email
    - utter_info_emailsent

## story1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ooty"}
    - slot{"location": "Ooty"}
    - action_check_location
    - utter_location_limit
    - action_listen

## story2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Heenaur"}
    - slot{"location": "Heenaur"}
    - action_check_location
    - utter_location_limit
    - action_listen

## story3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - utter_location_limit
    - action_listen

## story4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - utter_location_limit
    - action_listen

## story5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - utter_location_limit
    - action_listen


## story6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - utter_location_limit
    - action_listen

## story7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ooty"}
    - slot{"location": "Ooty"}
    - action_check_location
    - utter_location_limit
    - action_listen



## story2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiash@gmail.com"}
    - slot{"email":"vijiash@gmail.com"}
    - action_send_email
    - utter_info_emailsent

## story3
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "south indian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"email":"vijiash@gmail.com"}
    - slot{"email":"vijiash@gmail.com"}
    - action_send_email
    - utter_info_emailsent

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - action_listen
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"email": "viji@gmail.com"}
    - slot{"email": "viji@gmail.com"}
    - action_send_email
    - utter_info_emailsent
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "Madsd"}
    - slot{"location": "Madsd"}
    - action_check_location
    - action_listen
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"email": "viji@gmail.com"}
    - slot{"email": "viji@gmail.com"}
    - action_send_email
    - utter_info_emailsent


## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - action_listen
* restaurant_search{"location": "Erode"}
    - slot{"location": "Erode"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"email": "viji@gmail.com"}
    - slot{"email": "viji@gmail.com"}
    - action_send_email
    - utter_info_emailsent


## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - action_listen
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_search_restaurants
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"email": "viji@gmail.com"}
    - slot{"email": "viji@gmail.com"}
    - action_send_email
    - utter_info_emailsent




## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - action_search_restaurants
    - utter_ask_sendemail
* deny
    - utter_email_deny

