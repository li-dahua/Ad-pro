import csv
import smtplib

# specify the source and destination CSV files
source_file = "TEST-CountryCodes.csv"
destination_file = "Testing.csv"

# open the source file and read its data
with open(source_file, "r") as src:
    reader = csv.reader(src)
    data = [row for row in reader]

# open the destination file and write the data from the source file
with open(destination_file, "w", newline='') as dest:
    writer = csv.writer(dest)
    writer.writerows(data)

# send a notification email
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls() 
server.login("lidahua@graduate.utm.my", "")

from_email = "lidahua@graduate.utm.my"
to_email = "raylidahua@gmail.com"
subject = "CSV Data Copied"
body = "The data from the source CSV file has been successfully copied to the destination CSV file."

message = f"Subject: {subject}\n\n{body}"

server.sendmail(from_email, to_email, message)
server.quit()
