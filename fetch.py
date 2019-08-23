URL = "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/family-sponsorship/sponsor-parents-grandparents/tell-us-you-want-sponsor-parent-grandparent.html"
CONFIG_FILE = "config.ini"
CACHED_FILE = "cached-website.html"

import sys
import urllib.request
import configparser

def main():
    print("Cached file: " + CACHED_FILE)

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        from_email = config["EMAIL"]["FROM"]
        to_email = config["EMAIL"]["TO"]
    except:
        print ("Config file or key not found")
    else:
        fp = urllib.request.urlopen(URL)
        website_bytes = fp.read()
        website_content = website_bytes.decode("utf8")
        fp.close()

        cached_file = open(CACHED_FILE, "r", newline='')
        cached_content = cached_file.read()

        if (website_content == cached_content):
            print ("No difference")
        else:
            print ("Has difference")
            send_notificaiton(email)

def send_notificaiton(from_email, to_email):
    print ("Sending email to " + to_email)
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg["Subject"] = "Difference of Canadian Interest to Sponsor form detected"
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content("Possible that the availability of Interest to Sponsor form changes.\nCheck the form at " + URL)

    s = smtplib.SMTP("localhost")
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    main()
