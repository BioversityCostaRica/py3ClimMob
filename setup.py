import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "ago",
    "alembic",
    "amqp",
    "appdirs",
    "arrow",
    "attrs",
    "Babel",
    "backports.csv",
    "backports.functools-lru-cache",
    "beautifulsoup4",
    "billiard",
    "binaryornot",
    "black",
    "cairocffi",
    "CairoSVG",
    "celery",
    "certifi",
    "cffi",
    "Chameleon",
    "chardet",
    "cheroot",
    "CherryPy",
    "click",
    "cookiecutter",
    "cryptography",
    "cssselect2",
    "decorator",
    "defusedxml",
    "docxtpl",
    "fanstatic",
    "feedparser",
    "FormEncode",
    "future",
    "gevent",
    "greenlet",
    "gunicorn",
    "html5lib",
    "hupper",
    "idna",
    "imgkit",
    "importlib-metadata",
    "importlib-resources",
    "inflect",
    "ipaddress",
    "jaraco.classes",
    "jaraco.collections",
    "jaraco.functools",
    "jaraco.text",
    "Jinja2",
    "jinja2-time",
    "joblib",
    "kombu",
    "linecache2",
    "lingua",
    "lxml",
    "Mako",
    "MarkupSafe",
    "more-itertools",
    "mysql-connector-python",
    "mysqlclient",
    "nltk",
    "nose",
    "numpy",
    "PasteDeploy",
    "pathspec",
    "Pattern",
    "pdfminer.six",
    "Pillow",
    "plaster",
    "plaster-pastedeploy",
    "polib",
    "portend",
    "poyo",
    "protobuf",
    "pycparser",
    "pycrypto",
    "pycryptodome",
    "Pygments",
    "Pyphen",
    "pypng",
    "pyramid",
    "pyramid-debugtoolbar",
    "pyramid-fanstatic",
    "pyramid-jinja2",
    "pyramid-mako",
    "pyramid-tm",
    "pyTelegramBotAPI",
    "python-dateutil",
    "python-docx",
    "python-editor",
    "python-slugify",
    "pytz",
    "PyUtilib",
    "pyxform",
    "qrcode",
    "qrtools",
    "redis",
    "regex",
    "repoze.lru",
    "requests",
    "rutter",
    "scipy",
    "shutilwhich",
    "six",
    "sortedcontainers",
    "soupsieve",
    "SQLAlchemy",
    "SQLAlchemy-Utils",
    "tempora",
    "text-unidecode",
    "timeago",
    "tinycss2",
    "toml",
    "tqdm",
    "traceback2",
    "transaction",
    "translationstring",
    "typed-ast",
    "unicodecsv",
    "unittest2",
    "urllib3",
    "validators",
    "venusian",
    "vine",
    "waitress",
    "WeasyPrint",
    "webencodings",
    "WebHelpers2",
    "WebOb",
    "whichcraft",
    "xlrd",
    "XlsxWriter",
    "zc.lockfile",
    "zipp",
    "zope.deprecation",
    "zope.event",
    "zope.interface",
    "zope.sqlalchemy",
]


tests_require = [
    "WebTest >= 1.3.1",  # py3 compat
    "pytest",
    "pytest-cov",
]

setup(
    name="climmob",
    version="3.5.0",
    description="Climmob",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Bioverity Internatioanl",
    author_email="c.f.quiros@cgiar.org",
    url="http://climmob.net",
    keywords="web pyramid pylons",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require,},
    install_requires=requires,
    entry_points={
        "paste.app_factory": ["main = climmob:main",],
        "console_scripts": [
            "configure_mysql = climmob.scripts.configuremysql:main",
            "configure_alembic = climmob.scripts.configurealembic:main",
            "disable_ssl = climmob.scripts.disablessl:main",
            "set_super_password = climmob.scripts.setsuperpassword:main",
            "update_map_points = climmob.scripts.updatemappoints:main",
            "mysqldumps_climmob_dbs = climmob.scripts.mysqldumpclimmobdbs:main",
            "configure_tests = climmob.scripts.configuretests:main",
        ],
    },
)
