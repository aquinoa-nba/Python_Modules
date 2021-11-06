from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


def populate(request):
    response = ''
    movies = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'opening_crawl': '',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'opening_crawl': '',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'opening_crawl': '',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'opening_crawl': '',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'opening_crawl': '',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'opening_crawl': '',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'opening_crawl': '',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    for movie in movies:
        try:
            i = Movies(
                episode_nb=movie['episode_nb'],
                title=movie['title'],
                opening_crawl=movie['opening_crawl'],
                director=movie['director'],
                producer=movie['producer'],
                release_date=movie['release_date']
            )
            i.save()
            response += 'OK<br>'
        except Exception as ex:
            response += f"{ex}<br>"
    return HttpResponse(response)


def display(request):
    try:
        context = {
            'movies': Movies.objects.all()
        }
        if not context['movies']:
            return HttpResponse("No data available")
        return render(request, 'ex03/display.html', context=context)
    except Exception:
        return HttpResponse("No data available")
