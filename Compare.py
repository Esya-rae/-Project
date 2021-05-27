def fill_compare_matrix(pronunciation, word_phonemes):
    compare_matrix = [[0] * (len(word_phonemes) + 1) for i in range(len(pronunciation) + 1)]
    for i in range(1, len(pronunciation) + 1):
        for j in range(1, len(word_phonemes) + 1):
            if pronunciation[i - 1] == word_phonemes[j - 1]:
                compare_matrix[i][j] = compare_matrix[i - 1][j - 1] + 1
            else:
                compare_matrix[i][j] = max(compare_matrix[i - 1][j], compare_matrix[i][j - 1])
    return compare_matrix


def find_right_phonemes(pronunciation, word_phonemes):
    mistakes = [True] * len(word_phonemes)
    compare_matrix = fill_compare_matrix(pronunciation, word_phonemes)
    matched_phonemes = []
    pr_it, w_it = len(pronunciation) - 1, len(word_phonemes) - 1
    prev_right = len(word_phonemes)
    while pr_it > 0 and w_it > 0:
        if pronunciation[pr_it] == word_phonemes[w_it]:
            matched_phonemes.append(word_phonemes[w_it])
            if prev_right - w_it > 1:
                mistakes[prev_right] = True
            else:
                mistakes[w_it] = False
            prev_right = w_it
            pr_it, w_it = pr_it - 1, w_it - 1
        elif compare_matrix[pr_it - 1][w_it] > compare_matrix[pr_it][w_it - 1]:
            pr_it -= 1
        else:
            w_it -= 1
    mistakes.reverse()
    return mistakes