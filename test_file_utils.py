import word_file_utils.py as wf


def test_process_word_file():
    assert wf.process_word_file('sample.txt') == ("War and Peace", "line1\nline2\nline3")
    assert wf.process_word_file('sample.txt') == ("War and Peace", "line1\nline2")
    assert wf.process_word_file('sample.txt') == ("Title", "line1\nline2\nline3")
    assert wf.process_word_file('sample.txt') == None
    assert wf.process_word_file('sample.txt') == None
    

