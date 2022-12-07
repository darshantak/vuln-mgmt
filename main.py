import beautifulsoup4 as bs4
import requests, luigi
class Class1(luigi.Task):
    def output(self):
        return luigi.LocalTarget("")