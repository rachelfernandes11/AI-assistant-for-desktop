# https://www.google.com/search?q=waether+patna
'''user agrent Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'''
#  span id = id="wob_tm"
#div vk_bk wob-unit
# haZE4 wob_dc

from requests_html import HTMLSession
import speech_to_text
import weather

def weather():
    s = HTMLSession()
    query =  "patan"
    url = f'https://www.google.com/search?q=weather+patna+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = r.html.find('span#wob_dc', first=True).text
    return temp+" "+unit+" "+desc
