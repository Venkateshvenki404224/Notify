from twilio.rest import Client
import datetime
# Getting the day
day = datetime.date.today()
Today = day.strftime("%A")
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'Your SID FROM TWILLO'
auth_token = 'YOUR AUTH-TOKEN'
client = Client(account_sid, auth_token)
timetable = {
    "Monday": {
        '08:30-09:30': "ED",
        '09:30-10:30': "Pysics",
        '10:30-02:00': "Cs Lab",
        '02:00-03:00': "Maths",
        '03:00-04:00': "Cs",
        '04:00-05:00': "Physics"
    },
    "Tuesday": {
        '08:30-09:30': "ED",
        '09:30-10:30': "Cs",
        '10:30-11:30': "Maths",
        '11:30-12:30': "Physics",
        '01:00-04:00': "Maths Lab"
    },
    "Wednesday": {
        '09:30-10:30': "Maths",
        '10:30-11:30': "Cs",
        '11:30-12:00': "Physics",
        '01:00-04:00': "Maths Lab",
        '04:00-05:00': "Cs"
    },
    "Thursday": {
        '09:30-12:30': "Pysics Lab",
        '01:00-02:00': "Cs",
        '02:00-03:00': "Maths",
        '03:00-04:00': "Physics"
    },
    "Friday": {
        '09:30-10:30': "Cs",
        '10:30-11:30': "Physics",
        '11:30-12:30': "Maths",
        '01:00-04:00': "Physics Lab",
        '04:00-05:00': "Maths"
    },
    "Saturday": {
        '9:30-12:30': "Cs Lab"
    },
}
Day = timetable.get(Today)
message = client.messages.create(
                              body=f'Your Time Table for today is{Day}',
                              from_='+16205828628',
                              to='Your Mobile Number'
                          )
print(message.status)
