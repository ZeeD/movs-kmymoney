from sys import argv

from movs import read_txt

from .movskmymoney import write_csv


def main() -> None:
    src_fn = argv[1]
    dst_fn = argv[2]
    print(f'converting from {src_fn!r} to {dst_fn!r}')
    _, csv = read_txt(src_fn)
    write_csv(dst_fn, csv)
