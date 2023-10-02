import main

rp = main.RandomPassword()


class TestPassword:
    def test_generate_password(self):
        assert len(rp.generate_password()) == 12
        assert len(rp.generate_password(20)) == 20
        assert isinstance(rp.generate_password(12), str)


t = TestPassword()
t.test_generate_password()
