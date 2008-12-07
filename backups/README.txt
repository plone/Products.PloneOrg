
Backup plone.org catalog and data.fs to aneka
=============================================

repozo.cron (antiloop):
    - repozo backups
    - can be run from cron 
    - stored in /srv/plone.org/backups

rsync.cron (aneka):
    - rsync of plone.org:/srv/plone.org 
    - can be run from cron
    - stored in /srv/backup.plone.org
