from fabric import Connection, task
import os
@task 
def deploy(ctx):
    local_static_dir = os.path.join(os.path.expanduser('~'), 'alx-higher_level_programming', 'CODE_STUDY', 'HTML', 'project_a')
    remote_static_dir = '/var/www/project_a'

    conn = Connection(host='107.23.139.92', user='ubuntu', connect_kwargs={"key_filename": "/home/mpolyon/.ssh/id_rsa"})

    #Ensure the remote directory exists
    conn.run(f'sudo mkdir -p {remote_static_dir}')

   # Transfer static files with sudo privileges
    conn.sudo(f'put {local_static_dir}/* {remote_static_dir}')
    
    conn.run(f'chmod -R 755 {remote_static_dir}')
    conn.run('sudo systemctl reload nginx')

if __name__ == "__main__":
    deploy()