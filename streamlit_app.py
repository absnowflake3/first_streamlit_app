Import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)



streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)




import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())



fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
