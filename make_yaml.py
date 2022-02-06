from pathlib import Path


tables_scheme = {
    'file_path': Path('configuration/tables.yaml'),
    'tables': {
        'speakers': {
            'columns': {
                'name': None,
                'surname': None,
                'telegram': None,
                'facebook': None,
                'vk': None,
            },
        },
        'meetups': None,
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
    }
}


def create_file(file_scheme) -> None:
    pass
