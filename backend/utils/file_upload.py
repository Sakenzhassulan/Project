def university_path(instance, filename):
    university = instance.name
    return 'universities/{}/{}'.format(university, filename)


def professor_path(instance, filename):
    professor = instance.full_name
    return 'professor/{}/{}'.format(professor, filename)
