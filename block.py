import ctypes
import subprocess
import sys
import dns.resolver
import os
import platform
import shutil
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from fetch_browser_history import get_browser_history

class SiteBlocker:
    def __init__(self):
        self.domains = ["pornhub.com", "xvideos.com", "xnxx.com", "xhamster.com", "rutube.ru",
          "onlyfans.com", "patreon.com", "xvideos.es", "deviantart.com",
          "xhamsterlive.com", "theporndude.com", "redgifs.com", "redtube.com",
          "thisvid.com", "twidouga.net", "xnxx.tv", "xhamster19.com", "hentaila.com",
          "cityheaven.net", "xhamster2.com"]
    def is_admin(self):
        """Check if the script is running with administrative privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def block_website(self, rule_name, ip_address):
        """Block a website by adding a firewall rule."""
        #command = f'netsh advfirewall firewall add rule name="Block Website" dir=out action=block remoteip={ip_address} enable=yes'
        command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=out action=block remoteip={ip_address} enable=yes'
    
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Website with IP {ip_address} has been blocked successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute the command: {e}")

    def blockIP(self, domain):
        if not self.is_admin():
            print("Requesting administrator privileges...")
            # Relaunch script with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            # If already admin, execute the blocking command
            #ip_to_block = "102.132.104.35"  # Replace this with the actual IP
            #result = dns.resolver.resolve("facebook.com", 'A')
            #print("SITE IP ADDRESS: ", result[0].to_text())
            result = dns.resolver.resolve(domain, 'A')  # 'A' record for IPv4 address
            ip_count = 1
            for ip in result:
                print(f"The IP address of {domain} is {ip.to_text()}")
            
                self.block_website("Block_" + domain + "_" + str(ip_count), ip)
                ip_count += 1
    def unblock_website(self, rule_name):
        """Unblock a website by deleting a firewall rule with admin elevation."""
        command = f'netsh advfirewall firewall delete rule name="{rule_name}"'
        ps_command = f'Start-Process powershell -Verb runAs -ArgumentList \'{command}\''
    
        try:
            subprocess.run(["powershell", "-Command", ps_command], shell=True)
            print(f"Firewall rule '{rule_name}' has been removed successfully (with elevation).")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove the rule: {e}")
    def unblockIP(self, domain):
        result = dns.resolver.resolve(domain, 'A')  # 'A' record for IPv4 address
        ip_count = 1
        for ip in result:
            self.unblock_website("Block_" + domain + "_" + str(ip_count))
            ip_count += 1
    def blockAllListedSites(self):
        for domain in self.domains:
            self.blockIP(domain)
    def unblockAllListedSites(self):
        for domain in self.domains:
            self.unblockIP(domain)
    def listWebSiteIPs(self, domain):
        result = dns.resolver.resolve(domain, 'A')  # 'A' record for IPv4 address
        ip_count = 1
        print("Domain Name: ", domain)
        for ip in result:
            print("IP Address: ", ip)
            ip_count += 1

    def is_browser_installed(self, browser_paths):
        for path in browser_paths:
            if shutil.which(path) or os.path.exists(path):
                return True
        return False

    def get_installed_browsers(self):
        system = platform.system()
        browsers = {}

        if system == "Windows":
            browsers = {
                "Google Chrome": [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                ],
                "Mozilla Firefox": [
                    r"C:\Program Files\Mozilla Firefox\firefox.exe",
                    r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
                ],
                "Microsoft Edge": [
                    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
                ],
                "Brave": [
                    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
                    r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
                ],
                "Opera": [
                    r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera\launcher.exe"
                ]
            }

        elif system == "Darwin":  # macOS
            browsers = {
                "Safari": ["/Applications/Safari.app"],
                "Google Chrome": ["/Applications/Google Chrome.app"],
                "Mozilla Firefox": ["/Applications/Firefox.app"],
                "Brave": ["/Applications/Brave Browser.app"],
                "Opera": ["/Applications/Opera.app"]
            }

        elif system == "Linux":
            browsers = {
                "Google Chrome": ["google-chrome", "chrome"],
                "Mozilla Firefox": ["firefox"],
                "Brave": ["brave-browser"],
                "Opera": ["opera"],
                "Chromium": ["chromium", "chromium-browser"]
            }

        installed = []
        for browser, paths in browsers.items():
            if self.is_browser_installed(paths):
                installed.append(browser)

        return installed

    def google_search(self, query, num_results=20):
        print(f"Searching Google for: {query}\n")
        results = search(query, num_results=num_results)
        for index, link in enumerate(results, start=1):
            print(f"{index}. {link}")
    
    def search_google_unfiltered(self, query, num_results=20):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        params = {
            "q": query,
            "num": num_results,
            "safe": "off"  # <-- This disables SafeSearch
        }
        url = "https://www.google.com/search"
        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
    
        links = []
        for g in soup.select('div.g'):
            link_tag = g.find("a")
            if link_tag and link_tag['href']:
                links.append(link_tag['href'])
    
        print(f"\nFound {len(links)} links:")
        for i, link in enumerate(links[:num_results], 1):
            print(f"{i}. {link}")

if __name__ == "__main__":
    site_blocker = SiteBlocker()
    installed_browsers = site_blocker.get_installed_browsers()
    print(installed_browsers)
    get_browser_history(installed_browsers)
    #site_blocker.search_google_unfiltered("")
    #for browser in browsers:
        #print(browser)
