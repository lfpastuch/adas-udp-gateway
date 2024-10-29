import socket

class UDPGateway:
    def __init__(self, ip, port, chunk_size=1024):
        self.ip = ip
        self.port = port
        self.chunk_size = chunk_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_data(self, data):
        # Split data into chunks and add chunk index
        total_chunks = (len(data) + self.chunk_size - 1) // self.chunk_size
        total_chunks_bytes = total_chunks.to_bytes(4, byteorder='big')
        
        for i in range(0, len(data), self.chunk_size):
            chunk_index = i // self.chunk_size
            chunk_index_bytes = chunk_index.to_bytes(4, byteorder='big')
            chunk = chunk_index_bytes + total_chunks_bytes + data[i:i + self.chunk_size]
            self.sock.sendto(chunk, (self.ip, self.port))
            print(f"Sent chunk {chunk_index}/{total_chunks} to {self.ip}:{self.port}")