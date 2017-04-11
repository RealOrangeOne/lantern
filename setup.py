from setuptools import setup


setup(
    name="lantern",
    version="1.0",
    install_requires=[
        "sanic==0.4.1",
        "sanic-useragent==0.1.2"
    ],
    entry_points="""
        [console_scripts]
        lantern=lantern.main:main
    """
)
