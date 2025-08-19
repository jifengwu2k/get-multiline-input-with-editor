# `get-unicode-multiline-input-with-editor`

Opens `$EDITOR` to get multi-line input as a list of Unicode strings, just like what `git commit` does.

- Determines `$EDITOR` either manually or via the Git-flavored heuristics in [`get-unicode-arguments-to-launch-editor`](https://github.com/jifengwu2k/get-unicode-arguments-to-launch-editor)
- Supports optional initial content and comment lines
- Opens a temporary file in the editor to get multi-line input
- Ignores comment lines and blank lines in the result
- Works with Python 2+

## Installation

```bash
pip install get-unicode-multiline-input-with-editor
```

## Usage

```python
# coding=utf-8
from __future__ import print_function
from get_unicode_multiline_input_with_editor import get_unicode_multiline_input_with_editor

result = get_unicode_multiline_input_with_editor(
    unicode_initial_input_lines=[
        u'Write something here...',
        u'# Enter your text above.',
        u'# Lines starting with # will be ignored.'
    ],
    unicode_line_comments_start_with=u'#',
    editor=None  # or specify e.g. 'vim'
)

print(result)
```

Assuming `nano` is the default editor, the user will see something like this:


```
GNU nano 7.2    /tmp/tmp9khfi5es.txt                                                                                                 
Write something here...
# Enter your text above.
# Lines starting with # will be ignored.












^G Help         ^O Write Out    ^W Where Is     ^K Cut          ^T Execute      ^C Location     M-U Undo        M-A Set Mark
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^_ Go To Line   M-E Redo        M-6 Copy
```

Afterward, if the user enters some text, `print(result)` basically prints whatever the user entered, minus the comments.

## Contributing

Contributions welcome! Please open issues or pull requests on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).