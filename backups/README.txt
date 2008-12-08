
Backup plone.org catalog and data.fs to aneka
=============================================

antiloop/repozo.cron: 
    - repozo backups
    - can be run from cron 
    - stored in /srv/plone.org/backups

aneka/rsync.cron: 
    - rsync of plone.org:/srv/plone.org 
    - can be run from cron
    - stored in /srv/backup.plone.org
