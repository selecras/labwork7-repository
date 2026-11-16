def ip_address(ip: str) -> bool:
    try:
        ip = list(map(int, ip.split(".")))
    except ValueError:
        return False
    if len(ip) == 4:
        for num in ip:
            if not (0 <= num <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    tests = [
        "123.456.789.11",
        "192.168.0.1",
        "82.12.51.1",
        "abc.defg",
        "ab.ac.df.e",
        "12.41.51.",
        "1.1.1.1.1",
    ]
    for ip in tests:
        print(f"{ip} -- {ip_address(ip)}")
