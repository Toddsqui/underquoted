#!/bin/bash

# This script will quit on the first error that is encountered.
set -e

CIRCLE=$1

DEPLOY_DATE=`date "+%FT%T%z"`

heroku config:set --app=underquoted \
NEW_RELIC_APP_NAME='underquoted' \
ADMIN_EMAIL="the.underquoted@gmail.com" \
ADMIN_NAME="the.underquoted" \
DJANGO_SETTINGS_MODULE=underquoted.settings.production \
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY \
DEPLOY_DATE="$DEPLOY_DATE" \
> /dev/null

if [ $CIRCLE ]
then
    git push git@heroku.com:underquoted.git $CIRCLE_SHA1:refs/heads/master
else
    git push heroku master
fi

heroku run python manage.py syncdb --noinput --app=underquoted
heroku run python manage.py migrate --noinput --app=underquoted
heroku run python manage.py update_search_field quotations --app=underquoted
