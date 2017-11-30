from app import BaseXConnector
from test_data import DATA


conn = BaseXConnector()

conn.create_new_db('test', DATA)


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
