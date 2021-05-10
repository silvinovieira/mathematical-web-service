LOG_FILE = 'math-web-service.log'


def generate_report():
    with open(f'{LOG_FILE}', 'r') as log_file:
        log_data = log_file.read()
        report = []
        for function in ('Ackermann', 'Factorial', 'Fibonacci'):
            report.append({
                'function': function,
                'calls': log_data.count(f'{function.upper()}-ARGS'),
                'errors': log_data.count(f'{function.upper()}-ERROR'),
                'successful': log_data.count(f'{function.upper()}-CALC-RES'),
            })
    return report


if __name__ == '__main__':
    from tabulate import tabulate
    print(tabulate(generate_report(), headers='keys'))
