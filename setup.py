from setuptools import find_namespace_packages, setup

with open("README.md", "r") as rm:
    readme_md = rm.read()

with open("requirements.txt") as rq:
    requirements_txt = rq.read().splitlines()

setup(
    name="jinja_flowbite",
    version="0.2.dev0",
    platforms="any",
    description="Flowbite-Based Jinja Components",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    keywords="python flask jinja flowbite htmx",
    url="https://github.com/schaveyt/jinja-flowbite",
    author="Todd Schavey",
    author_email="schaveyt@gmail.com",
    license="MIT",
    python_requires=">=3.9",
    install_requires=requirements_txt,
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "jinja_flowbite.jinja_flowbite.controls": ["*.jinja"],
        "jinja_flowbite.jinja_flowbite.icons": ["*.jinja"],
    },
    classifiers=[],
    include_package_data=True,
)

