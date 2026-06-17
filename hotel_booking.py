from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Chromeのドライバを設定
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # URLにアクセス
    driver.get('https://www.booking.com/hotel/jp/intercontinental-yokohama-grand.ja.html')

    # 特定の要素が表示されるまで最大10秒待つ
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'hprt-roomtype-icon-link'))  # クラス名を指定
    )

    # ページのHTMLを取得
    html = driver.page_source

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(html, 'html.parser')

    # data-block-idが'35218445_94446806_2_34_0'の要素を検索
    block_element = soup.find(attrs={'data-block-id': '35218445_94446806_2_34_0'})

    # 検索結果の表示
    if block_element:
        # <span class="hprt-roomtype-icon-link">を検索
        span_element = block_element.find('span', class_='hprt-roomtype-icon-link')

        # <span>要素の表示
        if span_element:
            print(f'Found <span> element: {span_element}')
            print(f'Element content: {span_element.decode_contents()}')  # 中身のHTML
            print(f'Element text: {span_element.get_text(strip=True)}')  # テキスト
        else:
            print('<span class="hprt-roomtype-icon-link"> not found in the specified block.')
    else:
        print('Element with specified data-block-id not found.')

finally:
    # ブラウザを閉じる
    driver.quit()
