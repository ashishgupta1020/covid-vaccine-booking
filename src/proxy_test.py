import requests, datetime, random
from fake_useragent import UserAgent

def getProxyDict():
    list = [
        "https://117.197.119.151:8080",
    ]
    proxy = random.choice(list)
    print(f"chosen proxy: {proxy}")

    return {
        "https" : proxy
    }

try:
        ua = UserAgent(use_cache_server=False, verify_ssl=False)
        request_header = {
            'User-Agent': ua.random,
            'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate'
        }
        
        print(
            "==================================================================================="
        )
        today = datetime.datetime.today() + datetime.timedelta(days=1)
        today = today.strftime("%d-%m-%Y")
        base_url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date={today}"

        options = []
        resp = requests.get(
            base_url,
            headers=request_header,
            proxies=getProxyDict()
        )

        if resp.status_code == 401:
            print("Auth issue")

        elif resp.status_code == 200:
            resp = resp.json()
            print(f'{len(resp["centers"])}')

        else:
            print(f'Response code: {resp.status_code}')

except Exception as e:
    print(str(e))
