from os.path import abspath, dirname, join
import unittest
from mdtoc.mdtoc import generate_toc


class TestMdtoc(unittest.TestCase):
    ref_path = join(dirname(abspath(__file__)), "ref")
    out_path = join(dirname(abspath(__file__)), "out")
    in_path = join(dirname(abspath(__file__)), "in")

    # Methods placeholder. They are generated automatically at init  (see __init__.py)
    # PLACEHOLDER_BEGIN
    def test_toc_placeholdermd(self):
        with open(join(self.in_path, 'toc_placeholder.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'toc_placeholder.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'toc_placeholder.md')) as f:
            self.assertEqual(f.read(), out)

    def test_no_toc_yetmd(self):
        with open(join(self.in_path, 'no_toc_yet.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'no_toc_yet.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'no_toc_yet.md')) as f:
            self.assertEqual(f.read(), out)

    def test_no_headingsmd(self):
        with open(join(self.in_path, 'no_headings.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'no_headings.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'no_headings.md')) as f:
            self.assertEqual(f.read(), out)

    def test_same_namemd(self):
        with open(join(self.in_path, 'same_name.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'same_name.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'same_name.md')) as f:
            self.assertEqual(f.read(), out)

    def test_emptymd(self):
        with open(join(self.in_path, 'empty.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'empty.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'empty.md')) as f:
            self.assertEqual(f.read(), out)

    def test_emojismd(self):
        with open(join(self.in_path, 'emojis.md')) as f:
            out = generate_toc(f.read())
            with open(join(self.out_path, 'emojis.md'), 'w') as f_out:
                f_out.write(out)
        with open(join(self.ref_path, 'emojis.md')) as f:
            self.assertEqual(f.read(), out)
# PLACEHOLDER_END


if __name__ == '__main__':
    unittest.main()