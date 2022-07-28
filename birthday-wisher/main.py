import datetime as dt
import smtplib
import pandas
import random

# -----------------------------Constants-required---------------------------- #

current = dt.datetime.now()
month = current.month
day = current.day
year = current.year

mail_id = "xyz@gmail.com"
password = "1234"

# -----------------------------Data-from-csv---------------------------- #

data = pandas.read_csv('birthdays.csv')
data = pandas.DataFrame.to_dict(data, orient='records')

l = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']

for i in range(len(data)):
    date = data[i]['day'], data[i]['month'], data[i]['year']

    if day == data[i]['day'] and month == data[i]['month']:
        name = data[i]['name']

        # -----------------------------Files---------------------------- #

        with open(random.choice(l), 'r') as f:
            message_start = f.readline()
            message = f.read()
            message_start = message_start.replace("[NAME]", name)
            final_message = message_start + message

        # -----------------------------Mail---------------------------- #

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=mail_id, password=password)
        connection.sendmail(from_addr=mail_id,
                            to_addrs=f"{data[i]['email']}",
                            msg=f"Subject: It's You Birthday!!!\n\n{final_message}")
        print(name)
        connection.close()





