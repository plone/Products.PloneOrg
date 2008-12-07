
Backup plone.org catalog and data.fs to aneka
=============================================

repozo.cron;
    - repozo backups run daily from cron on antiloop 
    - stored in plone.org:/srv/plone.org/backups

rsync.cron:
    - rsync of plone.org:/srv/plone.org 
    - run daily from cron on aneka
    - stored in aneka:/srv/backup.plone.org
