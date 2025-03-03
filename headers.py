import os

cp = {'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTExODAxMTEzLCJvcmdJZCI6MTI4MDg5LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwNzAwNDU4MTgiLCJuYW1lIjoiUmFudSBLdW1hciIsImVtYWlsIjpudWxsLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6dHJ1ZSwib3JnQ29kZSI6Imh3c2drIiwiaXNEaXlTdWJhZG1pbiI6MCwiZmluZ2VycHJpbnRJZCI6ImI2NWRjY2RmODY0YTQwZTJmNDJmNDhhODY5ZjNjNTcxIiwiaWF0IjoxNzA3OTA2MDMwLCJleHAiOjE3MDg1MTA4MzB9.Fy7dc_cq0nK05K4cW6SVR1KD_39VD-XQExW19ouB4Z6ktClDo9tpSQ6MvNxbd2r1',
    'user-agent': 'Mobile-Android'
    }

vimeo = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-A226B Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "X-Requested-With": "com.edmingle.engageapp",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://edmingle-api.edmingle.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "vuid=pl262334675.728414577; player=\"\"; _cfuvid=cKOLn_s2GT3LCgQWr58w9XkfCbQ4kDZQl61VNaOFsYM-1710988985103-0.0.1.1-604800000; __cf_bm=s3IiTLeVwKLJVSl1Z2N58IhJlW8EvB7Bh4tij4ZPs8o-1710990259-1.0.1.1-D_Jac4UNoepH.Km4jLDbJ5AE7xeQFdIFZxlPQ28ywgEfmXB4nC_cRoSi0_qkSX8VTQIITWTvGNcIk6hmRJ547w"
}   

vision = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://www.visionias.in/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': "Android"}


pw = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5MTQ0NjUuMjA3LCJkYXRhIjp7Il9pZCI6IjY1ZWRlYTlkMTM4YzQ3MzQxZTg5MzJkMiIsInVzZXJuYW1lIjoiOTIzNTE2NDg1NiIsImZpcnN0TmFtZSI6Ik9wIiwibGFzdE5hbWUiOiJSYXoiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJtcmF6emppQGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTcxNzMwOTY2NX0.WObYDWVzSiV0mu_ODud83bVvb9hSjaz8Hp-seCnejhA",
    "client-type": "WEB",
    "randomId": "142d9660-50df-41c0-8fcb-060609777b03"
}

vc = {
        "Host": "license64.vdocipher.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Content-type": "application/octet-stream",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }

allen = {
    "Connection": "keep-alive",
    "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; G011A Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.171 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "com.allen.allenPlus",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://allenplus.allen.ac.in/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9"
}
