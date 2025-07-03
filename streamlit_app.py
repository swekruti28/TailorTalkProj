import streamlit as st
import requests
from datetime import datetime, timedelta

st.title("Tailor Appointment Booking")

st.markdown("📅 Book a new appointment to your calendar")

# Input fields
summary = st.text_input("Summary", "Tailoring Appointment")
description = st.text_area("Description", "Custom tailoring request")
date = st.date_input("Date", datetime.now().date())
start_time = st.time_input("Start Time", datetime.now().time())
duration_minutes = st.number_input("Duration (minutes)", min_value=15, value=60, step=15)

if st.button("Book Appointment"):
    start_datetime = datetime.combine(date, start_time)
    end_datetime = start_datetime + timedelta(minutes=duration_minutes)

    payload = {
        "summary": summary,
        "description": description,
        "start": start_datetime.isoformat(),
        "end": end_datetime.isoformat()
    }

    try:
        # Call your FastAPI backend
        response = requests.post("http://127.0.0.1:8000/book", json=payload)
        data = response.json()

        if data.get("status") == "success":
            st.success("✅ Event created successfully!")
            st.markdown(f"[View in Google Calendar]({data['event_link']})")
        else:
            st.error(f"❌ Error: {data.get('message')}")

    except Exception as e:
        st.error(f"Request failed: {e}")
