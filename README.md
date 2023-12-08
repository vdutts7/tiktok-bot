<br />
<div align="center">

  <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/tiktok-logo" alt="Logo" width="75" height="75"/>
  <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/python-logo_" alt="Logo" width="80" height="80"/>

  
  <h2 align="center">TikTok Bot</h2> 
  <p align="center">Automate TikTok views, likes, & follows 👁️</p>

[![Github][github]][github-url]

 </div>

<br/>

## Table of Contents

  <ol>
    <a href="#about">📝 About</a><br/>
    <a href="#how-to-build">💻 How to Build</a><br/>
        <ul>
            <a href="#steps">Steps</a>
            <a href="#pros-and-cons">Pros and Cons</a>
        </ul>
    <a href="#tools-used">🔧 Tools Used</a>
        <ul>
        </ul>
    <a href="#contact">👤 Contact</a>
  </ol>

<br/>

## 📝About

Coded a TikTok automation bot to:

- View videos
- Send Likes
- Gain Followers

I created this for my business <b>[Scorphx](https://scorphx.shop)</b> to take advantage of TikTok's "viral content" algorithm during the most viral time for my business (2022 World Cup): generate rapid engagement, promote the concept kits I was selling, and direct mass traffic to link-in-bio i.e. my [online store](https://scorphx.shop).

<br/>

## 💻How to Build

- `Selenium` library- controls a web browser and navigate to TikTok, where it allows user to select from a number of different modes that perform different actions.
- Uses `pyfiglet` library to display banner message = visually appealing.
- `strftime` function- formats into user-friendly readable elapsed time.

### Steps

1. Clone repo:
   <pre>git clone https://github.com/vdutts7/scorphx-tiktok-automation-bot </pre>
   <pre>cd scorphx-tiktok-automation-bot</pre>
2. Install modules:
   <pre>pip install -r scorphx-algo-reqs.txt</pre>
3. Run the `.py` file:
   <pre>python the-scorphx-algo.py</pre>

### Pros and Cons

_\*from POV of a non-coder looking for absolute convenience_

<b>Pros</b>

- Banner message = visually appealing.
- Includes functions to clear/title text in terminal = easy to read program output and see current status.
- Checks if current ChromeDriver version exists. If it doesn't, downloads it automatically.
- Several try and except blocks to catch exception i.e. minimize program crashes.
- `strftime` function --> formats into user-friendly readable elapsed time.
  <br/>

<b>Cons</b>

- Code uses `Selenium` to control a web browser, which can be unreliable and prone to breaking when websites change.
  - If TikTok makes any important updates, code may break.
- Code uses `chromedriver_autoinstaller` library to check if the current version of ChromeDriver exists and, if it doesn't, download it automatically. Potential compatibility issues.
- Does not include error handling for invalid input i.e. if user enters a value that is not an integer when prompted to select a mode. This could result in the program crashing if the user enters invalid input.

<br/>
<br/>

## 🔧Tools Used

[![Selenium][selenium]][selenium-url]
[![python][python]][python-url]

<br/>

## 👤Contact

[![Email][email]][email-url]
[![Twitter][twitter]][twitter-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[selenium]: https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
[python]: https://img.shields.io/badge/Python_(pyfiglet)-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[github]: https://img.shields.io/badge/💻Github-000000?style=for-the-badge
[github-url]: https://github.com/vdutts7/tiktok-bot/
[email]: https://img.shields.io/badge/me@vd7.io-FFCA28?style=for-the-badge&logo=Gmail&logoColor=00bbff&color=black
[email-url]: #
[twitter]: https://img.shields.io/badge/Twitter-FFCA28?style=for-the-badge&logo=Twitter&logoColor=00bbff&color=black
[twitter-url]: https://twitter.com/vdutts7/
