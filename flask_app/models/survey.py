from  flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Survey:
    
    db_name = "dojo_survey"

    def __init__(self, data) :
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO survey (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s); "
        print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)


    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name needs to be 3 or more characters")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Location needs to be 3 or more characters")
            is_valid = False
        if len(survey['language']) < 3:
            flash("Language needs to be 3 or more characters")
            is_valid = False
        if len(survey['comment']) > 255:
            flash("Comment is greater than 255 charcters")
            is_valid = False
        return is_valid
        
        

