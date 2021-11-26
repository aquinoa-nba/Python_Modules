#!/usr/bin/env python3

import sys


def sum_str(src):
    nbrs = src.split(' ')
    res = 0
    for i in nbrs:
        res += int(i)
    return str(res)


def start_html(f_out):
    f_out.write(
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "\t<meta charset=\"UTF-8\">\n"
        "\t<title>Periodic Table</title>\n"
        "\t<style>\n"
        "\t\t.element {\n"
        "\t\t\tborder: 1px solid black;\n"
        "\t\t\tpadding:10px;\n"
        "\t\t}\n"
        "\t</style>\n"
        "</head>\n"
        "<body>\n"
        "<table>\n"
    )


def add_elem_to_table(elem, prev_pos):
    html = str()
    for i in range(int(elem[1].get('position')) - prev_pos - 1):
        if i == 0:
            html += '\t\t'
        html += '<td></td>'
    if elem[1].get('position') == '0':
        html += "\t<tr>"
    html += "\n\t\t<td class=\"element\">\n"
    html += "\t\t\t<h4>"
    html += str(elem[0])
    html += "</h4>\n"
    html += "\t\t\t<ul>\n"
    html += "\t\t\t\t<li>No "
    html += str(elem[1].get('number'))
    html += "</li>\n"
    html += "\t\t\t\t<li>"
    html += str(elem[1].get('small'))
    html += "</li>\n"
    html += "\t\t\t\t<li>"
    html += str(elem[1].get('molar'))
    html += "</li>\n"
    html += "\t\t\t\t<li>"
    html += str(sum_str((elem[1].get('electron'))))
    html += " electron"
    html += "</li>\n"
    html += "\t\t\t</ul>\n"
    html += "\t\t</td>\n"
    if elem[1].get('position') == '17':
        html += "\t</tr>\n"
    return html


def end_html(f_out):
    f_out.write(
        "</table>\n"
        "</body>\n"
        "</html>"
    )


def make_params(params):
    splt_params = params.split(',')
    dic = {}
    for i in range(len(splt_params)):
        splt_params[i] = splt_params[i].strip()
    for i in splt_params:
        para_params = i.split(':')
        dic[para_params[0]] = para_params[1].strip()
    return dic


def dict_from_file(f_in):
    elements = {}
    for line in f_in:
        param = line.split('=')
        elements[param[0].strip()] = make_params(param[1])
    return elements


def make_table(f_out, elements):
    start_html(f_out)
    prev_elem_pos = 0
    for elem in elements.items():
        f_out.write(add_elem_to_table(elem, prev_elem_pos))
        prev_elem_pos = int(elem[1].get('position'))
    end_html(f_out)


if __name__ == '__main__':
    if len(sys.argv) == 2 or len(sys.argv) == 1:
        try:
            if len(sys.argv) == 2:
                f_in = open(sys.argv[1], 'r')
            else:
                f_in = open('periodic_table.txt', 'r')
            elements = dict_from_file(f_in)
            f_in.close()
            f_out = open("periodic_table.html", 'w')
            make_table(f_out, elements)
            f_out.close()
        except IOError:
            pass
