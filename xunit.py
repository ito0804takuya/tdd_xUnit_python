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

  # 自身のnameに応じたテストを実行する
  def run(self):
    self.setUp()
    method = getattr(self, self.name) # 自身のクラスのname属性を取得
    # テストが実行されると、method=自身のname("test....")であるため、method()にてそれがメソッドとして呼ばれるようになる
    method()

class WasRun(TestCase): # TestCaseを継承

  def setUp(self):
    self.wasRun = None # 未実行
    self.wasSetUp = 1 # 準備済み

  def testMethod(self):
    self.wasRun = 1 # 実行済み

class TestCaseTest(TestCase):

  # テストオブジェクトを準備するフィクスチャ
  def setUp(self):
    self.test = WasRun("testMethod")

  # テストが実行されたかどうか確認するテスト
  def testRunning(self):
    # テスト実行
    self.test.run()
    # 呼び出し後 : trueを期待
    assert(self.test.wasRun)

  # テストの準備ができているか確認するテスト
  def testSetUp(self):
    # テスト実行
    self.test.run()
    assert(self.test.wasSetUp)

# main() --------------------------------
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()