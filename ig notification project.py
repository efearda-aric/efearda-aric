from tkinter import Tk, Label, Entry, Button, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class InstagramNotifierUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Notifier")

    
        self.label_profile_url = Label(root, text="Enter Instagram Profile URL:")
        self.entry_profile_url = Entry(root, width=30)
        self.label_profile_url.grid(row=0, column=0, padx=10, pady=10)
        self.entry_profile_url.grid(row=0, column=1, padx=10, pady=10)

      
        self.label_email = Label(root, text="Enter your Email:")
        self.entry_email = Entry(root, width=30)
        self.label_email.grid(row=1, column=0, padx=10, pady=10)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

      
        self.start_button = Button(root, text="Start Notifier", command=self.start_notifier)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

    def start_notifier(self):
       
        profile_url = self.entry_profile_url.get()
        to_email = self.entry_email.get()

   
        if not profile_url or not to_email:
            messagebox.showerror("Error", "Please enter both Instagram profile URL and your email.")
            return

 
        driver = webdriver.Chrome()

        try:
       
            driver.get(profile_url)

         
            wait = WebDriverWait(driver, 10)
            latest_post = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_aagw")))

           
            username = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d603w9']").text
            type_of_post = "photo" if latest_post.find_element_by_class_name("_aabd") else "video"
            timestamp = latest_post.find_element_by_class_name("c-Yi7").text

            messagebox.showinfo("New Instagram Post", f"New post from {username}:\nType: {type_of_post}\nTimestamp: {timestamp}")

           
            subject = f"New Instagram Post from {username}"
            message = f"New post from {username} on Instagram.\nType: {type_of_post}\nTimestamp: {timestamp}"
            self.send_email(to_email, subject, message)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
           
            driver.quit()

    @staticmethod
    def send_email(to_email, subject, message):
       

        email_address = "your_email@gmail.com"
        email_password = "your_email_password"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)

       
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

    
        server.send_message(msg)


        server.quit()

root = Tk()
app = InstagramNotifierUI(root)
root.mainloop()

def send_email(to_email, subject, message):
    
    email_address = "your_email@gmail.com"
    email_password = "your_email_password"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)

    
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)

    server.quit()


driver = webdriver.Chrome()


driver.get("https://www.instagram.com/accounts/login/")

driver.get("https://www.instagram.com/0_eaa_0/")

wait = WebDriverWait(driver, 10)
latest_post = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_aagw")))


username = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d603w9']").text
type_of_post = "photo" if latest_post.find_element_by_class_name("_aabd") else "video"
timestamp = latest_post.find_element_by_class_name("c-Yi7").text


print(f"New post from {username}:")
print(f"Type: {type_of_post}")
print(f"Timestamp: {timestamp}")


to_email = input("Enter your email address for notifications: ")

subject = f"New Instagram Post from {username}"
message = f"New post from {username} on Instagram.\nType: {type_of_post}\nTimestamp: {timestamp}"
send_email(to_email, subject, message)


driver.quit()
