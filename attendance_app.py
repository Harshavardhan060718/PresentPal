import streamlit as st
import pandas as pd
from datetime import datetime

# Read the student-club data
df = pd.read_csv(r'C:\Users\HP\Desktop\Student_club_data.csv')

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
    attendance_data = []
    today = datetime.today().strftime('%Y-%m-%d')
    
    for name, present in attendance.items():
        attendance_data.append({
            'Date': today,
            'Club': selected_club,
            'Student Name': name,
            'Present': 'Yes' if present else 'No'
        })
    
    attendance_df = pd.DataFrame(attendance_data)

    # Save to CSV
    attendance_file = r'C:\Users\HP\Desktop\attendance_records.csv'
    try:
        existing_df = pd.read_csv(attendance_file)
        updated_df = pd.concat([existing_df, attendance_df], ignore_index=True)
        updated_df.to_csv(attendance_file, index=False)
    except FileNotFoundError:
        attendance_df.to_csv(attendance_file, index=False)

    st.success("✅ Attendance recorded successfully!")