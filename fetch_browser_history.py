import os
import sqlite3
import shutil
from pathlib import Path
from datetime import datetime, timedelta

def fetch_chrome_history():
    history_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\History')
    temp_path = os.path.join(os.environ['TEMP'], 'chrome_history_copy')
    if not os.path.exists(history_path):
        return "Chrome history not found."

    shutil.copy2(history_path, temp_path)
    conn = sqlite3.connect(temp_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")
    
    result = []
    for url, title, timestamp in cursor.fetchall():
        print(title, url, timestamp)
        if "search" in url or "query" in url or "google.com/search" in url:
            time = datetime(1601, 1, 1) + timedelta(microseconds=timestamp)
            result.append(f"[{time}] {title} - {url}")
    
    conn.close()
    os.remove(temp_path)
    return "\n".join(result) if result else "No search history found in Chrome."

def fetch_edge_history():
    history_path = os.path.join(os.environ['LOCALAPPDATA'], r'Microsoft\Edge\User Data\Default\History')
    temp_path = os.path.join(os.environ['TEMP'], 'edge_history_copy')
    if not os.path.exists(history_path):
        return "Edge history not found."

    shutil.copy2(history_path, temp_path)
    conn = sqlite3.connect(temp_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")
    
    result = []
    for url, title, timestamp in cursor.fetchall():
        print(title, url, timestamp)
        if "search" in url or "query" in url or "bing.com/search" in url:
            time = datetime(1601, 1, 1) + timedelta(microseconds=timestamp)
            result.append(f"[{time}] {title} - {url}")
    
    conn.close()
    os.remove(temp_path)
    return "\n".join(result) if result else "No search history found in Edge."

def fetch_firefox_history():
    firefox_base = os.path.join(os.environ['APPDATA'], r'Mozilla\Firefox\Profiles')
    profile_dirs = [d for d in os.listdir(firefox_base) if ".default" in d]
    if not profile_dirs:
        return "Firefox profile not found."

    profile_path = os.path.join(firefox_base, profile_dirs[0])
    history_path = os.path.join(profile_path, 'places.sqlite')
    temp_path = os.path.join(os.environ['TEMP'], 'firefox_history_copy')
    shutil.copy2(history_path, temp_path)

    conn = sqlite3.connect(temp_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, last_visit_date FROM moz_places ORDER BY last_visit_date DESC")

    result = []
    for url, title, timestamp in cursor.fetchall():
        print(title, url, timestamp)
        if url and ("search" in url or "query" in url or "duckduckgo.com" in url):
            time = datetime(1970, 1, 1) + timedelta(microseconds=timestamp)
            result.append(f"[{time}] {title} - {url}")

    conn.close()
    os.remove(temp_path)
    return "\n".join(result) if result else "No search history found in Firefox."
def get_browser_history(browsers):
    for browser in browsers:
        if browser == "Google Chrome":
            return fetch_chrome_history()
        elif browser == "Microsoft Edge":
            return fetch_edge_history()
        elif browser == "firefox":
            return fetch_firefox_history()
        else:
            return browser + "is not supported yet."
