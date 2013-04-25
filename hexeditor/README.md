HexEditor
=====

Hex Editor based on wxPython. It's a standalone application and a wxPython Panel can be embedded in other applications.

Usage:


    from hexeditor import HexEditor

    my_editor = HexEditor(parent)   # any wxPanel args

    my_editor.Binary = "\x00" * 128   # set binary content

    content = my_editor.Binary    # get binary content

    my_editor.LoadFile(filename)   # load binary content from file

    my_editor.SaveFile(filename)   # save binary content to file
