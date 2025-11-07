import paramiko
import pytest

# Update with your target IP, username, and password
TARGET_IP = "192.168.1.50"
USERNAME = "root"
PASSWORD = "root"

@pytest.fixture(scope="session")
def ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(TARGET_IP, username=USERNAME, password=PASSWORD)
    yield ssh
    ssh.close()

def test_hostname(ssh_connection):
    """Verify target device responds over SSH and has a hostname"""
    stdin, stdout, stderr = ssh_connection.exec_command("hostname")
    hostname = stdout.read().decode().strip()
    print(f"Target hostname: {hostname}")
    assert hostname != "", "No hostname found"

def test_disk_space(ssh_connection):
    """Verify target has sufficient disk space"""
    stdin, stdout, stderr = ssh_connection.exec_command("df -h / | tail -1 | awk '{print $5}'")
    usage = stdout.read().decode().strip()
    print(f"Disk usage: {usage}")
    assert not usage.startswith("100"), "Disk full!"


