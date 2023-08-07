GAMETIME:
gulp; gulp build
set up S3 and cloudfront in AWS, then set config vars in heroku
set ALLOWED_HOSTS and DEBUG
set up redis/postgres
set DISABLE_COLLECTSTATIC=1
set SECRET_KEY for django
push it

To build: 
docker-compose up --build


To create superuser:
docker-compose exec web python manage.py createsuperuser --settings=app.settings.dev


To push to heroku:
git subtree push --prefix app heroku master


If wanting to use django_debug_toolbar, be sure to change INTERNAL_IPS in settings/base.py, find heroku internal by using page.views.internal_addr


Set S3 with s3cors.json:
aws configure
aws s3api put-bucket-cors --bucket <BUCKETEER_BUCKET_NAME>  --cors-configuration file://s3cors.json

Confirming cors set:
aws s3api get-bucket-cors --bucket <BUCKETEER_BUCKET_NAME> --output json


To restore media:
docker-compose exec web python manage.py restore_media

To restore latest.dump: (In directory with docker-compose.yml)
heroku pg:backups:capture
heroku pg:backups:download

docker-compose down
docker-compose up db
docker-compose exec db bash -c 'env dropdb $POSTGRES_DB -U $POSTGRES_USER; createdb $POSTGRES_DB -U $POSTGRES_USER; pg_restore --clean --if-exists --no-acl --no-owner -d $POSTGRES_DB -U $POSTGRES_USER latest.dump'

heroku config:set DISABLE_COLLECTSTATIC=1
aws cloudfront create-invalidation --distribution-id <DISTRIBUTION_ID>--paths "/public/css/*"
aws s3 cp /app/app/static/css/ s3://<AWS_STORAGE_BUCKET_NAME>/public/ --recursive

heroku run python manage.py collectstatic --settings=app.settings.production --noinput
