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
  def run(self):
    self.setUp()
    method = getattr(self, self.name) # 自身のクラスのname属性を取得
    # テストが実行されると、method=自身のname("test....")であるため、method()にてそれがメソッドとして呼ばれるようになる
    method()
    self.tearDown()

class WasRun(TestCase): # TestCaseを継承
  def setUp(self):
    self.log = "setUp "
  def testMethod(self):
    self.log = self.log + "testMethod "
  def tearDown(self):
    self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
  # テストの準備ができているか確認するテスト
  def testTemplateMethod(self):
    test = WasRun("testMethod") # テストオブジェクト
    test.run() # テスト実行
    assert(test.log == "setUp testMethod tearDown ")

# main() --------------------------------
TestCaseTest("testTemplateMethod").run()