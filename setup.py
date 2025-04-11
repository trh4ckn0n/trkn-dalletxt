from setuptools import setup, find_packages

setup(
    name='trkn-dalletxt',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'openai',
        'python-dotenv',
        'requests',
        'Pillow',
        'questionary',
    ],
    entry_points={
        'console_scripts': [
            'trkn-menu=trkn_dalletxt.menu:main',  # main() doit exister dans menu.py
        ],
    },
    author='trhacknon',
    description='Générateur d’images DALL·E avec prompt texte et customisation',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/trh4ckn0n/trkn-dalletxt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
