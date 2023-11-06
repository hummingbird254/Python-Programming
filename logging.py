import logging, secrets

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def pass_gen():
    pin = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    length = secrets.randbelow(11)
    logging.info(f"Length choice:{length}")

    for x in range(length):
        y = secrets.choice(numbers)
        pin.append(y)

    pin_str = "".join(str(x) for x in pin)
    logging.info(f"string pin{pin_str}")
    actual_pin = int(pin_str)
    logging.info(f"Actual pin:{actual_pin}")
    return actual_pin


global_pin = pass_gen()



# numbers = 9999999999
# for x in range(numbers):
#     if x == global_pin:
#         print(x)



