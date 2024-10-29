import socket
import os

IMAGE_PATH = './received_images/reassembled_image_{:06d}.jpg'

def start_udp_server(ip, port):
    img_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    img_sock.bind((ip, port))
    print(f"UDP server listening on {ip}:{port} for images")

    # Create a directory to store the received image chunks
    os.makedirs('received_images', exist_ok=True)
    # Determine the starting index based on the latest file in the directory
    existing_files = [f for f in os.listdir('received_images') if f.startswith('reassembled_image_') and f.endswith('.png')]
    if existing_files:
        latest_file = max(existing_files, key=lambda x: int(x.split('_')[2].split('.')[0]))
        idx = int(latest_file.split('_')[2].split('.')[0]) + 1
    else:
        idx = 1

    image_chunks = {}
    expected_chunks = None

    while True:
        img_data, addr = img_sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message: {img_data[:32].hex()} from {addr}")

        # Assuming the first 4 bytes of img_data contain the chunk index
        chunk_index = int.from_bytes(img_data[:4], 'big')
        total_chunks = int.from_bytes(img_data[4:8], 'big')

        print(f"Chunk index: {chunk_index}, Total chunks: {total_chunks}")

        if expected_chunks is None:
            expected_chunks = total_chunks

        # Store the chunk data
        image_chunks[chunk_index] = img_data[8:]

        # Check if we have received all chunks
        if len(image_chunks) == expected_chunks:
            # Reassemble the image
            image_data = b''.join(image_chunks[i] for i in range(expected_chunks))
            with open(IMAGE_PATH.format(idx), 'wb') as f:
                f.write(image_data)
            print("Image reassembled and saved as '" + IMAGE_PATH.format(idx) + "'")

            # Reset for the next image
            image_chunks = {}
            expected_chunks = None
            idx += 1

if __name__ == "__main__":
    start_udp_server('127.0.0.1', 12345)