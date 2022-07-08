from yaml import BlockEndToken
from page import Page


class Bookstore:
    def __init__(self, page_number):
        self.url = 'http://books.toscrape.com'
        self.requested_page = Page(self.url).get_html()
        # page_number represents how many page will scrap.
        self.page_number = page_number

    def pagenumber(self, page_number=1):
        extended_url = f'/catalogue/page-{page_number}.html'
        self.requested_page = Page(self.url + extended_url).get_html()
        print(f'Collecting data from page {page_number}')

    def get_books(self):
        books = list()

        # returns a list
        for page in range(1, self.page_number+1):
            self.pagenumber(page)
            rows = self.requested_page.find('ol', class_='row')
            books.extend(rows.findAll('li'))
        return books

    def get_titles(self, max_price, min_price):
        books = self.get_books()
        book_list = []
        for book in books:
            price = book.find('div', class_='product_price').p.text.strip('Â£')
            # print(price)
            price = float(price)
            if price > min_price and price < max_price:
                title = book.h3.a['title']
                book_list.append(title)

        return book_list

    def critical_reader(self):
        books = self.get_books()
        book_list = []
        for book in books:
            star = book.article.p['class'][1]
            if star == 'One' or star == 'Two':
                continue
            else:
                title = book.h3.a['title']
                book_list.append(title)
        return book_list

    def avg_price(self):
        books = self.get_books()
        sumprice = 0
        book_counter = 0
        for book in books:
            price = book.find('div', class_='product_price').p.text.strip('Â£')
            price = float(price)
            sumprice += price
            book_counter += 1
        print('book of total : ', book_counter,
              'price of total books : ', sumprice)
        return sumprice / book_counter


def main():

    page_number = int(input('How many page you want to scrap  ? : '))
    bookstore = Bookstore(page_number)
    while True:
        choose = input((
            '1- Get titles with prices(max and min)\n2-Get above the 3 star\n3-Get avg prices\n4-Exit\n>>'))
        if choose == '1':
            max_price = int(input('max price : '))
            min_price = int(input('min price : '))
            print(bookstore.get_titles(max_price, min_price))
        elif choose == '2':
            print(bookstore.critical_reader())
        elif choose == '3':
            print(bookstore.avg_price())
        elif choose == '4':
            break


main()
