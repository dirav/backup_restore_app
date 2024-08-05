import os
import subprocess

def restore(site_directory, backup_date, db_user, db_password):
    backup_dir = os.path.join(site_directory, 'backups', backup_date)
    files_backup_name = os.path.join(backup_dir, "site-backup.tar.gz")
    db_backup_name = os.path.join(backup_dir, "db-backup.sql")
    db_name = os.path.basename(site_directory)

    if not os.path.exists(files_backup_name) or not os.path.exists(db_backup_name):
        return "Backup files not found."

    try:
        subprocess.check_call(["tar", "-xzvf", files_backup_name, "-C", "/"])
        subprocess.check_call(["mysql", "-u", db_user, f"-p{db_password}", db_name, "<", db_backup_name], shell=True)
        return "Restore completed successfully."
    except subprocess.CalledProcessError as e:
        return f"Restore failed: {e}"
