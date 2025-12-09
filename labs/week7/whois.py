# whois looks up details like regestration date of domain, when it
# expires, who owns it, contact informatio, nameserver info, and
# which registar the domain was purchased woith

import socket
import requests
import sys


def get_domain_info(key,domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Ip Address: {ip}")
        # Using API requires API key, this is passed in on command line for safety
        url = f"https://api.ipapi.com/{ip}?access_key={key}&format=1"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Organisation: {data.get('org', 'Unknown')}")
            print(f"City: {data.get('city', 'Unknown')}")
            print(f"Country: {data.get('country_name', 'Unknown')}")
        else:
            print("Could not fetch WHOIS data")
    except Exception as e:
        print(f"ERROR: {e}")


# Info passed in by running on command line
get_domain_info(sys.argv[1], sys.argv[2])