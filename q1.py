# TO BE UPDATED
import sys


def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    line = f.readlines()
    f.close()

    return line


def reverse_string(string):
    return string[::-1]


def string_match(string, r, l):
    len_string = len(string)
    return r < len_string and string[r] == string[r - l]


def z_algorithm_list(combined_str):
    len_combined = len(combined_str)
    z_lst = [None] * len_combined
    left = 0
    right = 0

    for i in range(1, len_combined):
        # Base case or Case 1
        if i > right:
            left = i
            right = i
            while string_match(combined_str, right, left):
                right += 1
            z_lst[i] = right - left
            right -= 1

        else:
            k = i - left
            if z_lst[k] < right - i + 1:
                z_lst[i] = z_lst[k]
            else:
                left = i
                while string_match(combined_str, right, left):
                    right += 1
                z_lst[i] = right - left
                right -= 1

    return z_lst


# concatenating pattern and text with a '$' symbol
def combine_text_pattern(txt, pat):
    original_string = '$'.join([pat, txt])
    reversed_string = '$'.join([reverse_string(pat), reverse_string(txt)])
    return original_string, reversed_string


def find_pattern_allow_transposition(txt, pat):
    if len(pat) == 0 or len(txt) < len(pat):
        return []

    og_string, rev_string = combine_text_pattern(txt, pat)
    # taking a list of z-algorithm just of the text (pattern and '$' are excluded)
    og_string_lst = z_algorithm_list(og_string)[len(pat) + 1:]
    rev_string_lst = z_algorithm_list(rev_string)[len(pat) + 1:]
    rev_string_lst.reverse()

    # logic to why calculate_lst is created will be written in the pdf.
    calculate_lst = []

    for i in range(len(txt) - len(pat) + 1):
        calculate_lst.append(og_string_lst[i] + rev_string_lst[i + len(pat) - 1])

    result = []

    # Complexity: O(n - m) where n is the length of the text and m is the length of the pattern
    for j in range(len(calculate_lst)):
        if calculate_lst[j] / 2 == len(pat):
            # convert to index-1 based
            result.append(str(j + 1))
        elif calculate_lst[j] + 2 == len(pat):

            index = og_string_lst[j]
            transposition = pat[index: index + 2]
            txt_string = og_string[len(pat) + 1:]
            if txt_string[j + index: j + index + 2] == reverse_string(transposition):
                # change to index-1 based
                next_ans = [str(j + 1), str(j + index + 1)]
                result.append(" ".join(next_ans))

    return result


if __name__ == '__main__':
    t = read_file(sys.argv[1])
    p = read_file(sys.argv[2])

    text = ''
    pattern = ''

    if len(t) > 0:
        text = t[0]

    if len(p) > 0:
        pattern = p[0]

    res = find_pattern_allow_transposition(text, pattern)

    n = str(len(find_pattern_allow_transposition(text, pattern)))

    with open('output_q1.txt', 'w') as f:
        f.write(n)
        f.write('\n')
        f.write('\n'.join(res))



