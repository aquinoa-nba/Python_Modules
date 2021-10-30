#!/usr/bin/env python3

from sys import argv
from requests import get
from dewiki import from_string

if __name__ == '__main__':
    if len(argv) == 2:
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'parse',
                "format": "json",
                'page': argv[1],
                'prop': 'wikitext',
                'redirects': ''
            }
            response = get(url, params)
            if response.status_code != 200:
                print('Error:', url, response.reason)
                exit(1)
            data = response.json()
            if 'error' in data.keys():
                print('Error: {}\nPage: \'{}\'.\nLink: {}.'.format(data['error']['info'], argv[1], response.url))
                exit(1)
            text = from_string(data['parse']['wikitext']['*'])
            f_in = open('{}.wiki'.format(argv[1].strip().replace(' ', '_')), 'w')
            f_in.write(text.strip())
            f_in.close()
        except Exception as exc:
            print(exc)
    else:
        print('Error: Wrong numbers of arguments.')
