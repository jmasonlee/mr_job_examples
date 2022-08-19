import io

from mr_job_with_increment_counter.child_mr_job_with_increment_counter import MRMostUsedWord


def test_whole_MR_job(capfd) -> None:
    stdin = open("lorem_ipsum.txt", "rb")
    stderr = open("stderr.txt", "w")
    mr_job = MRMostUsedWord(['--no-conf'])
    mr_job.sandbox(stdin=stdin, stderr=stderr)

    results = []
    with mr_job.make_runner() as runner:
        runner.run()
        for key, value in mr_job.parse_output(runner.cat_output()):
            results.append(f"{key}:{value}")

        stdin.close()
        stderr.close()
        #captured = capfd.readouterr()
        #assert sorted(results) == ['13:in']
        stderr = open("stderr.txt", "rb").read().decode("utf-8")
        print(stderr)
        assert False
