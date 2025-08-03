import pandas as pd
file_path = r'C:\Users\HP\Desktop\Student_club_data.csv'
df= pd.read_csv(file_path)

Members= df[df['Clubs'].str.contains('Member', case=False , na=False)]
Members.to_csv(r'C:\Users\HP\Desktop\members_club.csv', index=False)

Organizers= df[df['Clubs'].str.contains('Organiser', case=False, na=False)]
Organizers.to_csv(r'C:\Users\HP\Desktop\organizers_club.csv', index=False)

Volunteers= df[df['Clubs'].str.contains('Volunteer', case=False, na=False)]
Volunteers.to_csv(r'C:\Users\HP\Desktop\volunteers_club.csv', index=False)

print("Filtered files saved to Desktop!")





