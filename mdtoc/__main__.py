import argparse
import glob
from os.path import isdir, isfile
from mdtoc import generate_toc


def main():
    parser = argparse.ArgumentParser(
        description="Create tables of contents for your markdown files !")
    parser.add_argument("input",
                        help="Input file/directory. If you give a "
                             "directory (with -r or not), mdtoc is applied on "
                             "all *.md files. If the input does not contain "
                             "a mdtoc table of content, it is created at the"
                             " beginning of the file. If you wish to put "
                             "the ToC elsewhere, add a placeholder in your "
                             "file (`[](mdtoc) ... [](/mdtoc)`). If this "
                             "placeholder is already in the file, all the "
                             "content between `[](mdtoc)` and `[](/mdtoc)`"
                             " is replaced by the TOC.")
    parser.add_argument("-m", "--min-depth",
                        help="Minimum heading level. If this is set to `None`,"
                             " there is no minimum depth applied. For "
                             "example, if you set -m to "
                             "`2`, all the headings with level < 2 will be "
                             "ignored (such as `# Dummy  Heading`). Default is"
                             " None.",
                        default="None")
    parser.add_argument("-M", "--max-depth",
                        help="Maximum heading level. If this is set to `None`,"
                             " there is no maximum depth applied. For "
                             "example, if you set -M to  `3`, all the headings"
                             " with level > 3 will be ignored (such as"
                             " `#### Dummy  Heading`). Default is None.",
                        default="None")
    parser.add_argument("-t", "--toc-title",
                        help="Title of the table of content part. Defaults to "
                             "`Table of Contents`.",
                        default="Table of Contents")
    parser.add_argument("-l", "--toc-level",
                        help="Heading level of the Table of content section. "
                             "Defaults to 1.",
                        default="1")
    parser.add_argument("-p", "--print", action="store_true",
                        help="Do not overwrite the markdown file but print "
                             "it with the table of content.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="List processed files verbosely.")
    parser.add_argument("-r", "--recursive", action="store_true")

    args = parser.parse_args()

    try:
        min_depth = int(args.min_depth)
    except ValueError:
        min_depth = None
    try:
        max_depth = int(args.max_depth)
    except ValueError:
        max_depth = None
    toc_level = int(args.toc_level)
    toc_title = args.toc_title

    if isdir(args.input):
        if args.recursive:
            files = glob.glob(args.input + '/**/*.[Mm][Dd]', recursive=True)
        else:
            files = glob.glob(args.input + '/*.[Mm][Dd]')
    elif isfile(args.input):
        files = [args.input]
    else:
        raise FileNotFoundError(f"No such file or directory `{args.input}`.")
    for file in files:
        if args.verbose:
            print(f"Generating TOC for file `{file}` ...")
        with open(file) as f:
            content = generate_toc(f.read(),
                                   toc_title=toc_title,
                                   toc_level=toc_level,
                                   min_depth=min_depth,
                                   max_depth=max_depth)
        if args.print:
            print(file + ":\n===\n\n" + content + "\n\n")
        else:
            with open(file, 'w') as f:
                f.write(content)


if __name__ == "__main__":
    main()
