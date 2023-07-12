class Phonebook:

    def __init__(self):
        self.entries = {}

    def check_contact(self, name):
        """
        Check if name exists in list

        :param name: Name to be verified
        :return: True or False
        """

        if name in self.entries:
            return True
        else:
            return False

    def valid_characters(self, name):
        """
        Validates if there are disallowed characters in the name

        :param name: Name to be validated
        :return: True or False
        """

        strings = ['#', '@', '!', '$', '%']
        for string in strings:
            if string in name:
                return False
        return True

    def add(self, name, number):
        """
        Add a new contact

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if not self.valid_characters(name):
            return 'Nome invalido'

        if len(number) < 1:
            return 'Número invalido'

        if name not in self.entries:
            self.entries[name] = number
        else:
            return 'Contato existe'

        return 'Número adicionado'

    def lookup(self, name):
        """
        Retrieve a number by name

        :param name: name of person in string
        :return: number of person with name or 'Contato não encontrado'
        """

        if self.check_contact(name):
            return self.entries[name]

        return 'Contato não encontrado'

    def get_names(self):
        """
        Get all name in phonebook

        :return: All names in phonebook
        """

        return self.entries.keys()

    def get_numbers(self):
        """
        Get all numbers in phonebook

        :return: All numbers in phonebook
        """

        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook

        :return: 'phonebook limpo'
        """

        self.entries = {}
        return 'phonebook limpo'

    def search(self, search_name):
        """
        Search all substring with search_name

        :param search_name: string with name for search
        :return: List with results of search or 'Contato não encontrado'
        """

        result = []
        if self.check_contact(search_name):
            for name, number in self.entries.items():
                if search_name in name:
                    result.append({name: number})
            return result
        else:
            return 'Contato não encontrado'

    def get_phonebook_sorted(self):
        """
        Get phonebook in sorter order

        :return: Phonebook in sorted order
        """

        sorted_dict = dict(sorted(self.entries.items(), key=lambda x: x[0].lower()))

        return sorted_dict

    def get_phonebook_reverse(self):
        """
        Get phonebook in reverse sorted order

        :return: Phonebook in reverse sorted order
        """

        reversed_dict = dict(sorted(self.entries.items(), reverse=True, key=lambda x: x[0].lower()))

        return reversed_dict

    def change_number(self, name, number):
        """
        Change number by name

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Numero atualizado' or 'Contato não encontrado'
        """

        if self.check_contact(name):
            self.entries[name] = number
            return 'Número atualizado'
        else:
            return 'Contato não encontrado'

    def get_name_by_number(self, number):
        """
        Get name by number

        :param number: number of person in string
        :return: Name or 'Contato não encontrado'
        """

        for nome, numero in self.entries.items():
            if numero == number:
                return nome
        return 'Contato não encontrado'

    def delete(self, name):
        """
        Delete person by name

        :param name: String with name
        :return: 'Contato deletado' or 'Contato não encontrado'
        """

        if self.check_contact(name):
            self.entries.pop(name)
            return 'Contato deletado'
        else:
            return 'Contato não encontrado'