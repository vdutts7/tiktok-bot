import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists and, if it doesn't exist, download it automatically
chromedriver_autoinstaller.install()

def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_terminal()
system('title PROGRAM_NAME')

print(pyfiglet.figlet_format("PROGRAM_NAME", font="slant"))
print("1. Option 1.\n2. Option 2.\n3. Option 3.\n3. Option 4.\n4. Credits.\n")

mode = int(input("Mode: "))

if mode == 1 or mode == 2 or mode == 3 or mode == 4:
    url = input("URL: ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    metric1 = 0
    metric2 = 0
    metric3 = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def update_title1(): # Update the title IF option 1 was picked.
    global metric1
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title PROGRAM_NAME ^| Metric 1: {beautify(metric1)} ^| Elapsed Time: {time_elapsed}')

def update_title2(): # Update the title IF option 2 was picked.
    global metric2
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title PROGRAM_NAME ^| Metric 2: {beautify(metric2
