host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com"]
with open(host_path, 'r+') as file :
    content = file.read()
    for website in website_list :
        if website in content :
            pass
        else :
            file.write(redirect + " " + website + "\n")
