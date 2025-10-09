# 🐧 Kali Linux Basic Commands (Roman Urdu Mein Easy Explanation)

Kali Linux ek **powerful Operating System** hai jo hackers aur cyber experts use karte hain.  
Agar tum beginner ho to ye **basic commands** zaroor seekho 👇

---

## 📂 1. Folder (Directory) Commands

| Command | Matlab | Example | Asaan Explanation |
|----------|---------|----------|-------------------|
| `pwd` | Path dekhna | `pwd` | Ye batata hai ke tum abhi kis folder ke andar ho. |
| `ls` | Files dikhana | `ls` | Ye current folder ke andar sab files/folders dikhata hai. |
| `ls -l` | Detail list | `ls -l` | Ye file ka size, date aur permission ke sath list dikhata hai. |
| `ls -a` | Hidden files | `ls -a` | Ye wo files bhi dikhata hai jo chhupi hoti hain (like `.bashrc`). |
| `cd foldername` | Folder change karna | `cd Downloads` | Ye tumhe kisi aur folder ke andar le jata hai. |
| `cd ..` | Ek step peeche | `cd ..` | Ye tumhe ek level upar le jata hai. |
| `cd ~` | Home folder | `cd ~` | Ye tumhe apne home folder mein le jata hai. |

---

## 🧾 2. File Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `touch` | Nayi file banana | `touch file.txt` | Ek new empty file banata hai. |
| `cat` | File dekhna | `cat file.txt` | File ke andar kya likha hai wo dikhata hai. |
| `nano` | File edit karna | `nano file.txt` | File edit karne ke liye open hoti hai. |
| `rm` | File delete karna | `rm file.txt` | File ko hamesha ke liye delete karta hai. ⚠️ |
| `cp` | File copy karna | `cp a.txt b.txt` | Ek file ko dusri jagah copy karta hai. |
| `mv` | Move/Rename file | `mv old.txt new.txt` | File ko move ya rename karta hai. |

---

## 📁 3. Folder Banane ya Delete Karne Ke Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `mkdir` | Naya folder banana | `mkdir test` | Ek new folder banata hai. |
| `rmdir` | Empty folder delete | `rmdir test` | Sirf khali folder delete karta hai. |
| `rm -r` | Folder aur sab kuch delete | `rm -r myfolder` | Folder ke andar sab delete kar deta hai. ⚠️ Careful! |

---

## ⚙️ 4. System Info Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `whoami` | Current user | `whoami` | Tumhara username batata hai. |
| `hostname` | PC ka naam | `hostname` | System ka naam dikhata hai. |
| `uname -a` | System info | `uname -a` | OS aur kernel ka version dikhata hai. |
| `uptime` | Kitne time se on hai | `uptime` | System kitni der se chalu hai batata hai. |
| `history` | Commands history | `history` | Pehle likhe huye commands dikhata hai. |

---

## 🔍 5. Search Karne Wale Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `find` | File dhoondhna | `find /home -name file.txt` | File ko poore system mein search karta hai. |
| `locate` | Fast search | `locate file.txt` | Jaldi se file ka path dikhata hai. |
| `grep` | Text dhoondhna | `grep "hello" file.txt` | File ke andar likha text dhoondhta hai. |

---

## 📦 6. Software Install / Update Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `sudo apt update` | Update list | `sudo apt update` | System ke software updates check karta hai. |
| `sudo apt upgrade` | Upgrade software | `sudo apt upgrade` | Installed software ko latest version mein karta hai. |
| `sudo apt install` | Install tool | `sudo apt install nmap` | New tool install karta hai. |
| `sudo apt remove` | Uninstall tool | `sudo apt remove nmap` | Installed tool delete karta hai. |

---

## 🔐 7. User Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `adduser` | Naya user banana | `sudo adduser ali` | Naya user create karta hai. |
| `passwd` | Password change | `passwd ali` | User ka password set/change karta hai. |
| `su` | User change karna | `su ali` | Dusre user ke account mein switch karta hai. |
| `logout` | Logout | `logout` | Current user se bahar nikal jaata hai. |

---

## 🌐 8. Internet / Network Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `ifconfig` | IP info | `ifconfig` | Tumhara IP address aur network info dikhata hai. |
| `ping` | Network check | `ping google.com` | Check karta hai internet chal raha hai ya nahi. |
| `netstat -tuln` | Ports dekhna | `netstat -tuln` | Kaunse ports active hain wo dikhata hai. |
| `curl` | Website ka data | `curl https://example.com` | Website se data fetch karta hai. |

---

## 🔄 9. File Permission Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `chmod` | Permission change | `chmod 755 file.sh` | File ka read/write/execute permission change karta hai. |
| `chown` | Owner change | `chown ali:ali file.txt` | File ka owner badalta hai. |

---

## 🧹 10. Extra Useful Commands

| Command | Matlab | Example | Easy Samajh |
|----------|---------|----------|-------------|
| `clear` | Screen saaf | `clear` | Terminal ka pura screen clean kar deta hai. |
| `man` | Command help | `man ls` | Command ka full detail help page kholta hai. |
| `exit` | Terminal band | `exit` | Terminal se nikal jaata hai. |

---

## 💡 Tips For Beginners

1. Linux case-sensitive hota hai (A ≠ a).  
2. Admin commands ke liye `sudo` use karo.  
3. Agar command yaad nahi to `man command` likh kar dekh lo.  
4. `Tab` key se auto-complete hota hai (bahut help karta hai).  
5. Always be careful with delete (`rm -r`) commands ⚠️

---

👨‍💻 **Author:** Tumhara Kali Linux Dost  
🧠 **Purpose:** Easy aur simple learning beginners ke liye  
📅 **Version:** 1.0 (Roman Urdu Edition)
