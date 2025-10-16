# 📘 Git Commands Cheat Sheet

Yeh document Git ke most used commands ko simple aur easy words mein explain karta hai.

---

## 🔹 Basic Setup

1. **Check Git Version**

   ```bash
   git --version
   ```

   → Git install hua hai ya nahi aur konsa version hai, yeh check karein.

2. **Set Username**

   ```bash
   git config --global user.name "Your_Name"
   ```

   → GitHub ke liye ek username set karein.

3. **Set Email**

   ```bash
   git config --global user.email "your_email@example.com"
   ```

   → GitHub ke account wali email yahan likhni zaroori hai.

4. **Check Config Details**

   ```bash
   git config --list
   ```

   → Ab tak set ki gayi sari Git settings dikhayega.

5. **Edit Config**

   ```bash
   git config --global --edit
   ```

   → Username aur Email ko edit karne ke liye.

---

## 🔹 Directory Navigation (Git Bash / Terminal)

* `pwd` → Current directory ka path dikhata hai.
* `ls` → Current directory ke files/folders dikhata hai.
* `cd folder_name` → Kisi folder ke andar jaane ke liye.
* `cd ..` → Pichli directory mein wapas jane ke liye.

---

## 🔹 Start a New Project

1. **Initialize Git in a Project Folder**

   ```bash
   git init
   ```

   → Project ko Git se connect karta hai.

2. **Check Current Status**

   ```bash
   git status
   ```

   → Konsi files modified, untracked ya staged hain, dikhata hai.

3. **Add Files to Staging**

   ```bash
   git add file_name
   git add .
   ```

   → Specific file ya sari files ko staging area mein daalta hai.

4. **Commit Changes**

   ```bash
   git commit -m "Your message here"
   ```

   → Changes ko locally save karta hai ek message ke saath.

---

## 🔹 Work with Remote Repository (GitHub)

1. **Connect Local Project to GitHub Repo**

   ```bash
   git remote add origin <repo_link>
   ```

   → Local project ko GitHub repo se connect karta hai.

2. **Upload Project to GitHub**

   ```bash
   git push -u origin main
   ```

   → Local project ko GitHub pe bhejta hai.

3. **Clone a GitHub Repository**

   ```bash
   git clone <repo_link>
   ```

   → GitHub se poori repo download karta hai.

4. **Pull Latest Changes from GitHub**

   ```bash
   git pull origin main
   ```

   → GitHub se latest code apne local system mein laata hai.

---

## 🔹 Branch Management

1. **Create New Branch**

   ```bash
   git branch branch_name
   ```

   → Ek nayi branch banata hai.

2. **Create & Switch to New Branch**

   ```bash
   git checkout -b branch_name
   ```

   → Nayi branch banata hai aur usi pe switch kar deta hai.

3. **List All Branches**

   ```bash
   git branch
   ```

   → Sari branches dikhata hai.

4. **Switch Branch**

   ```bash
   git checkout branch_name
   ```

   → Kisi dusri branch pe switch karne ke liye.

5. **Delete Branch**

   ```bash
   git branch -d branch_name
   ```

   → Branch delete karta hai.

6. **Rename Branch**

   ```bash
   git branch -m new_branch_name
   ```

   → Branch ka naam change karta hai.

---

## 🔹 Logs & Commits

1. **View Commit History**

   ```bash
   git log
   ```

   → Detailed commit history dikhata hai.

2. **Short Commit History**

   ```bash
   git log --oneline
   ```

   → Ek line mein short history dikhata hai.

3. **Show Details of a Commit**

   ```bash
   git show commit_id
   ```

   → Specific commit ke details dikhata hai.

4. **Checkout Old Commit**

   ```bash
   git checkout commit_id
   ```

   → Purane commit ke code par wapas jane ke liye.

---

## 🔹 Compare & Merge

1. **Compare Current Branch with Main**

   ```bash
   git diff main
   ```

   → Current branch aur main branch ka difference dikhata hai.

2. **Merge Branch into Main**

   ```bash
   git checkout main
   git merge branch_name
   ```

   → Kisi branch ko main branch ke andar merge karta hai.

---

## 🔹 Reset / Delete Commits

```bash
git reset --soft commit_id   # Commit delete, code safe, staged
git reset --mixed commit_id  # Commit delete, code safe, unstaged
git reset --hard commit_id   # Commit + code delete (dangerous)
```
---
