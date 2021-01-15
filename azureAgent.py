import argparse 


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    required_param_group = arg_parser.add_argument_group('required arguments') 
    required_param_group.add_argument('-k', '--key', required=True, help="Azure Function Key")
    args = arg_parser.parse_args()

    print(args.key)   