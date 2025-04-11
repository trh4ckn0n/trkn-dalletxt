from setuptools import setup, find_packages

setup(
    name='trkn_dalletxt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "requests",
        "Pillow",
        "questionary",
    ],
    entry_points={
        'console_scripts': [
            'trkn-menu=menu:main',  # si `main()` est ton point d’entrée
        ],
    },
)
