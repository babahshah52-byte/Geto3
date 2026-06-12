import time
import random
import json
import os
import asyncio
import sys
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, SlowmodeWait, PeerIdInvalid
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import defaultdict, deque
import concurrent.futures

# =============== FIX FOR EVENT LOOP ================
if sys.version_info[0] == 3 and sys.version_info[1] >= 10:
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

#=============== CONFIG ================
API_ID = 39035274
API_HASH = "6a0b24e16c4bea2bbc975b7dbb0c1e64"
BOT_TOKEN = "
8924877076:AAHfXjBgw2bBLcvvvSx6SXYrr1pLZMEvtRo"
OWNER_ID = 8722144519
BOT_USERNAME = "ll_SUPRRME_XD_3_ll_BOT"

#=============== CUSTOM LINES ================
CUSTOM_LINES = [
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",

    # ========== DIRECT ABUSE LINES ==========
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    "bahenklodo tumhari maa meri setting",
    "bahenklodo tumhari maa meri setting",
    "teri mummy randi h randi bsdk",
    "teri mummy ki pussy m scooter dalduga",
    "teri mummy ki pussy me cum krduga randi maa k bache",
    "tera khandan hi randiyo ka h",
    "teri dadi ki pussy me mera lund",
    "teri mummy ko chodkr ulta ltkakr uske muh me loda deduga",
    "teri mummy ko deepthroat deduga madarchod k bache",
    "✌️✌️tera papa bhi randi ki aulad h bsdk",
    "teri mummy ko yoga sikhaduga aur usko different styles me choduga",
    "tera papa hu mai teri mummy ka bf jis s vo chudkr gyi thi",
    "teri maa ki pussy me scooter dalduga bahen k lode🤣🤣",
    "teri maa ki chut me bihari gutka khakr thuk kr chale gye the🔥🔥",
    "💀💀teri maa ka bosda randi k beej",
    "✌️✌️teri maa ki chut me 2finger dekr uska paani nikalduga0",
    "🔥🔥teri maa k muh me gass pipe dekr uski gaand me fire lgakr tere baap ki gaand jalauga",
    "😂😍😍teri randi maa ko chodkr maine gb road pr beach diya tha",
    "🙌🙌teri mummy k haath divar pr lgvadiye the 10bihariyo ne",
    "teri mummy ki chut madarchodo hizda hai hai tum madarchodo bol de yuta tera baap hai warna teri ki chut koi ramdi ki aulad nhi bacha payega aaj samjh le madrchod",
    "air jorden ke jute se teri ki chut pr maar maar ke laal kr dunga kali se laal 😋🥵 randi madarchodo",
    "madarchodo baap se ladega apne teri ma ki chut kha jaunga ramdi",
    "teri maa ki chhut ka khaa jaunga madarchodo randi ki aulad spam karta hai madarcod ke chakke ki aulad tere baap ko gadhe ke land see chodunga",
    "teri maki chut madarchod sur ke land se ma chodunga gandi chut ki kali aulad fati kali chut ki auld chamr teri maiya ki chut ko chor bazr me bechunga madrachod",
    "teri maiya ke ki chut me apne land ka python bot bana kr run krunga teri sasti spam user bot ka bhosda madarchodo",
    "teri maiya ka bhosda madarchodo sasti gb raod ki randi ki aulad",
    "fati kali chut ki auld chamr teri maiya ki chut ko chor bazr me bechunga madrachod",
    "teri makichut ko kutto ko khila dunga randi ki saststi aulad madarchodo",
    "teri mummy ki chut bsdk 🖕",
    
    # ========== PARAGRAPH EXTENDED ABUSE ==========
    "sun bhsdike, tu apni ma ki chut me pani bhar ke aa rha hai kya? teri maki chut ka anguthi ke barabar bhi koi value nahi hai, madarchod kahin ka. teri behen ki chut ka chakkar mein tera baap bhi kuch nahi kar payega. teri gaand me 4 golyan mar ke tumhe bhagwa chola pehna dunga. randi ki aulad, teri maiya ne to mujhe bolaya tha ke ${USER} ko rok ke rakh, lekin teri ma ki chut mein to puro poori jeej ka dungi!",
    "madarchod! teri maiya ne to mujhe bataya ki tu abhi tak bachon wali nikkar pehenta hai. teri behen to meri randi hai aur teri maa meri rakhal. tere baap ko malum hai to bhi kuch nahi kar sakta. teri maki chut me mera lund itna deep gaya ki teri dadi ki bhi yaad aa gayi. aag laga dunga teri family me, tere saare khandan ki gaand marunga. tu to bas ek khaali aluminium ka tube hai, jisme kuch nahi bachega!",
    "bahen ke lode! tujhe lagta hai tu bohot bada aaya hai? teri maiya to meri chodi hui malkin hai. teri behen ka muh mera lund se bhara hua tha jab tu tv dekh rha tha. teri maa ki chut me to 5 goliyan, 4 ungliyan aur 2 penetration ho chuki hain. tu kya bosdina kare ga? teri shakal pe thappar marunga to tu ro dega, madarchod.",
    "teri maiya ki chut me mera lund itna zor se ghoosta hai jaise stadium ke flood lights chal rahi ho. teri behen to itni suali hai ki uski chut me dandiyaan daalni padti hain. madarchod kahin ka, tu to bas ek chhotu sa bosdina hai. tera baap bhi meri presence me ghutno ke bal aata hai.",
    "randi ki aulad! teri maiya to meri aafat hai aur tu mera fan. teri maa ki chut me to bohot zyada traffic hai, ek to main aur ek tere baap ka dosra beta. tu kuch bhi nahi hai bosdina. main teri behen ki chut me ek dam paver blocker launch kar dunga aur teri maiya ko tere saamne sabke saamne chodunga.",
    "chutiya tu maa chudane aaya hai? teri maiya to meri randi list me highest rated hai. teri behen to itni raandi hai ki uski chut me paytm se payment karta hu main. tera baap to sirf camera dekhne ka kaam karta hai jab main teri maa chodta hu.",
    "teri maa ki chut me mera lund bsdk 🍆💦",
    "teri gaand phat gayi kya bhag kya rha hai 🏃💨",
    "teri maa ne mujhe bolya ko ghas mat khila 💀",
    "teri maa ki chut ka kera hai tu 🤡",
    
    # ========== BEHEN (SISTER) ABUSE LINES ==========
    "teri behen ko dekh ke mera lund khara ho gya 😏",
    "tu apni maa ka dudh peena band kar de 🍼",
    "teri behen ki chut me 5 bihari ek saath 🥵",
    "teri shakal dekh ke mera lund murjha gya 🥀",
    "teri behen to meri ex hai ab teri maa meri current hai 😎",
    "tera baap bhi randi ki aulad hai sale 🚮",
    "teri maa ki chut me parking lot 🅿️",
    "teri behen ki chut me wifi chalta hai 📶",
    "teri behen to meri favorite randi hai 💋",
    "teri maa ki chut me cloud storage ☁️",
    "teri behen ki chut me bluetooth connect 📱",
    "teri maa ki chut ka subscriber hu mai 🔔",
    "teri maa ko chod ke thak gya hu 💦",
    "teri behen ka onlyfans top donation mai hu 👑",
    "teri behen ko chodta hu to aawaz aati hai oye haye 🎵",
    "teri behen ki chut ka rent 500 hai 💵",
    "teri behen ko dekh ke mera lund bolta hai aaja 🗣️",
    "teri behen ka virginity maine li thi 🏆",
    "teri behen ke muh me mera lund 💯",
    "teri behen ko randi bana ke chodta hu 🎯",
    "teri behen to meri sugarmammy hai 🍭",
    "teri behen ke muh ka swad chang hai 👅",
    "teri behen ko randi banane ka master hu mai 🧠",
    "teri behen ki chut ka toll free number 📞",
    "teri behen ki chut ka pin 7860 📌",
    "teri behen ki chut ka rate list 💲",
    "teri behen ki chut ka catalog 📚",
    "teri behen ki chut ka location 📍",
    "teri behen ki chut ka color black 🖤",
    "teri behen ki chut ka stock available 📦",
    "teri behen ki chut ka offer zone 🏷️",
    "teri behen ki chut ki quality aaa ✅",
    "teri behen ki chut ka track record 🏅",
    "teri maa ki chut teri behen ka bhosda 🖕",
    "madarchod teri aukaat nahi hai bhaag yahan se 🤬",
    "bhadwe teri maa ki chut itna attitude kahan se laata hai 🖕",
    "itni shakal buri ki aaina bhi tod de 🔥",
    "teri photo dekh ke darwaza chod de itna ugly hai tu 🤣",
    "main aag hoon jo jalati hai aur raakh mein bhi chamakti hai 🔥",
    "meri aukaat nahi meri shaan hai 👑",
    "madarchod teri aukaat nahi hai bhaag yahan se 🤬",
    "teri shaadi kab hai? maa ne kaha ghar par rakh legi 😂",
    "tu itna smart hai ki duniya ko laga tera baap ka paisa hai 🤣",
    
    # ========== UNICODE FORMAL LINES (TERI MAA) ==========
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI BEHEN) ==========
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE BAAP) ==========
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI FAMILY) ==========
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE KUTTE) ==========
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI AUKAAT) ==========
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI MUMMY) ==========
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE DADA) ==========
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== PUNISHMENT LINES (UNAUTHORIZED USERS) ==========
    "TERI MAKI CHUT ${USER} RANDI ITACHI PAPA BOL KE THODI AUKAT BANA LE PHIR BOT SE CHUDWANA AAKE 😋🥵",
    "MADARCHOD ${USER} TERI AUKAAT NAHI HAI BOT USE KARNE KI TERI MAIYA KI CHUT ME MERA LUND 🍆💦",
    "${USER} RANDI KI AULAD BOT KA USE KARE GA TERI MAKI CHUT ME TALWAR GHUSAAUNGA 🔥",
    "BHOSDIKE ${USER} TERI BEHEN KI CHUT ME BOT DAAL DUNGA TERI AUKAAT PEHLE BANA 🖕",
    "${USER} CHUTIYE TU KAUN HOTA HAI BOT USE KARNE WALA TERI MAIYA NE BOL DIYA TERA BAAP BHI NAHI HAI 🤡",
    "TERI MAKI CHUT ${USER} MADARCHOD PEHLE SUDO LE PHIR AA NAHI TO TERI GAAND MARUNGA 💀",

]

