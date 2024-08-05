import os
import subprocess
from utils import get_current_date

def backup(site_directory, db_user, db_password):
    backup_dir = os.path.join(site_directory, 'backups', get_current_date())
    os.makedirs(backup_dir, exist_ok=True)

    files_backup_name = os.path.join(backup_dir, "site-backup.tar.gz")
    db_backup_name = os.path.join(backup_dir, "db-backup.sql")
    db_name = os.path.basename(site_directory)

    try:
        subprocess.check_call(["tar", "-czvf", files_backup_name, site_directory])
        subprocess.check_call(["mysqldump", "-u", db_user, f"-p{db_password}", db_name, "-r", db_backup_name])
        return "Backup completed successfully."
    except subprocess.CalledProcessError as e:
        return f"Backup failed: {e}"
