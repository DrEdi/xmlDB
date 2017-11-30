from BaseXClient import BaseXClient


class BaseXConnector():

    def __init__(self, host='localhost', port=1984):
        self.session = BaseXClient.Session(host, port, 'admin', 'admin')

    def create_new_db(self, name, data=None):
        return self.session.create(name, data)

    def __query_data(self, query):
        data = self.session.query(query)
        return [item for _, item in data.iter()]

    def get_book_list(self):
        query = 'for $x in doc("test")/all_books/book return $x/title'
        return self.__query_data(query)

    def get_author_list(self):
        query = 'for $x in distinct-values(doc("test")/all_books/book/author)'\
                ' order by $x return $x'
        return self.__query_data(query)

    def get_genres_list(self):
        query = 'for $x in distinct-values(doc("test")/all_books/book/genre)' \
                ' order by $x return $x'
        return self.__query_data(query)

    def get_city_and_publisher(self):
        query = 'for $x in distinct-values(doc("test")/all_books/' \
                'book/city) order by $x return $x'
        return self.__query_data(query)

    def get_books_by_autor(self, autor):
        query = f"for $x in doc('test')/all_books/book where" \
                f" $x/author = '{autor}' return $x/title"
        return self.__query_data(query)

    def get_books_by_publisher(self, pub):
        query = f"for $x in doc('test')/all_books/book where" \
                f" $x/publisher = '{pub}' return $x/title"
        return self.__query_data(query)

    def get_books_by_genre(self, genre):
        query = f"for $x in doc('test')/all_books/book where" \
                f" $x/genre = '{genre}' return $x/title"
        return self.__query_data(query)

    def get_books_by_year(self, start, end):
        query = f"for $x in doc('test')/all_books/book where" \
                f" $x/year > {start} and $x/year < {end} order by" \
                f" $x/year return $x/title"
        return self.__query_data(query)

    def get_books_by_price(self, start, end):
        query = f"for $x in doc('test')/all_books/book where" \
                f" $x/price > {start} and $x/price < {end} order by" \
                f" $x/price return $x/title"
        return self.__query_data(query)

    def get_books_count_by_author(self, autor):
        query = f"let $items := 0 return count(for $x in " \
                f"doc('test')/all_books/book where $x/author=" \
                f"'{autor}' return $x/author)"
        return self.__query_data(query)

    def get_books_count_by_type(self):
        query = f"let $items := 0 return count(for $x in doc('test')" \
                f"/all_books/book where $x/cover=\"solid\" return $x/cover)"
        return self.__query_data(query)


