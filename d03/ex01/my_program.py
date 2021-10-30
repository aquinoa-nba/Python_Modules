#!/usr/bin/env python3

from local_lib.path import Path


def make_dir(dir):
    print('Creating directory \'{}\''.format(dir.name))
    dir.mkdir()


def create_file(file):
    print('Creating file \'{}/{}\''.format(file.dirname(), file.name))
    file.touch()


def write_in_file(file, content):
    print('Writing \'{}\' in \'{}/{}\''.format(content, file.dirname(), file.name))
    file.write_text(content)


def read_from_file(file):
    print('Reading from file \'{}/{}\''.format(file.dirname(), file.name))
    print('Content from \'{}/{}\': {}'.format(file.dirname(), file.name,file.read_text()))


def create_file_in_dir(dir, filename):
    file = Path('{}/{}'.format(dir.name, filename))
    if dir.exists():
        print('Directory \'{}\' already exists'.format(dir.name))
        if file.exists():
            print('File \'{}/{}\' already exists'.format(file.dirname(), file.name))
        else:
            create_file(file)
    else:
        make_dir(dir)
        create_file(file)
    return file


if __name__ == '__main__':
    try:
        file = create_file_in_dir(Path('dir'), 'file')
        write_in_file(file, 'Text')
        read_from_file(file)
    except Exception as exc:
        print(exc)
