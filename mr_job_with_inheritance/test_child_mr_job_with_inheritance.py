from mr_job_with_inheritance.child_mr_job_with_inheritance import MRMostUsedWord


def test_whole_MR_job() -> None:
    stdin = open("lorem_ipsum.txt", "rb")
    mr_job = MRMostUsedWord(['--no-conf'])
    mr_job.sandbox(stdin=stdin)

    results = []
    with mr_job.make_runner() as runner:
        runner.run()
        for key, value in mr_job.parse_output(runner.cat_output()):
            results.append(f"{key}:{value}")

        assert sorted(results) == ['13:in']
