import requests
from bs4 import BeautifulSoup

resp = requests.get('http://127.0.0.1:5050')  # ✅ Specify correct port
soup = BeautifulSoup(resp.text, 'html.parser')
assert soup.find('form'), 'Form not found!'
print('✅ UI test passed!')
