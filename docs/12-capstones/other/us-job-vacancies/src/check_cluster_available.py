from create_cluster import config_parse_file, aws_client, aws_open_redshift_port, check_cluster_creation, aws_resource, config_persist_cluster_infos


def main():
    config_parse_file()

    redshift = aws_client('redshift', "us-east-2")

    if check_cluster_creation(redshift):
        print('available')
        ec2 = aws_resource('ec2', 'us-east-2')
        config_persist_cluster_infos(redshift)
        aws_open_redshift_port(ec2, redshift)
    else:
        print('notyet')


if __name__ == '__main__':
    main()