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
                    "CREATE TABLE ex00_movies ("
                    "title varchar(64) NOT NULL, "
                    "episode_nb int, "
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
