from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2


def init(request):
    try:
        # connect to exist database
        with psycopg2.connect(
                database=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST']
        ) as connection:
            # create a new table
            # the cursor for performing database operation
            with connection.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE ex02_movies ("
                    "episode_nb int, "
                    "title varchar(64) NOT NULL, "
                    "opening_crawl text, "
                    "director varchar(32) NOT NULL, "
                    "producer varchar(128) NOT NULL, "
                    "release_date date NOT NULL, "
                    "UNIQUE (title), "
                    "PRIMARY KEY (episode_nb)"
                    ");"
                )
            return HttpResponse('OK')
    except Exception as ex:
        return HttpResponse(ex)


def populate(request):
    response = ''
    movies = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    try:
        with psycopg2.connect(
                database=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST']
        ) as connection:
            with connection.cursor() as cursor:
                for movie in movies:
                    try:
                        cursor.execute(
                            "INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) VALUES "
                            "("
                            f"{movie['episode_nb']}, "
                            f"'{movie['title']}', "
                            f"'{movie['director']}', "
                            f"'{movie['producer']}', "
                            f"'{movie['release_date']}'"
                            ");"
                        )
                        response += "OK<br>"
                    except Exception as ex:
                        response += f'{ex}<br>'
            return HttpResponse(response)
    except Exception as ex:
        return HttpResponse(ex)


def display(request):
    try:
        with psycopg2.connect(
                database=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST']
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ex02_movies;")
                context = {
                    'movies': cursor.fetchall(),
                }
                if not context['movies']:
                    return HttpResponse('No data available')
        return render(request, 'ex02/display.html', context=context)
    except Exception:
        return HttpResponse('No data available')
