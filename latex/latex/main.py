import py_latex
if __name__ == '__main__':
    obj = py_latex.py_latex()
    if obj.parameters['run_mod'] == 0:
        obj.get_resume()