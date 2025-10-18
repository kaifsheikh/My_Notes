# What is File System?
1. Linux (ya kisi bhi operating system) mein file system wo system hota hai jo data ko organize karta hai — matlab, files aur folders kahan store hain, kaise save hote hain, kaise read hote hain, aur kaise delete hote hain.

# Linux File System?
1. File System Linux ka wo part hai jo data ko arrange aur manage karta hai — matlab files, folders, programs, aur settings sab isi system ke zariye handle hoti hain.

### 1. `/` – Root Directory
1. Linux mein sab kuch ek **main folder “/”** (slash) se start hota hai.
2. Is “/” ko **Root Directory** kehte hain — matlab sab folders isi ke andar hote hain.

3. Yeh **Linux ka main ghar (base)** hota hai.  
Iske andar saare important folders hote hain.

## Example:  
1. bin
2. home
3. etc
4. var

2. /home – Tumhara Data

Yahan har user ka apna data hota hai.

Example:

/home/ali → Ali ka folder

/home/sana → Sana ka folder

Yahan tum documents, photos, songs sab rakhte ho.
Phone ke “My Files” jaisa samajh lo.

3. /root – Boss ka Folder

Ye admin (root user) ka folder hai.
Jo sabse powerful banda hota hai system mein.
Usko sab jagah ka access milta hai.

### 1. `/`bin - Tool Box

1. /bin ka matlab hota hai "binary" —
aur “binary” ka matlab hota hai programs ya commands jo computer samajhta hai.

2. /bin wo folder hai jisme basic commands aur programs rakhe hote hain
jo har user use kar sakta hai (normal user bhi, aur admin bhi).

### 5. `/`etc

1. /etc ek bohot important folder hai Linux system mein.
Is folder ka kaam hota hai: System ke rules aur settings ko store karna.
2. Har program aur service ki configuration files yahin hoti hain.
3. Soch lo /etc ek control room hai jahan se Linux system ke sab “rules aur settings” handle hote hain.

6. /var – Changing Data

Yahan wo files hoti hain jo bar-bar change hoti rehti hain.
Jaise:

Logs (system ne kya kya kiya likha rehta hai)

Cache (temporary data)

7. /tmp – Temporary Folder

Yahan wo files aati hain jo kuch der ke liye chahiye hoti hain.
Jab system band hota hai, ye delete ho jaati hain.
Jaise download ke time temporary files.

8. /usr – Software Wale Programs

Yahan wo programs hote hain jo users install karte hain.
Jaise browsers, games, ya koi app.

9. /dev – Devices Wala Folder

Linux mein har device (jaise USB, hard drive) ek file ke form mein hoti hai.
Example:

/dev/sda → hard drive

/dev/usb → pendrive

Matlab hardware bhi file jaisa dikhai deta hai.

10. /boot – System Start Hone Wali Files

Yahan wo files hoti hain jisse Linux on (boot) hota hai.
Jaise kernel aur bootloader.


https://youtu.be/cKEf8H9cQGM?si=BQV1_1l_3Otroin1&t=11469