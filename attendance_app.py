import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('attendanceppal-1681b9b1fe82.json', scope)
client = gspread.authorize(creds)
sheet = client.open("ppal_attendance").worksheet("Attendance")

# Read the student-club data
df = pd.read_csv(r'Student_club_data.csv')

# Extracting unique clubs
all_clubs = set()
for clubs in df['Clubs'].dropna():
    club_list = [club.strip() for club in clubs.split(',')]
    all_clubs.update(club_list)

# Dropdown to select club
selected_club = st.selectbox("Select a Club", sorted(all_clubs))

# Filter students for the selected club
filtered_students = df[df['Clubs'].str.contains(selected_club, case=False, na=False)]

st.write(f"### Members in {selected_club} ({len(filtered_students)})")

# Attendance checkboxes
attendance = {}
for idx, row in filtered_students.iterrows():
    attendance[row['Name']] = st.checkbox(row['Name'])

# Save attendance on button click
if st.button("Submit Attendance"):
    today = datetime.today().strftime('%Y-%m-%d')
    
    for name, present in attendance.items():
        sheet.append_row([today, selected_club, name, "Yes" if present else "No"])
    
    st.success("✅ Attendance recorded successfully in Google Sheets!")
