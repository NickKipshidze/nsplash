import random, os, time
import config

ESC = "\x1B"

BLOCKS = "▁▂▃▄▅▆▇█▓▒░"

color_fg = lambda code, bold = False: f"{ESC}[{int(bold)};{code}m"

def generate_wave() -> str:
    length: int = os.get_terminal_size().columns

    height: int = 1
    max_height: int = 8
    wave: str = ""

    for _ in range(length):
        height += random.choice([-1, 1])

        if height > max_height: height = max_height
        if height < 1: height = 1

        wave += BLOCKS[height-1]
    
    return wave

def output_wave(wave: str, animate: bool = True, delay: float = 0.01) -> None:
    length: int = len(wave)

    print(color_fg(random.randint(31, 36)))

    if animate:
        for char in range(length//2, length+1):
            print(f"{wave[length-char:char]:{BLOCKS[0]}^{length}}", end = "\r")
            time.sleep(delay)
    else:
        print(wave)

    print(end = "\n")

def main() -> None:
    output_wave(
        wave = generate_wave(),
        animate = config.ANIMATE_OUTPUT,
        delay = config.OUTPUT_DELAY
    )

    print(
        config.splash_text()
    )

if __name__ == "__main__":
    main()