import requests
import uuid
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact

@task
def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        raise e
    return data

@task
def update_data(data):
    desired_fields = ['PatientId', 'PatientName', 'Collection']
    updated_record = []
    for record in data:
        new_dict = {key: record[key] for key in desired_fields}
        new_dict['PatientId'] = str(uuid.uuid4())
        updated_record.append(new_dict)
    return updated_record

@task
def print_data(data):
    for record in data:
        print(record)

@task
def create_markdown(data):
    markdown_report = "| PatientId | PatientName | Collection |\n"
    markdown_report += "|-----------|-------------|------------|\n"
    for record in data:
        markdown_report += f"| {record['PatientId']} | {record['PatientName']} | {record['Collection']} |\n"
    create_markdown_artifact(
        key="collection-report",
        markdown=markdown_report,
        description="simplified records of patient name with collection and unique identifier",
    )

@flow
def main():
    request_date = '2010/08/16'
    url = f"https://services.cancerimagingarchive.net/nbia-api/services/v1/NewPatientsInCollection?Collection=CBIS-DDSM&Date={request_date}"
    try:
        data = get_data(url)
        if data:
            data = update_data(data)
            create_markdown(data)
        else:
            print(f"No data to process for date: {request_date}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

