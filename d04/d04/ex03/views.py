from django.shortcuts import render


def table_maker(request):
    context = {
        'title': 'Ex03: Table',
        'shades': range(250, 0, -5),
    }
    return render(request, 'ex03/table.html', context=context)
