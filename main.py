from capture import capture_data
from udp_gateway import UDPGateway
from fault_injection import FaultInjector

def main():
    img_udp_gateway = UDPGateway('127.0.0.1', 12345, chunk_size=1024)
    # lidar_udp_gateway = UDPGateway('127.0.0.1', 12346, chunk_size=1024)
    fault_injector = FaultInjector(drop_rate=0.1, modify_rate=0, delay_rate=0.1, delay_time=1.0, corruption_rate=0.1, reordering_rate=0)
    idx = 1

    for image, point_cloud in capture_data(idx):
        
        # image = fault_injector.inject_faults(image)
        # point_cloud = fault_injector.inject_faults(point_cloud)
        idx += 1
        
        if image:
            img_udp_gateway.send_data(image)
            print(f"Sent image[{idx}] data to {img_udp_gateway.ip}:{img_udp_gateway.port}")
        # if point_cloud:
        #     lidar_udp_gateway.send_data(point_cloud)
        #     print(f"Sent lidar[{idx}] data to {lidar_udp_gateway.ip}:{lidar_udp_gateway.port}")

if __name__ == "__main__":
    main()