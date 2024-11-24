import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall("Добро пожаловать в шифратор сообщений!\n".encode('utf-8'))
        self.request.sendall("Допустимые символы: \n".encode('utf-8'))
        ascii_table = """
            \\x00 \\x01 \\x02 \\x03 \\x04 \\x05 \\x06 \\x07 \\x08 \\x09 \\x0A \\x0B \\x0C \\x0D \\x0E \\x0F
            \\x10 \\x11 \\x12 \\x13 \\x14 \\x15 \\x16 \\x17 \\x18 \\x19 \\x1A \\x1B \\x1C \\x1D \\x1E \\x1F
            ' '   !    "    #    $    %    &    '    (    )    *    +    ,    -    .    /
            0    1    2    3    4    5    6    7    8    9    :    ;    <    =    >    ?
            @    A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
            P    Q    R    S    T    U    V    W    X    Y    Z    [   \\\\    ]    ^    _
            `    a    b    c    d    e    f    g    h    i    j    k    l    m    n    o
            p    q    r    s    t    u    v    w    x    y    z    {    |    }    ~  \\x7F
        """
        self.request.sendall(ascii_table.encode('utf-8'))
        self.request.sendall("Введите `q`, чтобы выйти.\n\n".encode('utf-8'))
        
        while True:
            try:
                self.request.sendall("Введите количество слов для пересылки: ".encode('utf-8'))
                count_messages = self.request.recv(1024).decode('utf-8').strip()
                if count_messages.lower() == "q":
                    self.request.sendall("До свидания!\n".encode('utf-8'))
                    break
                count_words = int(count_messages)
                number_of_message = 1
                output_string = ""

                while number_of_message <= count_words:
                    self.request.sendall(f"Введите сообщение {number_of_message} для пересылки: ".encode('utf-8'))
                    input_data = self.request.recv(1024).decode('utf-8').strip()

                    if input_data.lower() == "q":
                        self.request.sendall("До свидания!\n".encode('utf-8'))
                        return

                    if not all(0 <= ord(symbol) <= 127 for symbol in input_data):
                        self.request.sendall("Ошибка: недопустимые символы.\n".encode('utf-8'))
                        continue

                    output_string += encoder(input_data) + ' '
                    number_of_message += 1

                self.request.sendall(f"Зашифрованное сообщение: {output_string.strip()}\n".encode('utf-8'))

                if output_string.strip() == "I was exposed":
                    self.request.sendall("Поздравляем! Вы отправили сообщение штабу, теперь Вас вытащат из этой передряги.\nВот флаг: limeCTF{1t_15_hard_t0_b3_a_5py}\n".encode('utf-8'))
            except ValueError:
                self.request.sendall("Ошибка: введите корректное число.\n".encode('utf-8'))
            except Exception as e:
                self.request.sendall(f"Произошла ошибка: {e}\n".encode('utf-8'))

def encoder(input_string):
    try:
        ascii_input_string = [ord(symbol) for symbol in input_string]
        print("ascii_input_string: " + ascii_input_string)
        shift = max(ascii_input_string) if not(len(ascii_input_string) % 2) else sum(ascii_input_string) // 2
        print("shift" + shift)
        ascii_output_string = [element + shift for element in ascii_input_string]
        print("ascii_output_string" + ascii_output_string)
        output_string = ''.join(
            [
                chr(shift_ascii_symbol % 127) 
                for shift_ascii_symbol in ascii_output_string
            ]
        )
        return output_string
    except Exception as e:
        return f"Ошибка шифрования: {e}"

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 11111
    with socketserver.ThreadingTCPServer((HOST, PORT), Handler) as server:
        print(f"Сервис запущен на {HOST}:{PORT}")
        server.serve_forever()
