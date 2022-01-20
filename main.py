from robo.robo import run
import sys

try:
    users_styles = sys.argv[1]
except IndexError:
    users_styles = []

print(users_styles)

if __name__ == "__main__":
    run(users_styles)
