"""
Usage
------

```python
import markdown
from underline import UnderlineExtension
markdown.markdown('__underline__', extensions=[UnderlineExtension()]
```

API
----

UnderlineExtension accepts:

tag: html tag name. use `u` by default

cls: add class to the underline element

e.g.

```python
import markdown
from underline import UnderlineExtension
markdown.markdown(
    '__underline__',
    extensions=[UnderlineExtension(tag='span', cls='under')]
# <span class='under'>underline</span>
```

Example
-------

__under__ -> <u>under</u>
__*em*under__ -> <u><em>em</em>under</u>
__*underem*__ -> <u><em>underem</em></u>

Note
----

This plugin only work on:

1.  underline alone, or combine with em. Won't work on ***__combine-3__***
2.  When conbine with em, em can only use *, thus ___underline-with-em___
    won't work

Author
------

TylerTemp <tylertempdev@gmail.com>
"""

from markdown.inlinepatterns import SimpleTagPattern, Pattern
from markdown.util import etree
from markdown import Extension
# import logging
#
# logger = logging.getLogger('MARKDOWN.underline')
__author__ = 'TylerTemp'
__version__ = '0.0.1'

# __underline__
UNDERLINE_RE = r'(__)(.+?)\2'

# *__underline-em__* or
# *__underline__em* or
# *em__underline__* or
# *em__underline__em*
EM_UNDERLINE_RE = r'\*(.*?)__(.+?)__(.*?)\*'

# __*em-ul*__ or
# __ul*em*__ or
# __*em*ul__ or
# __ul*em*ul__
UNDERLINE_EM_RE = r'__(.*?)\*(.+?)\*(.*?)__'


class SingleTagWithClassPattern(SimpleTagPattern):

    def __init__(self, pattern, tag, cls=None):
        super(SingleTagWithClassPattern, self).__init__(pattern, tag)
        self.cls = cls

    def handleMatch(self, m):
        elem = super(SingleTagWithClassPattern, self).handleMatch(m)
        if self.cls:
            old_class = elem.get('class', '')
            if old_class:
                new_class = '%s %s' % (old_class, self.cls)
            else:
                new_class = self.cls
            # logger.debug('set class as %s', new_class)
            elem.set('class', new_class)
        return elem


class EmUnderlinePattern(Pattern):

    def __init__(self, pattern, tag, cls, outside):
        super(EmUnderlinePattern, self).__init__(pattern)
        self.cls = cls
        self.tag = tag
        # underline tag is outside, e.g. __sth*em*sth__
        self.outside = outside

    def handleMatch(self, m):
        if self.outside:
            out_tag = etree.Element('em')
            in_tag = etree.SubElement(out_tag, self.tag)
            if self.cls:
                in_tag.set('class', self.cls)
        else:
            out_tag = etree.Element(self.tag)
            in_tag = etree.SubElement(out_tag, 'em')
            if self.cls:
                out_tag.set('class', self.cls)

        _, pre, mid, sub, _ = m.groups()
        if pre:
            out_tag.text = pre
        if sub:
            in_tag.tail = sub
        if mid:
            in_tag.text = mid

        return out_tag


class UnderlineExtension(Extension):

    def __init__(self, *args, **kwargs):
        # Define config options and defaults
        self.config = {
            'tag': ['u', 'underline tag'],
            'cls': ['', 'add class to the underline tag']
        }
        # Call the parent class's __init__ method to configure options
        super(UnderlineExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        # Create the del pattern
        underline = SingleTagWithClassPattern(
            UNDERLINE_RE, self.getConfig('tag'), self.getConfig('cls'))
        em_underline = EmUnderlinePattern(
            EM_UNDERLINE_RE,
            self.getConfig('tag'),
            self.getConfig('cls'), outside=False)
        underline_em = EmUnderlinePattern(
            UNDERLINE_EM_RE,
            self.getConfig('tag'),
            self.getConfig('cls'), outside=True)
        # Insert del pattern into markdown parser
        md.inlinePatterns.add('em_underline', em_underline, '>not_strong')
        md.inlinePatterns.add('underline_em', underline_em, '>not_strong')
        md.inlinePatterns.add('underline', underline, '>not_strong')


def makeExtension(*args, **kwargs):
    return UnderlineExtension(*args, **kwargs)


if __name__ == '__main__':
    import markdown
    # logging.basicConfig(level=logging.DEBUG)
    # logger.setLevel(logging.DEBUG)

    sources = [
        '*__em-under__*',
        '*em__under__*',
        '*__under__em*',
        '*em__under__em*',
        '__*em-ul*__',
        '__ul*em*__',
        '__*em*ul__',
        '__ul*em*ul__',
    ]

    for source in sources:
        print(source)
        print(markdown.markdown(source, extensions=[UnderlineExtension()]))
        print(markdown.markdown(source, extensions=[
            UnderlineExtension(tag='b', cls='underline')]))
