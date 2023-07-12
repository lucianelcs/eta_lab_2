from src.phonebook import Phonebook


class TestPhonebook:

    def test_add_success(self):
        phone = Phonebook()
        result = phone.add('Kátia', '123')
        expected = 'Número adicionado'

        assert  expected == result

    def test_add_invalid_character(self):
        phone = Phonebook()
        expected = 'Nome invalido'
        character = ['k#tia', 'k@tia', 'kat!a', 'kat$a', 'katia%']
        for name in character:
            result = phone.add(name,'1233333')

            assert  expected == result

    def test_add_invalid_number(self):
        phone = Phonebook()
        expected = 'Número invalido'
        result = phone.add('Kurama','')

        assert expected == result

    def test_add_exist_contact(self):
        phone = Phonebook()
        expected = 'Contato existe'
        phone.add('Kátia', '4353453535')

        result = phone.add('Kátia', '12333')

        assert expected == result

    def test_lookup_success(self):
        phone = Phonebook()
        expected = '123456'
        entries = {'Katia': '123456',
                   'Gabriel': '939399393'}

        for name, number in entries.items():
            phone.add(name, number)

        result = phone.lookup('Katia')

        assert expected == result

    def test_lookup_not_found(self):
        phone = Phonebook()
        expected = 'Contato não encontrado'
        entries = {'Junior': '1234356',
                   'Agatha': '939799393'}

        for name, number in entries.items():
            phone.add(name, number)

        result = phone.lookup('Tigresa')

        assert expected == result

    def test_get_names(self):
        phone = Phonebook()
        expected = ['Katia', 'Dororo']
        entries = {'Katia': '123456',
                'Dororo': '939399393'}
        for name, number in entries.items():
            phone.add(name, number)

        result = list(phone.get_names())

        assert expected == result

    def test_get_numbers(self):
        phone = Phonebook()
        expected = ['123456', '939399393']
        entries = {'Katia': '123456',
                'Dororo': '939399393'}
        for name, number in entries.items():
            phone.add(name, number)

        result = list(phone.get_numbers())

        assert expected == result

    def test_clear(self):
        phone = Phonebook()
        expected = 'phonebook limpo'
        phone.add('Kátia', '123')

        result = phone.clear()

        assert expected == result

    def test_search_success(self):
        phone = Phonebook()
        expected = {'Dororo': '939399393'}
        entries = {'Katia':'123456', 'Dororo': '939399393'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.search('Dororo')

        assert expected in result

    def test_search_not_found(self):
        phone = Phonebook()
        expected = 'Contato não encontrado'
        entries = {'Kurenai': '123456', 'Gabriel': '939399393'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.search('Naruto')

        assert expected == result

    def test_get_phonebook_sorted(self):
        phone = Phonebook()
        expected = {'Akamaru': '12345', 'bianca': '444444', 'Kurenai': '454656'}

        entries = {'Kurenai': '454656', 'bianca': '444444', 'Akamaru': '12345'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.get_phonebook_sorted()

        assert expected == result

    def test_get_phonebook_reverse(self):
        phone = Phonebook()
        expected = {'Zabimaru': '12345', 'tamara': '444444', 'Dororo': '454656'}

        entries = {'tamara': '444444', 'Zabimaru': '12345', 'Dororo': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.get_phonebook_reverse()

        assert expected == result

    def test_change_number_success(self):
        phone = Phonebook()
        expected = 'Número atualizado'
        name = 'Alexandre'
        new_number = '92993149719'
        entries = {'Alexandre': '12345', 'Renan': '444444', 'Lucas': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.change_number(name, new_number)

        assert expected == result

    def test_change_number_not_found(self):
        phone = Phonebook()
        expected = 'Contato não encontrado'
        nome = 'Noah'
        new_number = '92993143459'
        entries = {'Alexandre': '12345', 'Renan': '444444', 'Lucas': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.change_number(nome, new_number)

        assert expected == result

    def test_get_name_by_number_success(self):
        phone = Phonebook()
        expected = 'Lucas'
        entries = {'Alexandre': '12345', 'Renan': '444444', 'Lucas': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.get_name_by_number('454656')

        assert expected == result

    def test_get_name_by_number_not_found(self):
        phone = Phonebook()
        expected = 'Contato não encontrado'
        entries = {'Alexandre': '12345', 'Renan': '444444', 'Lucas': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.get_name_by_number('134234324324')

        assert expected == result

    def test_delete_success(self):
        phone = Phonebook()
        expected = 'Contato deletado'

        entries = {'Alexandre': '12345', 'Renan': '444444', 'Lucas': '454656'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.delete('Alexandre')

        assert expected == result

    def test_delete_user_not_found(self):
        phone = Phonebook()
        expected = 'Contato não encontrado'

        entries = {'Banana': '4334434', 'Pocahontas': '545434', 'Alegria': '656534'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.delete('Abacate')

        assert expected == result