from ansible import errors


def wildcard_ip(ip_address, octets_to_replace=1):
    """
    :param ip_address:
    :param octets_to_replace:
    :return:
    """

    split_ip_address = ip_address.split('.')
    arr_len = len(split_ip_address)-1

    for item in range(arr_len, arr_len-octets_to_replace, -1):
        split_ip_address[item] = "*"

    return ".".join(split_ip_address)


class FilterModule(object):
    def filters(self):
        filter_list = {
            'wildcard_ip': wildcard_ip
        }
        return filter_list
