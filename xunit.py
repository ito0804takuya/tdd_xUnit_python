# coding: UTF-8
# python2系では、上記の宣言がないとエラー発生する(このファイルには日本語が含まれるため)
# 今回は(anyenv)localをpython3.9にしたので不要

# 実行コマンド : python xunit.py

# class定義 --------------------------------
class TestCase:
  def __init__(self, name):
    self.name = name
  # テストメソッドを実行
  def run(self):
    method = getattr(self, self.name) # 自身のクラスのname属性を取得
    method()

class WasRun(TestCase): # TestCaseを継承
  def __init__(self, name):
    self.wasRun = None # None = null(Rubyのnil)
    super().__init__(name)
  def testMethod(self):
    self.wasRun = 1

class TestCaseTest(TestCase):
  def testRunning(self):
    # テストメソッドが呼ばれたらtrue, 呼ばれなければfalseを出力する
    
    # 呼び出し前 : falseを期待
    test = WasRun("testMethod") # WasRunクラス, name = "testMethod"
    assert(not test.wasRun)

    # 呼び出し後 : trueを期待
    test.run()
    assert(test.wasRun)

# main() --------------------------------
TestCaseTest("testRunning").run()