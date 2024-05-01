import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyHaveIBeenPwned",
    version="0.1.9",
    author="Shane Scott",
    author_email="sscott@gotham-security.com",
    description="Library to query HaveIBeenPwned.com with handeling for CloudFlare anti-bot ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoVanguard/pyHaveIBeenPwned",
    packages=['pyHaveIBeenPwned'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.9',
)
