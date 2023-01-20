# blame-rufus
pronto.ai assessment


Things to do before hand:

This project is made with Python and utilizes GitPython, so you would need do install it by typing in the command line:

    pip install GitPython


if other methods are needed, you can use:

    python setup.py install


download from: http://pypi.python.org/pypi/GitPython


or clone using this method:

    git clone https://github.com/gitpython-developers/GitPython
    git submodule update --init --recursive
    ./init-tests-after-clone.sh

----------------------
If you want to change what directory is checked, change the "git_dir" variable on line 30 to the desired local git repository path (using the same format shown in the example)

Then, you can run the program in either vscode or whatever program can run the Python programming language.

I did some testing to ensure that I could acccess local git repositoty information.
