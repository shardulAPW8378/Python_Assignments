import os
import time
import hashlib
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timedelta
from pathlib import Path
from Assignment13Module import *

def delete_duplicates(directory, email):
    duplicates = find_duplicate_files(directory)
    if duplicates:
        marvelous_dir = create_marvelous_directory()
        log_file_path = create_log_file(marvelous_dir)
       # print (log_file)
        log_file=open(log_file_path, "w+")
        for duplicate_set in duplicates:
            for file in duplicate_set[1:]:
                try:
                    os.remove(file)
                    log_file.write(f"{file} deleted.\n")
                except Exception as e:
                    log_file.write(f"Error deleting {file}: {e}\n")
        log_file.close()
        send_email(email,log_file_path)

def send_email(email, attachment):
    subject = "Duplicate File Removal Report"
    body = f"Starting time of scanning: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    body += f"Total number of files scanned: {total_files_scanned}\n"
    body += f"Total number of duplicate files found: {total_duplicate_files}\n"
    
    msg = MIMEMultipart()
    msg['From'] = "temporary8378@gmail.com" # your email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        marvelous_dir = create_marvelous_directory()  # Ensure Marvelous directory exists
        attachment_file = open(attachment, "rb")
        filename = os.path.basename(attachment)
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment_file).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587) # SMTP server
        server.starttls()
        server.login("temporary8378@gmail.com", "xybh vkcb rhkb kbwr") # your email credentials
        text = msg.as_string()
        server.sendmail("temporary8378@gmail.com", email, text)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    print("Welcome to Duplicate File Remover")
    directory = input("Enter the directory path: ")
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return

    duration = int(input("Enter duration in minutes: "))
    email = input("Enter your email: ")

    while True:
        delete_duplicates(directory,email)
        time.sleep(duration * 60)

if __name__ == "__main__":
    main()