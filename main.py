import sys
import datetime
from PyQt5 import QtWidgets
import gui.design as design
import requests
from bs4 import BeautifulSoup


class GUI(QtWidgets.QMainWindow, design.Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.parse)
        self.current_time = str(datetime.datetime.now())
        self.__HEADERS ={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0', 'accept': '*/*'}
        self.__URL = 'https://finance.ua/ru/currency'
        self.html = self.get_html(self.__URL)

    def parse(self):
        self.label.setText(self.current_time)
        if self.html.status_code == 200:
            vaults = self.content()
            result = []
            for item in vaults:
                result.append(item['name'])
                result.append(item['buy'])
                result.append(item['sell'])
            self.label_3.setText("Vault: " + result[0].center(9, ' ') + result[3].center(9, ' ') +
                                 result[6].center(9, ' ') + '\n' +
                                 'Buy: ' + result[1] + ' ' + result[4] + ' ' + result[7] + '\n' +
                                 'Sell: ' + result[2] + ' ' + result[5] + ' ' + result[8])
        else:
            self.label_3.setText("Error with connecting")
        return None

    def get_html(self, url, params=None):
        r = requests.get(url=url, headers=self.__HEADERS, params=params)
        return r

    def content(self):
        soup = BeautifulSoup(self.html.text, 'html.parser')
        vaults = []
        vaults_row = soup.find_all('tr', class_='major')
        for vault in vaults_row:
            vaults.append({
                'name': vault.find('td', class_='c1').get_text(),
                'buy': vault.find('td', class_='c2').get_text(),
                'sell': vault.find('td', class_='c3').get_text(),
            })
        return vaults


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
