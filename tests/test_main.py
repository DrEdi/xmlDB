from app import BaseXConnector

conn = BaseXConnector()

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

conn.create_new_db('test_db', prepared_data)


def test_get_all_data():
    assert conn.get_book_list() == ['<title>Vehicula Foundation</title>',
                                    '<title>Dolor Elit Consulting</title>',
                                    '<title>Lobortis Nisi Nibh Consulting</title>',
                                    '<title>Lacinia Vitae Sodales Company</title>',
                                    '<title>Velit Sed LLC</title>',
                                    '<title>Vitae Inc.</title>',
                                    '<title>Proin Eget Odio Associates</title>',
                                    '<title>Egestas Urna Institute</title>',
                                    '<title>Libero Morbi Accumsan LLP</title>',
                                    '<title>In Molestie Tortor Consulting</title>',
                                    '<title>Pulvinar Arcu Consulting</title>',
                                    '<title>Nunc LLP</title>',
                                    '<title>Pretium Et Rutrum Corporation</title>',
                                    '<title>Nisl Quisque Fringilla Corporation</title>',
                                    '<title>Aptent Taciti Corporation</title>']


def test_get_authors():
    assert conn.get_author_list() == ['Dalton X. Barton', 'Elton R. Walker',
                                      'Gwendolyn O. Tyler', 'Jillian E. Webb',
                                      'Lois A. Salas', 'Luke C. Bradley',
                                      'Philip B. Porter',
                                      'Rebekah C. Mcfarland', 'Trevor T. Pate']


def test_get_genres():
    assert conn.get_genres_list() == ['Action', 'Comedy', 'Drama', 'Poem',
                                      'Sci-FI']


def test_get_cities():
    assert conn.get_city_and_publisher() == ['Lugo', 'Luneburg', 'Metairie',
                                             'Neunkirchen', 'Ogbomosho',
                                             'Orleans', 'San Francisco',
                                             'Santo Domingo', 'Siddi']


def test_get_books_by_autor():
    assert conn.get_books_by_autor('Trevor T. Pate') == \
           ['<title>Proin Eget Odio Associates</title>',
            '<title>Libero Morbi Accumsan LLP</title>',
            '<title>In Molestie Tortor Consulting</title>',
            '<title>Pulvinar Arcu Consulting</title>']


def test_get_books_by_publisher():
    assert conn.get_books_by_publisher('Pellentesque Habitant PC') == \
           ['<title>Proin Eget Odio Associates</title>',
            '<title>Egestas Urna Institute</title>',
            '<title>In Molestie Tortor Consulting</title>']


def test_get_books_by_genre():
    assert conn.get_books_by_genre('Sci-FI') == ['<title>Vitae Inc.</title>',
                                                 '<title>Egestas Urna Institute</title>',
                                                 '<title>Pulvinar Arcu Consulting</title>']


def test_get_books_by_years():
    assert conn.get_books_by_year(1920, 1970) == \
           ['<title>Pretium Et Rutrum Corporation</title>',
            '<title>Vitae Inc.</title>']


def test_get_books_by_price():
    assert conn.get_books_by_price(100, 170) == \
           ['<title>Dolor Elit Consulting</title>',
            '<title>Lacinia Vitae Sodales Company</title>']


def test_get_count_by_autor():
    assert conn.get_books_count_by_author('Trevor T. Pate') == ['4']


def test_get_count_by_cover():
    assert conn.get_books_count_by_type() == ['8']
