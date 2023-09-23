import requests
import argparse
import io
import gzip
import csv
import os


def main():

    parser = argparse.ArgumentParser(description="Displays the latest report for a given ID")
    # Argument for the configuration file
    parser.add_argument("-t", "--token",
                        type=str,
                        required=True,
                        help="API Token",
                        default=os.environ.get('SECURE_API_TOKEN', None))
    parser.add_argument("-a", "--api",
                        type=str,
                        required=True,
                        help="API URL to use",
                        default=os.environ.get('API_URL', None))
    parser.add_argument("-i", "--id",
                        type=str,
                        required=False,
                        default=None,
                        help="Report ID to Download")

    obj_config = parser.parse_args()

    arr_header = {'Authorization': 'bearer ' + obj_config.token}
    if obj_config.id is None:
        str_url = f"{obj_config.api}/api/scanning/reporting/v2/schedules"
        obj_result = requests.get(headers=arr_header,
                                  url=str_url)
        if obj_result.status_code == 200:
            arr_schedules = obj_result.json()
            for item in arr_schedules:
                print(f"Name: '{item['name']}', Id: '{item['id']}'")
    else:
        str_url = f"{obj_config.api}/api/scanning/reporting/v2/schedules/{obj_config.id}/download"
        obj_result = requests.get(headers=arr_header,
                                  url=str_url)
        if obj_result.status_code == 200:
            decompressed_content = gzip.decompress(obj_result.content)
            text_content = decompressed_content.decode('utf-8')
            str_csv_file = io.StringIO(text_content)

            # Read the CSV content
            csv_reader = csv.reader(str_csv_file,
                                    delimiter=',')
            for row in csv_reader:
                print(', '.join(row))


if __name__ == '__main__':
    main()
