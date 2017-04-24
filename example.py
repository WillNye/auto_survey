import json

from run_survey import populate_survey


def main():
    with open('surveys.json') as f:
        surveys = json.loads(f.read())

    populate_survey(surveys['racetrac'])


if __name__ == '__main__':
    main()
