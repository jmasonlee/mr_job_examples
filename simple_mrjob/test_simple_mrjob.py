from io import BytesIO

from simple_mrjob.simple_mrjob import MRWordFrequencyCount


def test_whole_MR_job() -> None:
    stdin = open("lorem_ipsum.txt", "rb")
    mr_job = MRWordFrequencyCount(['--no-conf'])
    mr_job.sandbox(stdin=stdin)

    results = []
    with mr_job.make_runner() as runner:
        runner.run()
        for key, value in mr_job.parse_output(runner.cat_output()):
            results.append(f"{key}:{value}")

        assert sorted(results) == ['chars:3392', 'lines:9', 'words:510']
