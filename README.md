# scorphx-tiktok-automation-bot

![op](https://user-images.githubusercontent.com/63992417/210528515-c339c24b-f82a-4d84-bda7-12636ff2c2a6.png)


## How do I install and use this?
1. Git-clone this repo & change directory
   <pre>git clone https://github.com/vdutts7/scorphx-tiktok-automation-bot </pre>
   <pre>cd scorphx-tiktok-automation-bot</pre>
2. Install modules using pip:
   <pre>pip install -r scorphx-algo-reqs.txt</pre>
3. Make sure you have Google Chrome installed
4. Run the .py file!
   <pre>python the-scorphx-algo.py</pre>

## Pros (from POV of a non-coder looking for absolute convenience)
1. The code uses pyfiglet library to display banner message = visually appealing.
2. Includes functions to clear/title text in terminal = easy to read program output and see current status.
3. Checks if current ChromeDriver version exists. If it doesn't, downloads it automatically.
4. Several try and except blocks to catch exception i.e. minimize program crashes.
5. strftime function --> formats into user-friendly readable elapsed time.

## Cons (from POV of a non-coder looking for absolute convenience)
1. Code uses the Selenium library to control a web browser, which can be unreliable and prone to breaking when websites change. If TikTok makes any updates to their website, the code may no longer work as intended.
2. Depending on your perspective, the code may be seen as not aligned with the values in TikTok's "Community Guidelines". Real question is- who reads those in the first place? THose people probably wouldn't even make it this far in attention span or comprehension. It's alright, if you're here reading this youre in better shape to attack the ever-changing algorithm.
3. The code is using the chromedriver_autoinstaller library to check if the current version of ChromeDriver exists and, if it doesn't, download it automatically. This could potentially cause issues if the version of ChromeDriver that is being downloaded is incompatible with the version of Chrome being used.
4. The code does not include any error handling for invalid input, such as if the user enters a value that is not an integer when prompted to select a mode. This could result in the program crashing if the user enters invalid input.

## Note
The first recaptcha has to be completed manually. 

## Special thanks to
https://zefoy.com/ for providing this amazing free service!
