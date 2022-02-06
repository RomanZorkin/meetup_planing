from pathlib import Path

import yaml

tables_scheme = {
    'file_path': Path('configuration/tables.yaml'),
    'tables': {
        'speakers': {
            'description': 'ндекс строк',
            'columns': {
                'id': {
                    'format': ['int', 'NOT NULL'],
                    'primary_key': [True, 'AUTO_INCREMENT'],
                    'description': 'индекс строк',
                },
                'name': {
                    'format': ['text', 'NOT NULL'],
                    'primary_key': [False],
                    'description': 'Имя спикера',
                },
                'surname': {
                    'format': ['text', 'NOT NULL'],
                    'primary_key': [False],
                    'description': 'Фамилия спикера',
                },
                'organization': {
                    'format': ['text', 'NULL'],
                    'primary_key': [False],
                    'description': 'Место работы текущее (елси, нет то предыдущее)',
                },
                'experience': {
                    'format': ['text', 'NULL'],
                    'primary_key': [False],
                    'description': 'Опыт работы ',
                },
                'activity_sphere ': {
                    'format': ['text', 'NULL'],
                    'primary_key': [False],
                    'description': 'язык, направление деятельности(ML, web...)',
                },
                'other_information': {
                    'format': ['text', 'NULL'],
                    'primary_key': [False],
                    'description': 'Иная полезная информация',
                },
            },
        },
        'meetups': None,
        'social_net': {
            'name': None,
            'speaker': None,
            'address': None,
        },
        'messages': {
            'columns': {
                'general_theme': None,
                'exact_theme': None,
                'description': None,
                'period_start': None,
                'period_finish': None,
            },
        },
        'themes': None,
        'areas': None,
    },
}


def create_file(file_scheme) -> None:
    with open(file_scheme['file_path'], 'w') as target_file:
        yaml.dump(file_scheme['tables'], target_file, default_flow_style=False)


create_file(tables_scheme)
