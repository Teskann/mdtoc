import re
from os import mkdir, listdir
from os.path import dirname, abspath, join

# Create out folder
try:
    mkdir(join(dirname(abspath(__file__)), "out"))
except FileExistsError:
    pass

# Create a test method for each file
with open(join(dirname(abspath(__file__)), "test_generation.py")) as f:
    content = f.read()
with open(join(dirname(abspath(__file__)), "test_generation.py"), "w") as f:
    methods = ""
    for file in listdir(join(dirname(abspath(__file__)), "in")):
        file_identifier = re.sub(r"\W+", "", file)
        method = f"""\n    def test_{file_identifier}(self):
        with open(join(self.in_path, '{file}'), encoding='utf-8') as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, '{file}'), 'w', encoding='utf-8') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, '{file}'), encoding='utf-8') as f:
            self.assertEqual(f.read(), out)\n"""
        methods += method
    f.write(re.sub(r"(?<=# PLACEHOLDER_BEGIN).*(?=# PLACEHOLDER_END)", methods, content, flags=re.DOTALL))
