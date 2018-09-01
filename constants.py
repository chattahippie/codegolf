"""
Constant values go here
"""
import os

PROBLEMS = list(range(1, 10))

VALID_EXTENSIONS = {
    'py': lambda x: ['python3', x],
    'js': lambda x: ['node', x]
}

PROGRAMS = VALID_EXTENSIONS.keys()


def make_instance_folder(app_instance):
    '''
    Create the needed folders
    '''
    incorrect = os.path.join(app_instance, 'programs', 'incorrect')
    tmp = os.path.join(app_instance, 'tmp')
    correct_problems = [os.path.join(
        app_instance, 'programs', 'correct', str(x)) for x in PROBLEMS]

    if not os.path.exists(incorrect):
        os.makedirs(incorrect)
    if not os.path.exists(tmp):
        os.makedirs(tmp)
    [os.makedirs(x) for x in correct_problems if not os.path.exists(x)]