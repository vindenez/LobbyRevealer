import requests
import base64
import os
import platform
import time

def read_lockfile(lockfile_path):
    with open(lockfile_path, 'r') as file:
        data = file.read().split(':')
        return {
            'port': data[2],
            'password': data[3]
        }

def get_lcu_api_base_url(port):
    return f"https://127.0.0.1:{port}"

def get_auth_header(password):
    token = base64.b64encode(f"riot:{password}".encode('utf-8')).decode('utf-8')
    return {"Authorization": f"Basic {token}"}

def get_lockfile_path():
    os_name = platform.system()
    if os_name == "Windows":
        return os.path.join("C:\\Riot Games\\League of Legends", "lockfile")
    elif os_name == "Darwin":  # macOS
        return os.path.join("/Applications/League of Legends.app/Contents/LoL", "lockfile")
    else:
        print("Unsupported OS")
        return None

def main():
    lockfile_path = get_lockfile_path()
    if lockfile_path and os.path.exists(lockfile_path):
        lockfile_info = read_lockfile(lockfile_path)
        base_url = get_lcu_api_base_url(lockfile_info['port'])
        headers = get_auth_header(lockfile_info['password'])

        # Request to get champ-select participants
        #response = requests.get(f"{base_url}/chat/v5/participants/champ-select", headers=headers, verify=False)
        res = ""
        baseurl = ""

        while True:
            response = requests.get(f"{base_url}/chat/v5/participants/champ-select", headers=headers, verify=False)
            lockfile_path and os.path.exists(lockfile_path)
            lockfile_info = read_lockfile(lockfile_path)
            base_url = get_lcu_api_base_url(lockfile_info['port'])
            if res != response.status_code:
                res = response.status_code
                print(res)
            if baseurl != get_lcu_api_base_url(lockfile_info['port']):
                baseurl = get_lcu_api_base_url(lockfile_info['port'])
                print(baseurl)
            
            time.sleep(3)


        if response.status_code == 200:
            participants_info = response.json()
            # Process participants_info as needed, for example:
            print(f"Champ Select Participants: {participants_info}")
        else:
            #print("Failed to fetch champ select participants")
            print(base_url)
    else:
        print("Lockfile not found. Ensure League of Legends is running.")

    

if __name__ == "__main__":
    main()

