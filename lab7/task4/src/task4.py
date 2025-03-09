from lab7.utils import measure, file_write, file_read


def sample_length(seq1, seq2):
    n, m = len(seq1), len(seq2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def sample_main(seq1=None, seq2=None):
    if seq1 is None or seq2 is None:
        data = file_read()
        n, seq1 = data[0][0], data[1]
        m, seq2 = data[2][0], data[3]

        result = sample_length(seq1, seq2)
        file_write([result])
    else:
        result = sample_length(seq1, seq2)
    return result


if __name__ == '__main__':
    measure(sample_main)