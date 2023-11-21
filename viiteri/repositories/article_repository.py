from db import get_database_connection


class ArticleRepository:
    def __init__(self, connection):
        self._connection = connection
    
    # lisää tietokantaan "article"-lähdeviitteen, parametrina article entity?
    def add_article_reference(self, article):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into articles (content) values (?);',
            (article) # vai article.content ?
        )
        self._connection.commit()
    
    def find_all_articles(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from articles;'
        )
        self._connection.commit()


article_repository = ArticleRepository(get_database_connection())