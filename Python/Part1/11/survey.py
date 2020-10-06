class AnonymousSurvey():
    """
    Сбор анонимных ответов на опросы.
    """
    def __init__(self, question):
        """
        Сохраняет вопрос и готовится к сохранению ответов.
        """
        self.question = question
        self.responses = []
    
    def show_question(self):
        """
        Выводит вопросов.
        """
        print(self.question)
    
    def store_response(self, new_response):
        """
        Сохраняет один ответ на вопрос.
        """
        self.responses.append(new_response)

    def show_result(self):
        """
        Выводит полученные ответы.
        """
        print("Survey results:")
        for self.response in self.responses:
            print ('– ' + self.response)
        