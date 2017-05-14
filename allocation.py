def main():
    paper_heigth, paper_width = map(int, raw_input().split())
    card_height, card_width = map(int, raw_input().split())

    if not ((card_height > paper_heigth) or (card_width > paper_heigth)):
        parallel_count = (paper_heigth / card_height) * (paper_width / card_width)
        orthodox_count = (paper_width / card_height) * (paper_heigth / card_width)
        print max(parallel_count, orthodox_count)
    else:
        print 0


if __name__ == '__main__':
    main()