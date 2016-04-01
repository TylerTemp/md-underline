# md-underline

underline plugin for python markdown

## Summary

This will render `__content__` as underline format `<u>content</u>`

## Usage

```python
import markdown
from underline import UnderlineExtension
markdown.markdown('__underline__', extensions=[UnderlineExtension()]
# <u>underline</u>
```

## Install

```bash
pip install get+git://github.com/TylerTemp/md-underline.git
```

## API

`UnderlineExtension` accepts:

1.  `tag`: html tag name. use `u` by default

2.  `cls`: add class to the underline element. Default: `''`

e.g.

```python
import markdown
from underline import UnderlineExtension
markdown.markdown(
    '__underline__',
    extensions=[UnderlineExtension(tag='strong', cls='under')]
# <strong class='under'>underline</strong>
```

Note: it's strongly suggest using css to change the style instead of using `<u>` tag
because markdown is not designed for the style.

## Example

`__under__` -> `<u>under</u>`
`__*em*under__` -> `<u><em>em</em>under</u>`
`__*underem*__` -> `<u><em>underem</em></u>`

## Note

This plugin only work on:

1.  underline alone, or combine with em. Won't work on ***__combine-3__***
2.  When conbine with em, em can only use *, thus ___underline-with-em___
    won't work
