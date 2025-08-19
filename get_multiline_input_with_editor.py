import codecs
import os
import tempfile
from subprocess import Popen

from get_args_to_launch_editor import get_args_to_launch_editor


def get_multiline_input_with_editor(
        unicode_initial_input=u'',
        unicode_prompt_at_bottom=u'# Enter your text above. Lines starting with # will be ignored.',
        unicode_line_comments_start_with=u'#',
        editor=None
):
    """
    Opens a text editor for multi-line input, returns input as a Unicode string.

    This function creates a temporary file pre-filled with initial input and a prompt,
    then opens it in the specified or default text editor. When the editor is closed,
    the file's content is read, blank lines and lines starting with the comment marker
    are ignored, and the remaining lines are returned, joined as a single Unicode string.

    Args:
        unicode_initial_input (unicode): Initial content to pre-populate the editor.
        unicode_prompt_at_bottom (unicode): Instructional prompt to append as the last line.
        unicode_line_comments_start_with (unicode): Lines starting with this string are considered comments and ignored.
        editor (str or None): Name/path of the editor to use, or None to use the default.

    Returns:
        unicode: User input, excluding lines that are blank or comments.

    Raises:
        EnvironmentError: if no editor could be found.
        OSError: If the editor fails to open or another OS error occurs.
    """
    args_to_launch_editor = get_args_to_launch_editor(editor)

    # Create temporary file context and close the temporary file
    with tempfile.NamedTemporaryFile(suffix='.txt', mode='wb+', delete=False) as tf:
        filename = tf.name
        first_line = unicode_initial_input.strip().encode('utf-8')
        second_line = unicode_prompt_at_bottom.strip().encode('utf-8')
        if first_line:
            tf.write(first_line)
            tf.write(b'\n')
        tf.write(second_line)
        tf.flush()

    try:
        args_to_launch_editor.append(filename)

        # Launch the editor and wait for it to close
        process = Popen(args_to_launch_editor)
        process.wait()

        # Read the content after editing
        non_comment_lines = []
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.rstrip()
                # skip completely blank lines and comments
                if not stripped_line:
                    continue
                if not stripped_line.lstrip().startswith(unicode_line_comments_start_with):
                    non_comment_lines.append(stripped_line)

        return u'\n'.join(non_comment_lines)
    finally:
        os.unlink(filename)
