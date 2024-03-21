'''Test class Mark.'''

from opentaal import Mark

# pylint:disable=missing-function-docstring


def test_html_link():
    assert Mark.html_link(text='home', url='https://ho.me') == \
        '<a href="https://ho.me">home</a>'
    assert Mark.html_link(text='home',
                          url='https://ho.me',
                          new=True) == \
        '<a target="_blank" href="https://ho.me">home</a>'
    assert Mark.html_link(text='home',
                          url='https://ho.me',
                          tooltip='HOME') == \
        '<a title="HOME" href="https://ho.me">home</a>'
    assert Mark.html_link(text='home',
                          url='https://ho.me',
                          tooltip='HOME',
                          new=True) == \
        '<a target="_blank" title="HOME" href="https://ho.me">home</a>'


def test_md_link():
    assert Mark.md_link(text='home',
                        url='https://ho.me') == \
        '[home](https://ho.me)'
    assert Mark.md_link(text='home',
                        url='https://ho.me',
                        new=True) == \
        '<a target="_blank" href="https://ho.me">home</a>'
    assert Mark.md_link(text='home',
                        url='https://ho.me',
                        tooltip='HOME') == \
        '<a title="HOME" href="https://ho.me">home</a>'
    assert Mark.md_link(text='home',
                        url='https://ho.me',
                        tooltip='HOME',
                        new=True) == \
        '<a target="_blank" title="HOME" href="https://ho.me">home</a>'


def test_html_head():
    assert Mark.html_head(title='Title') == \
        '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Title</title>
</head>
<body>
<h1>Title</h1>
'''
    assert Mark.html_head(title='Title',
                          lang='en',
                          mono=True) == \
        '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Title</title>
<style>
* {font-family: monospace, monospace;}
</style>
</head>
<body>
<h1>Title</h1>
'''
    assert Mark.html_head(title='Title',
                          style='textarea {line-height: 150%;}') == \
        '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Title</title>
<style>
textarea {line-height: 150%;}
</style>
</head>
<body>
<h1>Title</h1>
'''
    assert Mark.html_head(title='Title',
                          style='textarea {line-height: 150%;}',
                          mono=True) == \
        '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Title</title>
<style>
* {font-family: monospace, monospace;}
textarea {line-height: 150%;}
</style>
</head>
<body>
<h1>Title</h1>
'''


def test_md_head():
    assert Mark.md_head(title='Title') == \
        '''# Title

'''


def test_html_foot():
    assert Mark.html_foot() == '''</body>
</html>
'''
    assert Mark.html_foot(footer='Some words at the bottom') == \
        '''<p><small>Some words at the bottom</small></p>
</body>
</html>
'''


def test_md_foot():
    assert Mark.md_foot() == ''
    assert Mark.md_foot(footer='Some words at the bottom') == '''
<small>Some words at the bottom</small>
'''

# pylint:enable=missing-function-docstring
