import requests
import json
import time
import random
import datetime
import logging

def perform_sign_event(user_name, user_cookie):
    wait_time = random.randint(60, 300)
    print(f"Waiting for {wait_time} seconds...")
    time.sleep(wait_time)

    url = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us"
    payload = '{"act_id": "e202102251931481" }'

    header = {
        "Cookie": user_cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
        "Origin": "https://act.hoyolab.com/",
        "Referer": "https://act.hoyolab.com/"
    }

    response = requests.post(url, data=payload, headers=header)
    response_json = response.json()

    print(response_json)

    logger = logging.getLogger(user_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f'{user_name.lower()}log.txt')
    handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
    logger.addHandler(handler)

    logger.info("%s" % response_json)

    time.sleep(5)

def perform_sign_event_hsr(user_name, user_cookie):
    wait_time = random.randint(60, 300)
    print(f"Waiting for {wait_time} seconds...")
    time.sleep(wait_time)

    url = "https://sg-public-api.hoyolab.com/event/luna/os/sign"
    payload = '{"act_id": "e202303301540311" }'

    header = {
        "Cookie": user_cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
        "Origin": "https://act.hoyolab.com/",
        "Referer": "https://act.hoyolab.com/"
    }

    response = requests.post(url, data=payload, headers=header)
    response_json = response.json()

    print(response_json)

    logger = logging.getLogger(user_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f'{user_name.lower()}hsrlog.txt')
    handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
    logger.addHandler(handler)

    logger.info("%s" % response_json)

    time.sleep(5)

# Example usage for John
john_cookie = "PASTE COOKIE HERE" #cookie should look like mi18nLang=en-us; _MHYUUID=randomstuff; DEVICEFP_SEED_ID=randomstuff; DEVICEFP_SEED_TIME=randomstuff; DEVICEFP=randomstuff; ltoken=randomstuff; ltuid=randomstuff; cookie_token=randomstuff; account_id=randomstuff
perform_sign_event("John", john_cookie)

# Example HSR usage for Doe
doe_cookie_hsr = "PASTE COOKIE HERE" #HSR cookie should look like _MHYUUID=randomstuff; DEVICEFP_SEED_ID=randomstuff; DEVICEFP_SEED_TIME=randomstuff; DEVICEFP=randomstuff; mi18nLang=randomstuff; ltoken=randomstuff; ltuid=randomstuff
perform_sign_event_hsr("Doe", doe_cookie_hsr)
