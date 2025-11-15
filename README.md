# OD Code Project

## VM Environment Setup Guide
* OS: Ubuntu 22.04 LTS
* Region: asia-east1(Taiwan)
* Machine type: e2-micro (1 vCPU, 1 GB memory)
* Disk: 10 GB Standard persistent disk
* Data protection: No backups

## Install Steps

### Step0. Sudo
```bash
sudo su
```

### Step1. Install Git
```bash
sudo apt update
sudo apt install -y git 
```

### Step2. Generate SSH Key Pair & Add to GitHub
```bash
ssh-keygen -t rsa -b 4096 -C "joe4od@gmail.com"
cat ~/.ssh/id_rsa.pub
```

### Step3. Install Docker
```bash
# 1.安裝前置套件
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

# 2.加入 Docker 官方 Repository
# 2-1. 新增 Docker GPG Key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 2-2.新增 Docker repo 到 apt sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 3.安裝 Docker Engine、Docker CLI、Containerd、Compose v2
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 4.確認 Docker 正常執行
sudo systemctl status docker

# 5. 測試docker compose是否已安裝
docker compose version
```

### Step4. Clone Repository
```bash
git clone git@github.com:joe4od/OD.git
```

### Step5. Run Application
```bash
# up
docker compose up -d
# down
docker compose down
```
### Step6. Python Run Example
```bash
python main/momo/momo_sign.py
```

## Background Running Services
```bash
# 背景執行python
nohup python main/momo/momo_memory_card.py > log.txt 2>&1 &

# 查看背景執行狀態
ps aux | grep python

# 停止背景執行
pkill -f momo_memory_card.py
```

## Other
```bash
# 安裝python套件
sudo apt update
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo python3 -m pip install -r requirements_auto.txt
```