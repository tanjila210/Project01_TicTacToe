def main(args=None):
    print("hello")

if __name__ == "__main__":
    # call main function with ctrl-c handling
    try:
        main()
    except KeyboardInterrupt:
        # add ctrl-c handling here, default is do nothing
        print("Code terminated")
        pass
