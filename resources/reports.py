from app import LOG_FILE


def generate_report():
    with open(f'../{LOG_FILE}', 'r') as log_file:
        log_data = log_file.read()
        calls = log_data.count('ARGS')
        errors = log_data.count('ERROR')
        successful = log_data.count('CALC-RES')
    return f'Calls: {calls}, errors: {errors}, successful: {successful}'


if __name__ == '__main__':
    print(generate_report())
