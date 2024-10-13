# 1. Contributing

## 1.1. Setup Development Environment

### 1.1.1. Toolchain

- Install python 3.11 or newer

### 1.1.2. VSCode Extensions

- Pylance: `ms-python.vscode-pylance`
- Tailwind CSS Intellisense: `bradlc.vscode-tailwindcss`
- Jinja: `wholroyd.jinja`
- Jinja2 Snippet Kit: `wyattferguson.jinja2-snippet-kit`
- BetterJinja: `samuelcolvin.jinjahtml`
- Markdown All in One: `yzhang.markdown-all-in-one`
- markdownlint: `davidanson.vscode-markdownlint`

### 1.1.3. Python Library Dependencies

~~~sh
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
~~~

## 1.2. Build Package

1. Run the following commands

    ~~~sh
    .\venv\Scripts\activate
    python setup.py bdist_wheel
    ~~~

1. Verify the package

    1. Examine the build output files at `build/lib/jinja_flowbite`
       1. Ensure that all the expected `.jinja` files are there

## 1.3. Publishing to PyPi

1. Install twine

    ~~~sh
    .\venv\Scripts\activate
    pip install twine # if you haven't already
    ~~~

1. Ensure you have your ~/.pypirc populated

    ~~~sh
    [pypi]
    username = __token__
    password = pypi-**********
    ~~~

1. Publish to PyPI

    1. Update the version number in `setup.py`
    1. Run the following command

        ~~~sh
        .\venv\Scripts\activate
        .\publish.ps1
        ~~~
