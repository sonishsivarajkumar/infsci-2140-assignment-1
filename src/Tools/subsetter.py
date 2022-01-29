import time


def write_n_from(in_path, out_path, delimiter, n=100000):
    count = 0

    with open(in_path, 'r', encoding="utf-8") as file_in:
        with open(out_path, 'w+', encoding="utf-8") as file_out:
            for read_line in file_in.readlines():
                file_out.write(f'{read_line}')

                if read_line.strip() == delimiter:
                    count += 1

                    if count % 1000 == 0:
                        print('count:', count)
                    if count >= n:
                        break


start_time = time.time()
write_n_from(
    in_path='data/output/docset.trectext',
    out_path='data/output/docset.100k.trectext',
    delimiter='</DOC>',
    n=100000)
print('time', time.time() - start_time)
