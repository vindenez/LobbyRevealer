import requests
import time
import json

def fetch_userinfo():
    api_url = "https:///rso-auth/v1/authorization/userinfo?"  # Replace with the actual API URL
    response = requests.get(api_url)
    userinfo = json.loads(response.text)
    if response.status_code == 200 and response.content:
        print(userinfo)
    return None

def fetch_lobby_participants():
    api_url = "/rso-auth/v1/authorization/userinfo"  # Replace with the actual API URL
    response = requests.get(api_url)
    if response.status_code == 200 and response.content:
        participants_json = json.loads(response.text)
        if participants_json and "participants" in participants_json:
            names = [participant["name"] for participant in participants_json["participants"] if "name" in participant]
            return names
    return None

def update_participants(fetched_data):
    participants = []  # Reset participants list
    if fetched_data:
        for data in fetched_data:
            participant_info = {
                'game_name': data['game_name'],
                'game_tag': data['game_tag'],
                'region': data['region']
            }
            participants.append(participant_info)
    return participants

def display_participants(participants):
    print("Updated lobby participants:")
    for participant in participants:
        print(f"{participant['game_name']}#{participant['game_tag']} from {participant['region']}")

def main():
    while True:
        fetch_userinfo()
        time.sleep(3)  # Sleep for 10 seconds before updating again

if __name__ == "__main__":
    main()