# =============== WEB SERVER ================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = "<h1>ULTRA FAST MULTI-GROUP RAID BOT V3</h1><p>Status: ONLINE</p><p>Speed: 1000x (ULTRA OPTIMIZED)</p>"
        self.wfile.write(html.encode('utf-8'))
    def log_message(self, format, *args):
        pass

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

app = Client("ultra_fast_bot_v3", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

#=============== DATA ================
sudo_users = set()
raid_active = {}
raid_tasks = {}
raid_count = {}

# High-performance flood control - per group token bucket
class TokenBucket:
    def __init__(self, rate=35, burst=50):
        self.rate = rate
        self.burst = burst
        self.tokens = burst
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()
    
    def consume(self, tokens=1):
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(self.burst, self.tokens + elapsed * self.rate)
            self.last_refill = now
            if self.tokens >= tokens:
                self.tokens -= tokens
                return 0
            wait = (tokens - self.tokens) / self.rate
            self.tokens = 0
            return wait

group_buckets = defaultdict(lambda: TokenBucket(35, 50))

#=============== FILE PATHS ================
SUDO_FILE = "sudo_users.json"
LINES_FILE = "custom_lines.json"

#=============== DATA PERSISTENCE ================
def load_all_data():
    global sudo_users, CUSTOM_LINES
    print("\n📂 LOADING SAVED DATA...")
    
    if os.path.exists(SUDO_FILE):
        try:
            with open(SUDO_FILE, "r") as f:
                loaded_sudo = json.load(f)
                if loaded_sudo and isinstance(loaded_sudo, list):
                    sudo_users = set(loaded_sudo)
                    print(f"✅ Loaded {len(sudo_users)} sudo users")
        except Exception as e:
            print(f"⚠️ Error loading sudo users: {e}")
            sudo_users = {OWNER_ID}
    else:
        sudo_users = {OWNER_ID}
        save_sudo_users()
    
    if os.path.exists(LINES_FILE):
        try:
            with open(LINES_FILE, "r", encoding='utf-8') as f:
                loaded_lines = json.load(f)
                if loaded_lines and isinstance(loaded_lines, list):
                    CUSTOM_LINES = loaded_lines
                    print(f"✅ Loaded {len(CUSTOM_LINES)} custom lines")
        except Exception as e:
            print(f"⚠️ Error loading lines: {e}")
    
    print(f"👑 Owner ID: {OWNER_ID}")
    print("✅ DATA LOADING COMPLETE!\n")

def save_sudo_users():
    try:
        with open(SUDO_FILE, "w") as f:
            json.dump(list(sudo_users), f, indent=2)
    except Exception as e:
        print(f"❌ Error saving sudo users: {e}")

def save_custom_lines():
    try:
        with open(LINES_FILE, "w", encoding='utf-8') as f:
            json.dump(CUSTOM_LINES, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Error saving lines: {e}")

def save_all_data():
    save_sudo_users()
    save_custom_lines()

def is_sudo(user_id):
    return user_id == OWNER_ID or user_id in sudo_users

#=============== ULTRA-FAST SENDER ================
async def ultra_fast_send(chat_id, text, retries=3):
    """Super fast sender with automatic flood handling"""
    for attempt in range(retries):
        try:
            # Token bucket rate limiting
            wait = group_buckets[chat_id].consume()
            if wait > 0:
                await asyncio.sleep(wait)
            
            return await app.send_message(chat_id, text)
        except FloodWait as e:
            # Adaptive backoff
            sleep_time = e.value + random.uniform(0, 0.5)
            await asyncio.sleep(sleep_time)
            # Reduce rate for this group
            bucket = group_buckets[chat_id]
            bucket.rate = max(5, bucket.rate * 0.7)
            bucket.burst = max(10, bucket.burst * 0.7)
        except SlowmodeWait as e:
            await asyncio.sleep(e.value + 0.1)
        except Exception as e:
            err = str(e).lower()
            if "420" in err or "flood" in err:
                await asyncio.sleep(1)
            elif "blocked" in err or "deactivated" in err:
                return None
            else:
                await asyncio.sleep(0.05)
    return None

#=============== BURST SENDER ================
async def burst_send(chat_id, texts, batch_size=10):
    """Send multiple texts in parallel bursts"""
    results = []
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        
        # Send batch concurrently
        tasks = [ultra_fast_send(chat_id, text) for text in batch]
        batch_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for r in batch_results:
            if not isinstance(r, Exception) and r is not None:
                results.append(r)
        
        # Minimal delay between batches - 0 delay for maximum speed
        # Only delay if we have more batches to send
        if i + batch_size < len(texts):
            # Dynamic delay based on group bucket state
            bucket = group_buckets[chat_id]
            if bucket.rate < 15:
                await asyncio.sleep(0.05)
    
    return results

#=============== GET CLICKABLE MENTION ================
async def get_clickable_mention(client, user_input, message):
    if message.reply_to_message:
        target = message.reply_to_message.from_user
        return target.mention, target.id, target.first_name
    
    if user_input and user_input.startswith("@"):
        try:
            target = await client.get_users(user_input)
            return target.mention, target.id, target.first_name
        except:
            return user_input, None, None
    
    if user_input and user_input.isdigit():
        try:
            target = await client.get_users(int(user_input))
            return target.mention, target.id, target.first_name
        except:
            return f"`{user_input}`", None, None
    
    return None, None, None

#=============== ULTRA-FAST RAID LOOP ================
async def raid_loop(client, chat_id, target_user_id, target_mention, target_name, raid_id, count):
    global raid_active, raid_count
    
    raid_active[raid_id] = True
    sent = 0
    
    if not CUSTOM_LINES:
        await ultra_fast_send(chat_id, f"❌ No custom lines found! Use `!addline` to add lines first.")
        raid_active[raid_id] = False
        return
    
    # Build message queue for maximum throughput
    message_queue = []
    
    if count == -1:
        raid_type = "UNLIMITED"
        
        await ultra_fast_send(
            chat_id,
            f"╔══════════════════════════════════╗\n"
            f" ⚡ **ULTRA RAID STARTED** ⚡\n"
            f"╚══════════════════════════════════╝\n\n"
            f"🎯 **Target:** {target_mention}\n"
            f"📜 **Lines:** `{len(CUSTOM_LINES)}`\n"
            f"⚡ **Mode:** BURST (10 parallel)\n"
            f"♾️ **Type:** {raid_type}\n"
            f"🛑 **Stop:** `!stopr`"
        )
        
        # Unlimited mode - keep generating and sending in bursts
        try:
            while raid_active.get(raid_id, False):
                # Build a batch of messages
                batch_texts = []
                for _ in range(30): # 30 messages per batch cycle
                    for line in CUSTOM_LINES:
                        if not raid_active.get(raid_id, False):
                            break
                        if "${USER}" in line:
                            final = line.replace("${USER}", target_mention)
                        else:
                            final = f"{target_mention} {line}"
                        batch_texts.append(final)
                        sent += 1
                        if len(batch_texts) >= 30:
                            break
                    if not raid_active.get(raid_id, False) or len(batch_texts) >= 30:
                        break
                
                if batch_texts:
                    # Send batch in parallel (burst mode)
                    await burst_send(chat_id, batch_texts, batch_size=10)
                
                # Progress update every 500 messages
                if sent % 500 < 30 and sent > 0:
                    await ultra_fast_send(chat_id, f"📊 **PROGRESS**\n📨 Sent: `{sent}` 🎯 {target_mention}")
                
                await asyncio.sleep(0) # Yield control
                
        except Exception as e:
            print(f"Raid error: {e}")
    else:
        # Limited mode
        await ultra_fast_send(chat_id, f"⏳ **Raiding {target_name}**\n📨 Target: `{count}` messages\n⚡ Mode: BURST")
        
        try:
            messages_to_send = min(count, 10000)
            
            while sent < messages_to_send and raid_active.get(raid_id, False):
                remaining = messages_to_send - sent
                batch_size = min(25, remaining)
                
                batch_texts = []
                for _ in range(batch_size):
                    for line in CUSTOM_LINES:
                        if sent >= messages_to_send or not raid_active.get(raid_id, False):
                            break
                        if "${USER}" in line:
                            final = line.replace("${USER}", target_mention)
                        else:
                            final = f"{target_mention} {line}"
                        batch_texts.append(final)
                        sent += 1
                
                if batch_texts:
                    await burst_send(chat_id, batch_texts, batch_size=10)
                
                await asyncio.sleep(0)
            
            await ultra_fast_send(chat_id, f"✅ **RAID COMPLETE**\n📨 Sent: `{sent}/{messages_to_send}`\n🎯 {target_mention}")
            
        except Exception as e:
            print(f"Raid error: {e}")
    
    raid_active[raid_id] = False
    raid_count[raid_id] = sent

#=============== MULTI-GROUP RAID ================
@app.on_message(filters.command(["r", "tr"], prefixes="!") & filters.group)
async def multi_group_raid_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text(f"❌ Not authorized! Only sudo users can use raid.")
        return
    
    parts = message.text.split()
    cmd = parts[0].lower().replace("!", "")
    
    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass
        
        if not target_user and len(parts) > 1:
            try:
                target_user = await client.get_users(parts[1])
            except:
                pass
    
    if not target_user:
        await message.reply_text("❌ Reply to user or tag them!\nUsage: `!r @username` (unlimited)\n`!tr @username 100` (limited)")
        return
    
    if target_user.id == OWNER_ID or is_sudo(target_user.id):
        await message.reply_text("🛡️ Cannot raid owner/sudo user!")
        return
    
    count = -1
    if cmd == "tr":
        for part in parts:
            if part.isdigit():
                count = int(part)
                break
        
        if count == -1:
            await message.reply_text("❌ For limited raid, specify count!\nExample: `!tr @user 100`")
            return
        
        if count < 1 or count > 10000:
            await message.reply_text("❌ Count must be between 1-10000!")
            return
    
    chat_id = message.chat.id
    raid_id = f"{chat_id}_{target_user.id}"
    
    if raid_active.get(raid_id, False):
        await message.reply_text(f"❌ Already raiding {target_user.first_name} in this group!")
        return
    
    try:
        await message.delete()
    except:
        pass
    
    asyncio.create_task(raid_loop(client, chat_id, target_user.id, target_user.mention, target_user.first_name, raid_id, count))

#=============== RAID ALL GROUPS AT ONCE ================
@app.on_message(filters.command(["ra"], prefixes="!") & filters.private)
async def raid_all_groups_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can use this command!")
        return
    
    parts = message.text.split(maxsplit=2)
    if len(parts) < 2:
        await message.reply_text(
            "❌ **Usage:** `!ra @username` (unlimited in all groups)\n"
            "`!ra @username 100` (limited in all groups)"
        )
        return
    
    target_input = parts[1]
    target_user = None
    
    if target_input.startswith("@"):
        try:
            target_user = await client.get_users(target_input)
        except:
            await message.reply_text("❌ Invalid username!")
            return
    elif target_input.isdigit():
        try:
            target_user = await client.get_users(int(target_input))
        except:
            await message.reply_text("❌ Invalid user ID!")
            return
    else:
        await message.reply_text("❌ Please tag a user with @username!")
        return
    
    if target_user.id == OWNER_ID or is_sudo(target_user.id):
        await message.reply_text("🛡️ Cannot raid owner/sudo user!")
        return
    
    count = -1
    if len(parts) == 3 and parts[2].isdigit():
        count = int(parts[2])
        if count < 1 or count > 10000:
            await message.reply_text("❌ Count must be between 1-10000!")
            return
    
    # Get all groups fast
    groups = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            groups.append(dialog.chat.id)
    
    if not groups:
        await message.reply_text("❌ Bot is not in any groups!")
        return
    
    raid_type = "UNLIMITED" if count == -1 else f"LIMITED ({count} messages)"
    
    status_msg = await message.reply_text(
        f"⚡ **MULTI-GROUP RAID STARTED** ⚡\n\n"
        f"🎯 Target: {target_user.mention}\n"
        f"📦 Groups: `{len(groups)}`\n"
        f"♾️ Mode: {raid_type}\n"
        f"⚡ Mode: BURST (10 parallel)\n\n"
        f"⏳ Starting..."
    )
    
    # Launch all raids SIMULTANEOUSLY - no delay between them
    tasks = []
    started = 0
    
    for group_id in groups:
        raid_id = f"{group_id}_{target_user.id}"
        if not raid_active.get(raid_id, False):
            task = asyncio.create_task(
                raid_loop(client, group_id, target_user.id, target_user.mention, target_user.first_name, raid_id, count)
            )
            tasks.append(task)
            started += 1
    
    await status_msg.edit_text(
        f"✅ **MULTI-GROUP RAID ACTIVE**\n\n"
        f"🎯 Target: {target_user.mention}\n"
        f"✅ Groups: `{started}`\n"
        f"⚡ All running simultaneously!\n\n"
        f"🛑 Stop all: `!stopall`"
    )

#=============== STOP RAID ================
@app.on_message(filters.command("stopr", prefixes="!") & filters.group)
async def stop_raid_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    chat_id = message.chat.id
    stopped = 0
    
    for raid_id in list(raid_active.keys()):
        if raid_id.startswith(f"{chat_id}_") and raid_active.get(raid_id, False):
            raid_active[raid_id] = False
            stopped += 1
    
    if stopped == 0:
        await message.reply_text("❌ No active raid in this group!")
        return
    
    try:
        await message.delete()
    except:
        pass
    
    await message.reply_text(f"🛑 **Stopped {stopped} raid(s) in this group**")

#=============== STOP ALL RAIDS ================
@app.on_message(filters.command("stopall", prefixes="!") & filters.private)
async def stop_all_raids(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner!")
        return
    
    count = 0
    for raid_id in list(raid_active.keys()):
        if raid_active.get(raid_id, False):
            raid_active[raid_id] = False
            count += 1
    
    await message.reply_text(f"🛑 **Stopped {count} raid(s) globally**")

#=============== STATUS ================
@app.on_message(filters.command("raidstatus", prefixes="!") & filters.group)
async def raid_status_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    chat_id = message.chat.id
    active_raids = []
    
    for raid_id, active in raid_active.items():
        if raid_id.startswith(f"{chat_id}_") and active:
            target_id = raid_id.split("_")[1]
            sent = raid_count.get(raid_id, 0)
            try:
                user = await client.get_users(int(target_id))
                active_raids.append(f"• {user.mention} - {sent} msgs")
            except:
                active_raids.append(f"• `{target_id}` - {sent} msgs")
    
    if not active_raids:
        await message.reply_text("📊 **No active raids in this group**")
    else:
        status_text = f"📊 **ACTIVE RAIDS**\n\n" + "\n".join(active_raids)
        await message.reply_text(status_text)

#=============== GLOBAL STATUS ================
@app.on_message(filters.command("globalstatus", prefixes="!") & filters.private)
async def global_raid_status(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    
    active_raids = []
    for raid_id, active in raid_active.items():
        if active:
            parts = raid_id.split("_")
            chat_id = parts[0]
            target_id = parts[1]
            sent = raid_count.get(raid_id, 0)
            active_raids.append(f"• Group: `{chat_id}` | Target: `{target_id}` | Sent: {sent}")
    
    if not active_raids:
        await message.reply_text("📊 **No active raids globally**")
    else:
        text = f"📊 **GLOBAL ACTIVE RAIDS**\n\n" + "\n".join(active_raids[:50])
        await message.reply_text(text)

#=============== LINES MANAGEMENT ================
@app.on_message(filters.command("addline", prefixes="!") & filters.private)
async def add_line_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add lines!")
        return
    
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❌ Usage: `!addline <text>`\n💡 Use `${USER}` for target mention")
        return
    
    CUSTOM_LINES.append(parts[1])
    save_custom_lines()
    await message.reply_text(f"✅ Line added! Total: `{len(CUSTOM_LINES)}`")

@app.on_message(filters.command("lines", prefixes="!") & filters.private)
async def view_lines_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    if not CUSTOM_LINES:
        await message.reply_text("📝 No lines found! Use `!addline` to add.")
        return
    
    text = f"📝 **Lines ({len(CUSTOM_LINES)})**\n\n"
    for i, line in enumerate(CUSTOM_LINES[:30], 1):
        text += f"`{i}.` {line[:60]}\n"
    
    await message.reply_text(text)

#=============== SUDO MANAGEMENT ================
@app.on_message(filters.command("add", prefixes="!") & filters.group)
async def add_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner!")
        return

    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        parts = message.text.split()
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass

    if not target_user:
        await message.reply_text("❌ Reply to user or tag them!")
        return

    if target_user.id in sudo_users:
        await message.reply_text(f"❌ Already sudo!")
        return

    sudo_users.add(target_user.id)
    save_sudo_users()
    await message.reply_text(f"✅ {target_user.first_name} added as sudo!")
    await message.delete()

@app.on_message(filters.command("remove", prefixes="!") & filters.group)
async def remove_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner!")
        return

    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        parts = message.text.split()
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass

    if not target_user:
        await message.reply_text("❌ Reply to user or tag them!")
        return

    if target_user.id not in sudo_users:
        await message.reply_text(f"❌ Not a sudo user!")
        return

    sudo_users.remove(target_user.id)
    save_sudo_users()
    await message.reply_text(f"✅ {target_user.first_name} removed from sudo!")
    await message.delete()

@app.on_message(filters.command("sudolist", prefixes="!") & filters.group)
async def sudo_list_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return

    if not sudo_users:
        await message.reply_text("📝 No sudo users!")
        return

    text = "👑 **SUDO USERS**\n\n"
    for uid in sudo_users:
        try:
            user = await client.get_users(uid)
            text += f"• {user.mention}\n"
        except:
            text += f"• `{uid}`\n"
    
    text += f"\n👑 Owner: `{OWNER_ID}`"
    await message.reply_text(text)

#=============== ALIVE ================
@app.on_message(filters.command("alive", prefixes="!") & filters.group)
async def alive_command(client, message: Message):
    chat_id = message.chat.id
    active_count = 0
    for raid_id, active in raid_active.items():
        if raid_id.startswith(f"{chat_id}_") and active:
            active_count += 1
    
    await message.reply_text(
        f"🔥 **BOT ONLINE V3** 🔥\n\n"
        f"⚡ Mode: BURST (10 parallel)\n"
        f"📜 Lines: `{len(CUSTOM_LINES)}`\n"
        f"🔑 Sudo: `{len(sudo_users)}`\n"
        f"🎯 Active Raids: `{active_count}`\n"
        f"🌍 Multi-Group: ✅\n"
        f"👑 Owner: `{OWNER_ID}`"
    )

#=============== PING ================
@app.on_message(filters.command("ping", prefixes="!") & filters.group)
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("📡 Pinging...")
    end = time.time()
    await msg.edit_text(f"⚡ **PONG!** `{round((end-start)*1000)}ms`\n🚀 **BURST MODE ACTIVE**")

#=============== HELP ================
@app.on_message(filters.command("help", prefixes="!"))
async def help_command(client, message: Message):
    await message.reply_text(
        f"🤖 **ULTRA RAID BOT V3**\n\n"
        f"⚔️ **RAID (BURST MODE - 10 PARALLEL):**\n"
        f"• `!r @user` - Unlimited raid\n"
        f"• `!tr @user 100` - Limited raid\n"
        f"• `!ra @user` - RAID ALL GROUPS\n"
        f"• `!ra @user 100` - Limited all groups\n"
        f"• `!stopr` - Stop raid\n"
        f"• `!stopall` - Stop all raids\n"
        f"• `!raidstatus` - Check status\n"
        f"• `!globalstatus` - Global status\n\n"
        f"👑 **OWNER:**\n"
        f"• `!addline text` - Add line\n"
        f"• `!lines` - View lines\n\n"
        f"🔐 **SUDO:**\n"
        f"• `!add @user` / `!remove @user`\n"
        f"• `!sudolist`\n\n"
        f"⚡ **V3 OPTIMIZATIONS:**\n"
        f"• Token Bucket Rate Limiting\n"
        f"• Parallel Burst Sending (10x)\n"
        f"• Automatic Flood Adaptation\n"
        f"• Zero-Delay Batch Processing\n"
        f"• Concurrent Multi-Group Raids"
    )

#=============== CALLBACK ================
@app.on_callback_query()
async def button_callback(client, callback_query):
    data = callback_query.data
    if data == "help":
        await callback_query.message.edit_text(
            "⚔️ **COMMANDS**\n\n"
            "`!r @user` - Unlimited raid\n"
            "`!tr @user 100` - Limited raid\n"
            "`!ra @user` - All groups raid\n"
            "`!stopr` - Stop raid\n"
            "`!ra` = RAID ALL GROUPS!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )
    elif data == "back":
        await callback_query.message.edit_text(
            "🔥 **ULTRA RAID BOT V3** 🔥\n\nBURST Mode | 10 Parallel | Auto Flood Control",
            reply_markup=get_main_keyboard()
        )
    elif data == "home":
        await callback_query.message.edit_text(
            f"🏠 **STATS**\n\n"
            f"Sudo: `{len(sudo_users)}`\n"
            f"Lines: `{len(CUSTOM_LINES)}`\n"
            f"Mode: BURST (10 parallel)\n"
            f"Multi-Group: ✅\n"
            f"Owner: `{OWNER_ID}`",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )
    await callback_query.answer()

def get_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me Baby", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🏠 My Home", callback_data="home")],
        [InlineKeyboardButton("👑 My Master", url="https://t.me/ll_SUPRRME_XD_ll")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⚡ Get Sudo", url="https://t.me/ll_SUPRRME_XD_ll")]
    ])

#=============== SHUTDOWN ================
import atexit
atexit.register(save_all_data)

#=============== MAIN ================
if __name__ == "__main__":
    load_all_data()
    
    print("=" * 60)
    print("⚡ **ULTRA RAID BOT V3 - BURST MODE (1000x SPEED)** ⚡")
    print("=" * 60)
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"🔑 Sudo Users: {len(sudo_users)}")
    print(f"📝 Custom Lines: {len(CUSTOM_LINES)}")
    print(f"⚡ Mode: BURST (10 parallel sends)")
    print(f"🌍 Multi-Group: ✅ YES")
    print(f"🔄 Token Bucket Rate Limiting: ✅")
    print(f"📦 Batch Size: 25 messages")
    print("=" * 60)
    print("✅ Commands: !r | !tr | !ra | !stopr | !stopall")
    print("=" * 60)

    app.run()

