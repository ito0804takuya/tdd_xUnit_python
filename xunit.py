# coding: UTF-8
# python2系では、上記の宣言がないとエラー発生する(このファイルには日本語が含まれるため)
# 今回は(anyenv)localをpython3.9にしたので不要

# 実行コマンド : python xunit.py

# class定義 --------------------------------
class TestCase:
  def __init__(self, name):
    self.name = name
  def setUp(self):
    pass # 未実行 (pass = Noneをreturnする)
  def tearDown(self): # 空実装だが、これがないとエラーになる
    pass
  # 自身のnameに応じたテストを実行する
  def run(self, result):
    result.testStarted()
    self.setUp()
    try:
      method = getattr(self, self.name) # 自身のクラスのname属性を取得
      # テストが実行されると、method=自身のname("test....")であるため、method()にてそれがメソッドとして呼ばれるようになる
      method()
    except:
      result.testFailed()
    self.tearDown()

class WasRun(TestCase): # TestCaseを継承
  def setUp(self):
    self.log = "setUp "
  def testMethod(self):
    self.log = self.log + "testMethod "
  def testBrokenMethod(self):
    raise Exception # 例外を発生させる
  def tearDown(self):
    self.log = self.log + "tearDown "

class TestResult:
  def __init__(self):
    self.runCount = 0
    self.errorCount = 0
  def testStarted(self): # テスト実行完了数
    self.runCount += 1
  def testFailed(self): # テスト失敗数
    self.errorCount += 1
  def summary(self): # テスト実行結果
    return "%d run, %d failed" % (self.runCount, self.errorCount)

# 複数のテストをまとめる
class TestSuite:
  def __init__(self):
    self.tests = []
  def add(self, test):
    self.tests.append(test)
  def run(self, result):
    for test in self.tests:
      test.run(result)

# テスト項目（シナリオ）
class TestCaseTest(TestCase):
  def setUp(self):
    self.result = TestResult()
  # テストの準備ができているか確認するテスト
  def testTemplateMethod(self):
    test = WasRun("testMethod") # テストオブジェクト
    test.run(self.result) # テスト実行
    assert(test.log == "setUp testMethod tearDown ")
  # テスト成功時の結果が出力できているか確認するテスト
  def testResult(self):
    test = WasRun("testMethod")
    test.run(self.result)
    assert(self.result.summary() == "1 run, 0 failed")
  # テスト失敗時の結果が出力できているか確認するテスト
  def testFailedResult(self):
    test = WasRun("testBrokenMethod")
    test.run(self.result)
    assert(self.result.summary() == "1 run, 1 failed")
  def testFailedResultFormatting(self):
    self.result.testStarted()
    self.result.testFailed()
    assert(self.result.summary() == "1 run, 1 failed")
  def testSuite(self):
    suite = TestSuite()
    seite.add(WasRun("testMethod")) # 成功したテスト
    seite.add(WasRun("testBrokenMethod")) # 失敗したテスト
    # 結果を取得
    suite.run(self.result)
    assert(self.result.summary() == "2 run, 1 failed")

# main() --------------------------------
suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())