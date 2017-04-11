from setuptools import setup


setup(
    name="lantern",
    version="1.0",
    install_requires=[
    ],
    entry_points="""
        [console_scripts]
        lantern=lantern.main:main
    """
)
