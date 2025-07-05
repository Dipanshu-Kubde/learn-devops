# learn-devops

A simple repository to explore basic DevOps scripting in Python. This project includes example scripts for monitoring system uptime and disk usage, which are useful for learning foundational DevOps automation tasks.

## 📁 Project Structure

```
learn-devops/
├── dev.py                # Script to check system uptime
├── disk_usage_check.py  # Script to check disk space usage
```

## 🚀 Getting Started

These scripts require **Python 3** and are intended to be run on a Unix-based system (Linux/macOS) where the `uptime` command is available.

### Prerequisites

* Python 3.x
* Unix-based system (Linux/macOS)
* Basic understanding of terminal and Python scripting

### Running the Scripts

Clone the repository:

```bash
git clone https://github.com/your-username/learn-devops.git
cd learn-devops
```

#### 1. Check System Uptime

```bash
python3 dev.py
```

**Output Example:**

```
System Uptime: up 1 hour, 25 minutes
```

#### 2. Check Disk Usage

```bash
python3 disk_usage_check.py
```

**Output Example:**

```
Disk Usage on '/':
  Total: 100 GB
  Used:  45 GB
  Free:  55 GB
```

## 🧰 Use Cases

These scripts can be used as:

* Practice tools for beginners in DevOps
* Simple building blocks in larger monitoring/automation workflows
* Cron job scripts for system health checks
