import streamlit as st 
import requests as r

api="e6c256c40692ee4029aea0bb17fbea55"

city=st.text_input("enter city name.. ")

response=r.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}")


data=response.json()

print(data)






if response.status_code == 200:
        st.write("City:", data["name"])
        st.write("Country:", data["sys"]["country"])
        st.write("Temperature (°C):", data["main"]["temp"])
        st.write("Weather:", data["weather"][0]["main"])
        st.write("Description:", data["weather"][0]["description"])
        st.write("Humidity (%):", data["main"]["humidity"])
        st.write("Wind Speed (m/s):", data["wind"]["speed"])
else:
        st.error("City not found. Please enter a valid city name.")