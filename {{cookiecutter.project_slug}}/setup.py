from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    packages=find_packages(),
    install_requires=[
        # Lista de dependências
    ],
)
