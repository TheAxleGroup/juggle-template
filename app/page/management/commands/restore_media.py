import json
import os
import boto3

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


def download_dir(client, resource, dist, bucket, local='/tmp'):
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                if '/images/' in subdir.get('Prefix') or '/original_images/' in subdir.get('Prefix'):
                    print('\n') # \n\n
                    download_dir(client, resource, subdir.get('Prefix'), bucket, local)
                else:
                    print('SKIPPING DIR', subdir.get('Prefix'))

        if result.get('Contents') is not None:
            for file in result.get('Contents'):
                print(file.get('Key'))
                file_path = file.get('Key')
                if 'public' in file_path.split('/')[0]:
                    file_path = '/'.join(file_path.split('/')[1:])
                print('->', local + os.sep + file_path)
                print()
                if not os.path.exists(os.path.dirname(local + os.sep + file_path)):
                    os.makedirs(os.path.dirname(local + os.sep + file_path))
                resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file_path)


class Command(BaseCommand):
    help = 'Restore media from s3'

    def add_arguments(self, parser):
        parser.add_argument('--bucket-name', type=str, help='AWS_STORAGE_BUCKET_NAME')
        parser.add_argument('--access-key', type=str, help='AWS_ACCESS_KEY_ID')
        parser.add_argument('--secret-access-key', type=str, help='AWS_SECRET_ACCESS_KEY')
        parser.add_argument('--force', action='store_true', dest='force')

    def handle(self, *args, **options):
        AWS_STORAGE_BUCKET_NAME = options['bucket_name']
        AWS_ACCESS_KEY_ID = options['access_key']
        AWS_SECRET_ACCESS_KEY = options['secret_access_key']

        if AWS_STORAGE_BUCKET_NAME is None or AWS_ACCESS_KEY_ID is None or AWS_SECRET_ACCESS_KEY is None:
            secrets_dir = settings.BASE_DIR + '/secrets.json'
            self.stdout.write(self.style.WARNING(
                "Not all arguments provided, attempting to load AWS from settings.BASE_DIR/secrets.json (%s)" % secrets_dir
            )
            )
            self.stdout.write(self.style.WARNING(
                "Looking for keys PROD_AWS_S3_BUCKET_NAME, PROD_AWS_ACCESS_KEY_ID, PROD_AWS_SECRET_ACCESS_KEY"
            )
            )

            secrets = json.load(open(secrets_dir))
            AWS_STORAGE_BUCKET_NAME = secrets["PROD_AWS_S3_BUCKET_NAME"]
            AWS_ACCESS_KEY_ID = secrets["PROD_AWS_ACCESS_KEY_ID"]
            AWS_SECRET_ACCESS_KEY = secrets["PROD_AWS_SECRET_ACCESS_KEY"]


        self.stdout.write(self.style.WARNING(
            '\nAWS_STORAGE_BUCKET_NAME: ' + AWS_STORAGE_BUCKET_NAME
            )
        )

        self.stdout.write(self.style.WARNING(
            'AWS_ACCESS_KEY_ID: ' + AWS_ACCESS_KEY_ID
            )
        )

        self.stdout.write(self.style.WARNING(
            'AWS_SECRET_ACCESS_KEY: ' + AWS_SECRET_ACCESS_KEY
            )
        )

        self.stdout.write(self.style.WARNING(
                '\nIs the above entered information correct?\n'
            )
        )
        confirm = input('Enter "YES" to confirm: ')  #nosec
        if confirm != 'YES':
            return

        client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        resource = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        download_dir(client, resource, 'public/', AWS_STORAGE_BUCKET_NAME, settings.MEDIA_ROOT)

        self.stdout.write(self.style.SUCCESS(
                '\nDONE'
            )
        )
