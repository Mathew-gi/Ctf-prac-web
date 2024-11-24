FROM ubuntu:20.04

RUN apt-get update && apt-get install -y vsftpd python3 && apt-get clean

# Создаем пользователя ftpuser
RUN useradd -m -d /home/ftpuser -s /bin/false ftpuser && \
    echo 'ftpuser:ftpuser' | chpasswd || echo "Password set skipped (for compatibility)"

# Создаем нужные каталоги
RUN mkdir -p /var/run/vsftpd/empty /home/ftpuser/ftp_root && \
    chown -R ftpuser:ftpuser /home/ftpuser && \
    chmod -R 755 /home/ftpuser

# Конфигурируем vsftpd
RUN echo "listen=YES\n\
anonymous_enable=NO\n\
local_enable=YES\n\
write_enable=NO\n\
chroot_local_user=YES\n\
allow_writeable_chroot=YES\n\
max_clients=15\n\
max_per_ip=15\n\
idle_session_timeout=60\n\
data_connection_timeout=120\n\
ftpd_banner=🐍 Welcome to the snake-server! 🐍\n\
pasv_enable=YES\n\
pasv_min_port=30000\n\
pasv_max_port=30010\n\
pasv_address=127.0.0.1\n\
secure_chroot_dir=/var/run/vsftpd/empty\n" > /etc/vsftpd.conf

# Удаляем утилиты чтения файлов
RUN rm -f /usr/bin/cat /usr/bin/strings /usr/bin/less /usr/bin/more \
/usr/bin/tail /usr/bin/head /usr/bin/nano /usr/bin/vi /usr/bin/vim \
/usr/bin/awk /usr/bin/sed /usr/bin/od /usr/bin/hexdump /usr/bin/tac \
/usr/bin/cut /usr/bin/split /usr/bin/grep /usr/bin/diff /usr/bin/cmp /usr/bin/dd /usr/bin/readlink


# Копируем скрипт генерации файлов
COPY generate_files.py /generate_files.py

# Генерируем файлы
RUN python3 /generate_files.py

WORKDIR /home/ftpuser/ftp_root

# Запускаем vsftpd
CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
