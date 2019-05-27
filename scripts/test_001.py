import allure

class Test001:

    @allure.step(title="测试步骤")
    def test_001(self):
        print("--->test_001")
        assert True