from app import LOG_FILE


def generate_report():
    with open(f'../{LOG_FILE}', 'r') as log_file:
        log_data = log_file.read()
        errors = log_data.count('ERROR')
    return f'Errors: {errors}'


if __name__ == '__main__':
    print(generate_report())
