#匯入os操作系統模塊(工具包)
#匯入HtmlTestRunner 工具 可產生 result report

import os, HtmlTestRunner

#從script匯入GA_AutoTest
from script import GA_AutoTest

#存放report路徑，op是變數可自己改
op = os.path.abspath('./result')

#runner 是變數可自己改 
#第一個HtmlTestRunner(大工具)，第二個HtmlTestRunner(大工具裡面其中一個功能)
#執行以下動作產生report，結果存放到op裡
runner = HtmlTestRunner.HTMLTestRunner(
    output = op,
)

#HtmlTestRunner(大工具)
#run(大工具裡面其中一個功能)
#run GA_AutoTest裡的suite() (小工具要加())
runner.run(GA_AutoTest.suite())
