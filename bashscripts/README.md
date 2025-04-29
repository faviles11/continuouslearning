# 🧠 Linux Cheat Sheet – Organized by Functional Blocks

## 1. System

| Administration                             | Troubleshooting                              |
| ------------------------------------------ | -------------------------------------------- |
| `adduser fabian` – Create user             | `ls -la` – View permissions and ownership    |
| `usermod -aG sudo fabian` – Add to group   | `stat file.txt` – File details               |
| `passwd fabian` – Change user password     | `top` / `htop` – Check CPU and memory usage  |
| `chmod 755 file` – Change permissions      | `strace -p PID` – Trace process system calls |
| `chown user:group file` – Change ownership | `ps aux` – List all processes                |
| `kill -9 PID` – Kill a process             | `journalctl -xe` – View recent system errors |

---

## 2. Files & Storage

| Administration                                   | Troubleshooting                                    |
| ------------------------------------------------ | -------------------------------------------------- |
| `mkdir -p /path/dir` – Create nested directories | `df -h` – Disk space usage                         |
| `cp`, `mv`, `rm` – Basic file operations         | `du -sh *` – Folder size usage                     |
| `touch file.txt` – Create an empty file          | `find / -size +100M` – Find large files            |
| `mount /dev/sdX /mnt` – Mount a disk             | `iotop` – Show disk I/O per process (if installed) |

---

## 3. Networking

| Administration                                | Troubleshooting                               |
| --------------------------------------------- | --------------------------------------------- |
| `ip a` – Show interfaces and IPs              | `ping 8.8.8.8` – Test connectivity            |
| `hostname -I` – Show host IP                  | `curl -I http://site.com` – View HTTP headers |
| `nmcli` – Network configuration (interactive) | `ss -tulwn` – Show open ports                 |
|                                               | `traceroute google.com` – Trace network path  |
|                                               | `dig domain.com` – Test DNS resolution        |

---

## 4. Services & Daemons (systemd)

| Administration                                            | Troubleshooting                                              |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| `systemctl start nginx` – Start service                   | `systemctl status nginx` – Service status and logs           |
| `systemctl stop nginx` – Stop service                     | `journalctl -u nginx` – Service-specific logs                |
| `systemctl restart nginx` – Restart service               | `systemctl list-units --failed` – View failed units          |
| `systemctl enable nginx` – Start on boot                  | `journalctl -b` – Logs from current boot session             |
| `systemctl list-units --type=service` – List all services | `systemctl daemon-reexec` / `daemon-reload` – Reload configs |
| `.service` files stored in `/etc/systemd/system/`         |                                                              |

---

## 5. Automation & Packages

| Administration                              | Troubleshooting                                        |
| ------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| `apt update && apt upgrade` – Update system | `dpkg -l                                               | grep name` – Check if a package is installed   |
| `apt install nginx` – Install software      | `which command` – Locate an executable                 | |
| `crontab -e` – Edit user cron jobs          | `grep CRON /var/log/syslog` – Check cron logs (Debian) | |
| `crontab -l` – List scheduled tasks         | `journalctl                                            | grep CRON` – Check cron logs (systemd distros) |

## 6. Linux Directory Structure

| Directory        | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `/`              | Root directory. All files and directories start from here.              |
| `/bin`           | Essential user binaries (e.g., `ls`, `cp`, `mv`) used during boot.      |
| `/sbin`          | System binaries (e.g., `ifconfig`, `reboot`) used by root/admins.       |
| `/etc`           | System configuration files (e.g., network, users, services).            |
| `/home`          | User directories. Each user has a folder like `/home/fabian`.           |
| `/root`          | Home directory for the root user.                                       |
| `/var`           | Variable data files – logs, spool files, mail, etc.                     |
| `/var/log`       | System logs and service logs (e.g., `syslog`, `auth.log`).              |
| `/usr`           | User-installed software and libraries.                                  |
| `/usr/bin`       | Most user commands and apps installed here.                             |
| `/usr/local`     | Locally compiled software (outside package manager control).            |
| `/opt`           | Optional third-party apps (often commercial software).                  |
| `/lib`, `/lib64` | Libraries needed by binaries in `/bin` and `/sbin`.                     |
| `/dev`           | Device files (e.g., `/dev/sda`, `/dev/null`).                           |
| `/proc`          | Virtual filesystem for system and process info (e.g., `/proc/cpuinfo`). |
| `/sys`           | Interface to the kernel (hardware info, drivers, etc.).                 |
| `/tmp`           | Temporary files. Cleared on reboot.                                     |
| `/mnt`           | Mount point for temporary storage (USB, ISO, etc.).                     |
| `/media`         | Mount point for removable devices (automatically mounted).              |
| `/boot`          | Kernel and bootloader files (e.g., `vmlinuz`, `grub`).                  |
| `/run`           | Runtime data for processes started since boot (e.g., PID files).        |
