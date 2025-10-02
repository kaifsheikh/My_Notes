IP vs Port — computer example (bahut simple)

IP address = tumhare computer ka ghar/building ka address.
Example: 192.168.1.10 — yeh batata hai kaunsa computer hai.

Port = us computer ke andar ek specific kamra/darwaza jahan koi program (service) sun raha hota hai.
Ek hi computer pe bahut saare programs alag-alag ports par sun (listen) kar sakte hain.

Real computer example — ek hi machine par multiple services

Maan lo tumhara laptop (IP 192.168.1.10) pe yeh programs chal rahe hain:

Port 80 → Apache / web server — website serve karta hai.
http://192.168.1.10:80 (browser)

Port 443 → HTTPS (secure web).
https://192.168.1.10 (browser auto 443 use karega)

Port 22 → SSH — remote login (terminal).
ssh user@192.168.1.10 (yahan port 22 default hai)

Port 3306 → MySQL database (usually not public).
Agar koi 192.168.1.10:3306 request bheje aur MySQL chal raha ho, to connection banega.

Port 27015 → Game server (for example, Counter-Strike server).
connect 192.168.1.10:27015 (game client se)

Port 515 → Printer sharing (old example).

Ek hi IP, lekin har service ka alag port — isliye ek hi machine pe web bhi chal sakta, SSH bhi, aur game server bhi — sab simultaneously.

Total ports = 65,536
Ports 0 se lekar 65,535 tak hotay hain. (0 bhi ek port maana jata hai — isliye total 65,536.)

Chhote examples:

22 → SSH (remote login)

80 → HTTP (web)

443 → HTTPS (secure web)

53 → DNS (aksar UDP par)

3306 → MySQL database
