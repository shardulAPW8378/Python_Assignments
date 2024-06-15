import os
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def get_process_info():
    try:
        process_info = []
        for process in psutil.process_iter(['pid', 'name', 'username']):
            process_info.append({
                'Name': process.info.get('name', ''),
                'PID': process.info.get('pid', ''),
                'Username': process.info.get('username', '')
            })
        return process_info
    except Exception as e:
        print(f"Error getting process information: {e}")
        return []

def create_log_file(directory):
    try:
        log_file_path = os.path.join(directory, "processes6.log")
        with open(log_file_path, "w") as logfile:
            process_info = get_process_info()
            for process in process_info:
                logfile.write(f"Name: {process['Name']}, PID: {process['PID']}, Username: {process['Username']}\n")
        print(f"Process information logged in '{log_file_path}'.")
        return log_file_path
    except Exception as e:
        print(f"Error creating log file: {e}")
        return None

def send_email(receiver_email, log_file_path):
    try:
        sender_email = "temporary8378@gmail.com"
        sender_password = "xybh vkcb rhkb kbwr"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "Process Information Log"

        
        with open(log_file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(log_file_path)}")

        message.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        print("Log file sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    try:
        directory = input("Enter the directory name where you want to create the log file: ")
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return

        receiver_email = input("Enter the receiver's email address: ")
        
        log_file_path = create_log_file(directory)
        if log_file_path:
            send_email(receiver_email, log_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
