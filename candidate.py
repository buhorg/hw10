class Candidate:


    def __init__(self, arguments):
        self.my_id = arguments[0]
        self.name = arguments[1]
        self.picture = arguments[2]
        self.position = arguments[3]
        self.gender = arguments[4]
        self.age = arguments[5]
        self.skills = arguments[6]


    def __repr__(self):
        return self.name+' '+str(self.my_id)


    def is_candidate_by_id(self, my_id):
        """
        Проверка на совпадение id экземпляра класса с введенным id
        """
        if self.my_id == my_id:
            return True
        return False


    def is_candidate_by_skill(self, skill):
        """
        Проверка на включение в skill экземпляра класса введенного skill
        """
        if self.skills.lower().count(skill.lower()):
            return True
        return False


    def print_candidate(self):
        """
        Распечатка в виде строки экземпляра класса
        """
        my_str = f"<img src = {self.picture}>"
        my_str += f"<pre>{self.name}\n{self.position}\n{self.skills}</pre>"
        return my_str
