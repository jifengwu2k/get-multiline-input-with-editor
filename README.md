# **get-multiline-input-with-editor**

Opens a text editor for multi-line input, returns input as a Unicode string. Just like what Git does.

- Works with Python 2.7 and Python 3.x
- Determines editor either manually or via the Git-flavored heuristics in [`get-args-to-launch-editor`](https://github.com/jifengwu2k/get-args-to-launch-editor)
- Supports optional initial content and instructional prompt
- Opens a temporary file in the editor for multi-line user input
- Ignores comment lines and blank lines in the result

## Installation

```bash
pip install get-multiline-input-with-editor
```

## Usage

```python
from get_multiline_input_with_editor import get_multiline_input_with_editor

result = get_multiline_input_with_editor(
    unicode_initial_input=u"Write something...",
    unicode_prompt_at_bottom=u"# Enter your text above. Lines starting with # will be ignored.",
    unicode_line_comments_start_with=u"#",
    editor=None  # or specify e.g. 'vim'
)

print(result)
```

Assuming `nano` is the default editor, the user will see something like this:


```
GNU nano 7.2    /tmp/tmp9khfi5es.txt                                                                                                 
Write something...
# Enter your text above. Lines starting with # will be ignored.













^G Help         ^O Write Out    ^W Where Is     ^K Cut          ^T Execute      ^C Location     M-U Undo        M-A Set Mark
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^_ Go To Line   M-E Redo        M-6 Copy
```

Afterward, if the user enters some text, `print(result)` basically prints whatever the user entered, minus the comments.

## Contributing

Contributions welcome! Please open issues or pull requests on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).