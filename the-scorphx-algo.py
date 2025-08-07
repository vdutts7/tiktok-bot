from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import system, name
from time import time, strftime, gmtime, sleep
import pyfiglet
import threading
import chromedriver_autoinstaller
import random
import csv

# ChromeDriver'ı otomatik yükle
chromedriver_autoinstaller.install()

def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def update_title(metric):
    global start
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title TikTokMultiLikeBot ^| Beğeni: {beautify(metric)} ^| Elapsed Time: {time_elapsed}')
        sleep(1)

def load_accounts(file_path):
    accounts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    accounts.append({'username': row[0], 'password': row[1]})
        return accounts
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return []
    except Exception as e:
        print(f"Hesaplar yüklenirken hata: {e}")
        return []

def load_proxies(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            proxies = [line.strip() for line in file if line.strip()]
        return proxies
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı, proxy'siz devam ediliyor.")
        return []
    except Exception as e:
        print(f"Proxy'ler yüklenirken hata: {e}")
        return []

def login_to_tiktok(driver, username, password):
    try:
        driver.get("https://www.tiktok.com/login")
        print(f"{username} ile giriş yapılıyor...")

        # E-posta/telefon ile giriş butonunu bul
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in with email or phone')]"))
        )
        login_button.click()

        # Kullanıcı adı ve şifre alanlarını doldur
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

        # Giriş yap butonuna tıkla
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()

        # Girişin başarılı olduğunu doğrulamak için birkaç saniye bekle
        WebDriverWait(driver, 20).until(
            EC.url_contains("tiktok.com")
        )
        print(f"{username} ile giriş başarılı!")
        return True
    except Exception as e:
        print(f"{username} ile giriş sırasında hata: {e}")
        return False

def like_video(driver, url, metric):
    try:
        driver.get(url)
        print(f"Video URL'si açılıyor: {url}")

        # Beğeni butonunu bul ve tıkla
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-e2e='like-icon']"))
        )
        like_button.click()
        metric += 1
        print(f"Beğeni yapıldı: {metric}")
        return metric
    except Exception as e:
        print(f"Beğeni yapılamadı: {e}")
        return metric

def main():
    global start
    clear_terminal()
    system('title TikTokMultiLikeBot')

    print(pyfiglet.figlet_format("TikTokMultiLikeBot", font="slant"))
    print("Birden fazla hesapla TikTok videosuna beğeni atmak için bilgilerinizi girin.")

    # Kullanıcıdan video URL'sini, hesap dosyasını ve proxy dosyasını al
    url = "https://www.tiktok.com/@yuskadi04/video/7535085734244470023"
    print(f"Video URL'si: {url}")
    accounts_file = input("Hesapların bulunduğu CSV dosyasının adı (örneğin, accounts.csv): ")
    proxies_file = input("Proxy'lerin bulunduğu TXT dosyasının adı (isteğe bağlı, boş bırakabilirsiniz): ")

    accounts = load_accounts(accounts_file)
    proxies = load_proxies(proxies_file) if proxies_file else []

    if not accounts:
        print("Hesap bulunamadı, program sonlandırılıyor.")
        return

    start = time()
    metric = 0

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'user-agent={random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ])}')

    try:
        threading.Thread(target=update_title, args=(metric,), daemon=True).start()
        print("Beğeni botu çalışıyor...")

        for i, account in enumerate(accounts):
            username = account['username']
            password = account['password']

            # Proxy ayarla (varsa)
            if proxies:
                proxy = random.choice(proxies)
                chrome_options.add_argument(f'--proxy-server={proxy}')
                print(f"Kullanılan proxy: {proxy}")

            driver = webdriver.Chrome(options=chrome_options)
            driver.set_window_size(1024, 650)

            try:
                # Her hesap için giriş yap
                if login_to_tiktok(driver, username, password):
                    # Videoya beğeni at
                    metric = like_video(driver, url, metric)
                    # TikTok'un bot tespitini önlemek için rastgele gecikme
                    sleep(random.uniform(5, 10))
                else:
                    print(f"{username} ile giriş başarısız, bir sonraki hesaba geçiliyor.")
            except Exception as e:
                print(f"{username} ile işlem sırasında hata: {e}")
            finally:
                driver.delete_all_cookies()
                driver.quit()

            # Her 100 beğeniden sonra durumu kaydet
            if (i + 1) % 100 == 0:
                print(f"Ara durum: {metric} beğeni atıldı.")

        print(f"Toplam beğeni: {metric}")
        input("Programı kapatmak için Enter'a basın...")

    except KeyboardInterrupt:
        print("Kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
        print("Tarayıcı kapatıldı.")

if __name__ == "__main__":
    main()
