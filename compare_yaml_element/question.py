# q: 今天有一份yaml(xxx_need_to_add.yml) 資料,要跟xxx.yml比對
# 缺少的資料寫入,如果資料一模一樣就不寫入
# 所以這邊data1.yml經你的程式處理後資料會有三筆,data2.yml處理後維持一筆,
# 然後把答案輸出成answer_data1.yml,跟answer_data2.yml
# 該程式須可以重複執行,且不能有重複資料
# 提示可以先裝pyyaml( pip3 install pyyaml),import後,用yaml.safe_load跟yaml.dump協助