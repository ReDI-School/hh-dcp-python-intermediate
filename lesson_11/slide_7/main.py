import time
# install with pip install wikipedia
import wikipedia

def fetch_wikipedia(language = 'de') -> str:
    wikipedia.set_lang(language)
    return wikipedia.summary("Python")

def count_words(text: str) -> int:
    return len(text.split())


def run() -> tuple[float, int]:
    start_time = time.time()
    text = fetch_wikipedia()
    end_time = time.time()
    return end_time - start_time, count_words(text)

if __name__ == '__main__':
    duration, words = run()
    print(f"Words: {words}")
    print(f"Duration: {duration} seconds.")
