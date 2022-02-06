from pathlib import Path

import yaml

tables_scheme = {
    'file_path': Path('configuration/tables.yaml'),
    'tables': {
        'speakers': {
            'columns': {
                'id': {
                    'format': ['int', 'NOT NULL'],
                    'primary_key': [True, 'AUTO_INCREMENT'],
                    'description': '',
                },
                'name': {
                    'format': ['text', 'NOT NULL'],
                    'primary_key': [False],
                    'description': '',
                },
                'surname': None,
                'organization': None,
                'experience': None,
                'activity_sphere ': None,
                'other_information': None,
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
