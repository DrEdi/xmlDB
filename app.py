from BaseXClient import BaseXClient

prepared_data = """
<all_books>
    <book id = "00001">
        <author>Elton R. Walker</author>
        <title>Vehicula Foundation</title>
        <year>1970</year>
        <price>100</price>
        <publisher>Sapien Cras Dolor Ltd</publisher>
        <annotation>lacus. Ut</annotation>
        <pages>284</pages>
        <sale>17</sale>
        <city>Ogbomosho</city>
        <cover>solid</cover>
        <genre>Comedy</genre>
    </book>
    <book id = "00002">
        <author>Gwendolyn O. Tyler</author>
        <title>Dolor Elit Consulting</title>
        <year>1973</year>
        <price>106</price>
        <publisher>Sapien Cras Dolor Ltd</publisher>
        <annotation>nec, imperdiet nec, leo. Morbi</annotation>
        <pages>448</pages>
        <sale>5</sale>
        <city>Luneburg</city>
        <cover>soft</cover>
        <genre>Drama</genre>
    </book>
    <book id = "00003">
        <author>Philip B. Porter</author>
        <title>Lobortis Nisi Nibh Consulting</title>
        <year>1972</year>
        <price>170</price>
        <publisher>Maecenas Iaculis Aliquet Consulting</publisher>
        <annotation>enim nisl elementum purus, accumsan</annotation>
        <pages>389</pages>
        <sale>12</sale>
        <city>Ogbomosho</city>
        <cover>soft</cover>
        <genre>Comedy</genre>
    </book>
    <book id = "00004">
        <author>Luke C. Bradley</author>
        <title>Lacinia Vitae Sodales Company</title>
        <year>1980</year>
        <price>120</price>
        <publisher>Viverra Maecenas Corp.</publisher>
        <annotation>Donec egestas. Aliquam nec enim.</annotation>
        <pages>314</pages>
        <sale>17</sale>
        <city>Ogbomosho</city>
        <cover>soft</cover>
        <genre>Drama</genre>
    </book>
    <book id = "00005">
        <author>Dalton X. Barton</author>
        <title>Velit Sed LLC</title>
        <year>1872</year>
        <price>200</price>
        <publisher>Mollis Vitae LLP</publisher>
        <annotation>pede,</annotation>
        <pages>407</pages>
        <sale>16</sale>
        <city>Lugo</city>
        <cover>solid</cover>
        <genre>Comedy</genre>
    </book>
    <book id = "00006">
        <author>Dalton X. Barton</author>
        <title>Vitae Inc.</title>
        <year>1954</year>
        <price>300</price>
        <publisher>Viverra Maecenas Corp.</publisher>
        <annotation>sed pede. Cum sociis</annotation>
        <pages>471</pages>
        <sale>20</sale>
        <city>Lugo</city>
        <cover>solid</cover>
        <genre>Sci-FI</genre>
    </book>
    <book id = "00007">
        <author>Trevor T. Pate</author>
        <title>Proin Eget Odio Associates</title>
        <year>1869</year>
        <price>250</price>
        <publisher>Pellentesque Habitant PC</publisher>
        <annotation>Aenean sed pede nec</annotation>
        <pages>471</pages>
        <sale>12</sale>
        <city>San Francisco</city>
        <cover>solid</cover>
        <genre>Comedy</genre>
    </book>
    <book id = "00008">
        <author>Rebekah C. Mcfarland</author>
        <title>Egestas Urna Institute</title>
        <year>1991</year>
        <price>40</price>
        <publisher>Pellentesque Habitant PC</publisher>
        <annotation>Vestibulum ante ipsum primis in</annotation>
        <pages>317</pages>
        <sale>5</sale>
        <city>Lugo</city>
        <cover>soft</cover>
        <genre>Sci-FI</genre>
    </book>
    <book id = "00009">
        <author>Trevor T. Pate</author>
        <title>Libero Morbi Accumsan LLP</title>
        <year>1874</year>
        <price>190</price>
        <publisher>Odio Aliquam PC</publisher>
        <annotation>euismod urna.</annotation>
        <pages>299</pages>
        <sale>17</sale>
        <city>Santo Domingo</city>
        <cover>soft</cover>
        <genre>Comedy</genre>
    </book>
    <book id = "00010">
        <author>Trevor T. Pate</author>
        <title>In Molestie Tortor Consulting</title>
        <year>1910</year>
        <price>220</price>
        <publisher>Pellentesque Habitant PC</publisher>
        <annotation>Nunc sed orci</annotation>
        <pages>192</pages>
        <sale>10</sale>
        <city>San Francisco</city>
        <cover>solid</cover>
        <genre>Drama</genre>
    </book>
    <book id = "00011">
        <author>Trevor T. Pate</author>
        <title>Pulvinar Arcu Consulting</title>
        <year>1856</year>
        <price>280</price>
        <publisher>Amet Diam Eu Company</publisher>
        <annotation>ornare, facilisis eget, ipsum. Donec</annotation>
        <pages>459</pages>
        <sale>13</sale>
        <city>San Francisco</city>
        <cover>solid</cover>
        <genre>Sci-FI</genre>
    </book>
    <book id = "00012">
        <author>Lois A. Salas</author>
        <title>Nunc LLP</title>
        <year>2000</year>
        <price>80</price>
        <publisher>Amet PC</publisher>
        <annotation>Fusce mi lorem, vehicula</annotation>
        <pages>158</pages>
        <sale>14</sale>
        <city>Orleans</city>
        <cover>soft</cover>
        <genre>Action</genre>
    </book>
    <book id = "00013">
        <author>Lois A. Salas</author>
        <title>Pretium Et Rutrum Corporation</title>
        <year>1925</year>
        <price>175</price>
        <publisher>Amet Diam Eu Company</publisher>
        <annotation>Fusce mollis. Duis sit</annotation>
        <pages>429</pages>
        <sale>20</sale>
        <city>Neunkirchen</city>
        <cover>soft</cover>
        <genre>Action</genre>
    </book>
    <book id = "00014">
        <author>Jillian E. Webb</author>
        <title>Nisl Quisque Fringilla Corporation</title>
        <year>1852</year>
        <price>310</price>
        <publisher>Amet Diam Eu Company</publisher>
        <annotation>ac mattis velit justo nec</annotation>
        <pages>342</pages>
        <sale>8</sale>
        <city>Siddi</city>
        <cover>solid</cover>
        <genre>Action</genre>
    </book>
    <book id = "00015">
        <author>Lois A. Salas</author>
        <title>Aptent Taciti Corporation</title>
        <year>1909</year>
        <price>210</price>
        <publisher>Integer Vitae Nibh Incorporated</publisher>
        <annotation>eu</annotation>
        <pages>108</pages>
        <sale>12</sale>
        <city>Metairie</city>
        <cover>solid</cover>
        <genre>Poem</genre>
    </book>
</all_books>
"""


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


if __name__ == '__main__':
    conn = BaseXConnector()
    conn.create_new_db('test', prepared_data)
    print(conn.get_books_count_by_type())
