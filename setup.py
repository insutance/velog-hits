from setuptools import setup, find_packages


setup(
    name="velog-hits",
    version="1.0.0",
    description="Velog Hits",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="insutance",
    author_email="insutance@naver.com",
    url="https://github.com/insutance/velog-hits",
    python_requires=">= 3.8",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pandas",
        "requests"
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "velog-hits = velog_hits.main:main"
        ]
    },
    include_package_data = True,
    package_data={"velog-hits": ["html/*.css", "html/*.js"]}
)
